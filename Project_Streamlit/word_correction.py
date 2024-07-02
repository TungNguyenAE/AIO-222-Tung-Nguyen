'''
This is a simple word correction module by calculating the Levenshtein distance
between given and each word in a vocabulary database.

Functions:
    load_vocab(file_path): Loading vocabulary database.
    levenshtein_distance(token1, token2): Calculate Levenshtein distance between two words.
    main(): Run web UI using Streamlit
'''

import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    words = sorted(set([line.strip() for line in lines]))
    return words


def levenshtein_distance(token1, token2):
    len1, len2 = len(token1), len(token2)
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        distances[i][0] = i

    for j in range(len2 + 1):
        distances[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            distances[i][j] = min(
                distances[i - 1][j] + 1,       # Deletion
                distances[i][j - 1] + 1,       # Insertion
                distances[i - 1][j - 1] + cost  # Substitution
            )

    return distances[len1][len2]


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word:")

    if st.button("Compute"):
        # Compute Levenshtein distance
        leven_distances = {vocab: levenshtein_distance(
            word, vocab) for vocab in vocabs}

        # Sorted by distance
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))

        # Get the correct word
        correct_word = list(sorted_distances.keys())[0]
        st.write("Correct word:", correct_word)

        # Display vocabulary and distances
        col1, col2 = st.columns(2)
        col1.write("Vocabulary:")
        col1.write(vocabs)

        col2.write("Distances:")
        col2.write(sorted_distances)


if __name__ == "__main__":
    vocabs = load_vocab('./data/vocab.txt')
    main()
