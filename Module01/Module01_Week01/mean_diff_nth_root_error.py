# Module 1, Week 1, Q5
# prompt: function to calculate difference of nth root error for a pair of data y and y_hat given n and p value

def mean_diff_nth_root_error(y, y_hat, n, p):
  """
  This function computes the difference of nth root error for a pair of data y and y_hat given n and p value.

  Parameters:
    y (float): The actual value.
    y_hat (float): The predicted value.
    n (int): The order of the root.
    p (int): The power of the difference.

  Returns:
    float: The difference of nth root error.
  """
  diff_nth = ((y**(1/n)) - (y_hat**(1/n)))**p
  return diff_nth

# Test:
if __name__ == "__main__":
    print (f"diffirence of nth root error is {mean_diff_nth_root_error(100,99.5,2,1)}")
    print (f"diffirence of nth root error is {mean_diff_nth_root_error(50,49.5,2,1)}")
    print (f"diffirence of nth root error is {mean_diff_nth_root_error(20,19.5,2,1)}")
    print (f"diffirence of nth root error is {mean_diff_nth_root_error(0.6,0.1,2,1)}")