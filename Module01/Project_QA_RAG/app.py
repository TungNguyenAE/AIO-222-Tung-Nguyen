import chainlit as cl
import torch

from chainlit.types import AskFileResponse

from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFacePipeline

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain import hub

# Function to load and split file


def process_file(file: AskFileResponse):
    if file.type == "text/plain":
        loader = TextLoader
    elif file.type == "application/pdf":
        loader = PyPDFLoader

    file_loader = loader(file.path)
    documents = file_loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    for i, doc in enumerate(docs):
        doc.metadata['source'] = f"source_{i}"
    return docs

# Function to get vector database


def get_vector_db(file: AskFileResponse):
    docs = process_file(file=file)
    cl.user_session.set("docs", docs)
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=HuggingFaceEmbeddings()
    )
    return vector_db

# Function to get LLMs (Vicuna)


def get_huggingface_llm():
    model_name = "lmsys/vicuna-7b-v1.5"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Set device to "cpu"
    model_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        device=torch.device("cpu")
    )

    llm = HuggingFacePipeline(
        pipeline=model_pipeline,
    )
    return llm


LLM = get_huggingface_llm()
welcome_message = """Welcome to the PDF QA! To get started:
1. Upload a PDF or text file
2. Ask a question about the file
"""


@cl.on_chat_start
async def on_chat_start():
    files = None
    while files is None:  # Wait until a file is uploaded
        files = await cl.AskFileMessage(
            content=welcome_message,  # Message prompting for file
            accept=["text/plain", "application/pdf"],  # Allowed file types
            max_size_mb=20,
            timeout=180,  # Wait 3 minutes for file
        ).send()
    file = files[0]  # Get the uploaded file

    # Processing message
    msg = cl.Message(content=f"Processing '{
                     file.name}'...", disable_feedback=True)
    await msg.send()

    # Create vector database from the file (asynchronously)
    vector_db = await cl.make_async(get_vector_db)(file)

    # Initialize conversation history and memory
    message_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )

    # Create a retriever for searching the vector database
    retriever = vector_db.as_retriever(
        search_type="mmr", search_kwargs={'k': 3})

    # Create a conversational retrieval chain using the LLM
    chain = ConversationalRetrievalChain.from_llm(
        llm=LLM,
        chain_type="stuff",
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

    # Update the processing message
    msg.content = f"‘{file.name}’ processed. You can now ask questions!"
    await msg.update()

    cl.user_session.set("chain", chain)  # Store the chain in the user session


@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")
    cb = cl.AsyncLangchainCallbackHandler()
    res = await chain.ainvoke(message.content, callbacks=[cb])
    answer = res["answer"]
    source_documents = res["source_documents"]
    text_elements = []

    if source_documents:
        for source_idx, source_doc in enumerate(source_documents):
            source_name = f"source_{source_idx}"
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name)
            )
        source_names = [text_el.name for text_el in text_elements]

        if source_names:
            answer += f"\nSources: {', '.join(source_names)}"
        else:
            answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()


if __name__ == "__main__":
    cl.run()
