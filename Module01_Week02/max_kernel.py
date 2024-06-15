def max_kernel(num_list, k):
    """
    Finds the maximum value in a sliding window of size k in a given 1D list of numbers.
    Args:
      num_list (list): A list of numbers.
      k (int):  The size of the sliding window.
    Returns:
      A list of maximum values in the sliding windows.
    """

    result = []
    for i in range(len(num_list)-k+1):
        result.append(max(num_list[i:i+k]))
    return result


# Testcases:
if __name__ == "__main__":
    assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(max_kernel(num_list, k))
