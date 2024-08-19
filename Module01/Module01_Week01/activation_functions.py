# Module 1, Week 1, Q2
# Given function
def is_number (n):
  try :
    float (n) # Type - casting the string to ‘float ‘.
              # If string is not a valid ‘float ‘,
              # it ’ll raise ‘ValueError ‘ exception
  except ValueError :
    return False
  return True

# prompt: write python function to compute Sigmoid Function

import math

def cal_sigmoid(x):
  """
  This function computes the sigmoid function.

  Parameters:
    x (float): The input value.

  Returns:
    float: The sigmoid of x.
  """
  return 1 / (1 + math.exp(-x))

# prompt: write python function to compute ReLU Function

def cal_relu(x):
  """
  This function computes the rectified linear unit (ReLU) function.

  Parameters:
    x (float): The input value.

  Returns:
    float: The ReLU of x.
  """
  if x <= 0:
    return 0
  else:
    return x


# prompt: write python function to compute ELU Function

def cal_elu(x, alpha = 0.01):
  """
  This function computes the exponential linear unit (ELU) function.

  Parameters:
    x (float): The input value.
    alpha (float): alpha value, default=0.01
  Returns:
    float: The ELU of x.
  """
  if x > 0:
    return x
  else:
    return (math.exp(x) - 1) * alpha



def calc_activation_func(x, act_name):
  """
  This function computes the activation function based on user's input value x and selection of function.

  Parameters:
    x (float): The input value.
    function (str): The name of the activation function (sigmoid, relu, elu).

  Returns:
    float: The output of the activation function.
  """
  if is_number(x):
    if act_name == "sigmoid":
        return cal_sigmoid(x)
    elif act_name == "relu":
        return cal_relu(x)
    elif act_name == "elu":
        return cal_elu(x)
    else:
        print(f"Error: Invalid function name.")
        return
  else:
    print(f"Error: Input value must be a number.")
    return

# Test:
if __name__ == "__main__":
    assert is_number (3) == 1.0
    assert is_number (' -2a') == 0.0
    print ( is_number (1))
    print ( is_number ('n'))

    assert round ( cal_sigmoid (3) , 2) ==0.95
    print ( round ( cal_sigmoid (2) , 2))

    assert round ( cal_elu (1))==1
    print ( round ( cal_elu ( -1) , 2))

    assert calc_activation_func (x = 1, act_name ='relu') == 1
    print ( round ( calc_activation_func (x = 3, act_name ='sigmoid'), 2))

    print(calc_activation_func(-2, "sigmoid"))
    print(calc_activation_func(-2, "relu"))
    print(calc_activation_func(-2, "elu"))

    # get 2 inputs from user
    x = float(input("Enter value of x: "))
    function = input("Enter activation function (sigmoid or relu or elu): ")
    print(calc_activation_func(x, function))