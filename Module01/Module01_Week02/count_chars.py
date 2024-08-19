def count_characters(text):
    """
    Counts the occurrence of each letter in a given text string.

    Args:
      text: The text string to analyze.

    Returns:
      A dictionary containing the counts of each letter.
    """

    character_statistic = {}
    for letter in text:
        if letter not in character_statistic:
            character_statistic[letter] = 0
        character_statistic[letter] += 1

    return character_statistic


# Testcases:
if __name__ == "__main__":
    assert count_characters("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
    print(count_characters("smiles"))
