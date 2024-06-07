# Module 1, Week 1, Q3
# prompt: write python function to compute regression loss given user's input number of samples n to use to generate samples using random function with range from 0 to 10 and selection of function out of these three: MAE Function, MSE Function or RMSE Function
import numpy as np
import math
import random

def calc_ae (y, y_hat ):
  return np.abs(y - y_hat)

# Test:
y = 1
y_hat = 6
assert calc_ae (y, y_hat )==5
y = 2
y_hat = 9
print ( calc_ae (y, y_hat ))

def calc_se (y, y_hat ):
  return np.square(y - y_hat)

# Test:
y = 4
y_hat = 2
assert calc_se (y, y_hat ) == 4
print ( calc_se (2, 1))


def loss_function(n='', function=''):
  """
  This function computes the regression loss based on user's input number of samples n to use to generate samples using random function with range from 0 to 10 and selection of function out of these three: MAE Function, MSE Function or RMSE Function

  Parameters:
    n (int): The number of samples to generate.
    function (str): The name of the loss function (mae, mse, rmse).

  Returns:
    float: The regression loss.
  """
  # Generate random samples
  y_target = []
  y_predict = []
  loss = []
  for i in range(n):
    y_target.append(random.uniform(0, 10))
    y_predict.append(random.uniform(0, 10))
    # Compute the loss based on the selected function
    if function == "MAE":
      loss.append(np.abs(y_target[i] - y_predict[i]))
    elif function == "MSE":
      loss.append(np.square(y_target[i] - y_predict[i]))
    elif function == "RMSE":
      loss.append(np.square(y_target[i] - y_predict[i]))
    else:
      print(f"Error: Invalid function name.")
      return
    print(f"loss name : {function} , sample : {i}, Prediction: {y_predict[i]}, Target: {y_target[i]}, loss: {loss[i]}")
  if not function == "RMSE":
    return sum(loss)/len(loss)
  else:
    return np.sqrt(sum(loss)/len(loss))

# Test:
if __name__ == "__main__":
  # Get input from user
  n = input("Enter number of samples n: ")
  if not n.isnumeric() or int(n) <= 0:
    print(f"Error: n must be a number and > 0.")
  else:
    n = int(n)
    function = input("Enter loss function (MAE or MSE or RMSE): ")
    # Compute and print the loss
    loss = loss_function(n, function)
    print(f"The final {function} loss is: {loss}")