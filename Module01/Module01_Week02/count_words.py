def count_words(file_path):
    """
    Counts the occurrence of each word in a text file downloaded from the given file path.

    Args:
      file_path: The path of the text file.

    Returns:
      A dictionary containing the counts of each word.
    """

    with open(file_path, "r") as f:
        text = f.read()

    # Count the words in the text
    word_counts = {}
    for word in text.split():
        word = word.lower()
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

    return word_counts


# Testcases:
if __name__ == "__main__":
    url = "https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko"
    # Download the text file
    !gdown {url}
    file_path = "/content/P1_data.txt"
    result = count_words(file_path)

    assert result["who"] == 3
    print(result["man"])

    # Print the word counts
    # for word, count in word_counts.items():
    #    print(f'Word {word} appears {count} times.')
