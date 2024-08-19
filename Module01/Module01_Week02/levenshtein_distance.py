def levenshtein_distance(string1, string2):
    """
    Calculates the Levenshtein distance between two strings.

    Args:
      string1: The first string.
      string2: The second string.

    Returns:
      The Levenshtein distance between the two strings.
    """

    if not string1:
        return len(string2)
    if not string2:
        return len(string1)

    # Create a matrix to store the distances between prefixes.
    distances = [[0 for _ in range(len(string2) + 1)]
                 for _ in range(len(string1) + 1)]

    # Initialize the first row and column of the matrix.
    for i in range(len(string1) + 1):
        distances[i][0] = i
    for j in range(len(string2) + 1):
        distances[0][j] = j

    # Fill in the rest of the matrix.
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                cost = 0
            else:
                cost = 1
            distances[i][j] = min(
                distances[i - 1][j] + 1,  # deletion
                distances[i][j - 1] + 1,  # insertion
                distances[i - 1][j - 1] + cost  # substitution
            )

    # The last element of the matrix is the Levenshtein distance.
    return distances[len(string1)][len(string2)]


# Testcases:
if __name__ == "__main__":
    string1 = "kitten"
    string2 = "sitting"

    distance = levenshtein_distance(string1, string2)
    print(f'The Levenshtein distance between "{
          string1}" and "{string2}" is {distance}.')
    assert levenshtein_distance("hi", "hello") == 4
    print(levenshtein_distance(" hola ", "hello"))
