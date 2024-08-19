# Module 1, Week 1, Q4
# prompt: write function to compute factorial of user input value x , checking if x if not negative

def factorial(x):
    """
    This function computes the factorial of a non-negative integer x.

    Parameters:
      x (int): The non-negative integer.

    Returns:
      int: The factorial of x.
    """
    if x < 0:
        print("x must be a non-negative integer.")
        return
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

# prompt: write function to compute sin(x) using n number of iterations, in which x is user input value in radian and n is user input value


def approx_sin(x, n):
    """
    This function computes the sine of x using the Taylor series expansion with n number of iterations.

    Parameters:
      x (float): The input value in radians.
      n (int): The number of iterations.

    Returns:
      float: The approximated sine of x.
    """
    sin_x = 0
    for i in range(n):
        sign = (-1)**i
        term = (x**(2*i + 1))/(factorial(2*i + 1))
        sin_x += sign * term
    return sin_x

# prompt: write function to compute cos(x) using n number of iterations, in which x is user input value in radian and n is user input value


def approx_cos(x, n):
    """
    This function computes the cosine of x using the Taylor series expansion with n number of iterations.

    Parameters:
      x (float): The input value in radians.
      n (int): The number of iterations.

    Returns:
      float: The approximated cosine of x.
    """
    cos_x = 0
    for i in range(n):
        sign = (-1)**i
        term = (x**(2*i))/(factorial(2*i))
        cos_x += sign * term
    return cos_x

# prompt: write function to compute sinh(x) using n number of iterations, in which x is user input value in radian and n is user input


def approx_sinh(x, n):
    """
    This function computes the sinh of x using the Taylor series expansion with n number of iterations.

    Parameters:
      x (float): The input value in radians.
      n (int): The number of iterations.

    Returns:
      float: The approximated sinh of x.
    """
    sinh_x = 0
    for i in range(n):
        sinh_x += (x**(2*i + 1))/(factorial(2*i + 1))
    return sinh_x

# prompt: write function to compute cosh(x) using n number of iterations, in which x is user input value in radian and n is user input


def approx_cosh(x, n):
    """
    This function computes cosh of x using the Taylor series expansion with n number of iterations.

    Parameters:
      x (float): The input value in radians.1
      n (int): The number of iterations.

    Returns:
      float: The approximated cosh of x.
    """
    cosh_x = 0
    for i in range(n):
        cosh_x += (x**(2*i))/(factorial(2*i))
    return cosh_x


# Test:
if __name__ == "__main__":
    import math
    # Get input from user
    x = int(input("Enter a non-negative integer: "))
    # Compute and print the factorial
    factorial_x = factorial(x)
    print(f"The factorial of {x} is: {factorial_x}")
    getinput_x = "Enter the value of x in radians: "
    getinput_ite = "Enter the number of iterations: "

    # Get input from user
    x = float(input(getinput_x))
    n = int(input(getinput_ite))
    # Compute and print the approximated sine
    sin_x = approx_sin(x, n)
    print(f"The approximated sine of {x} using {n} iterations is: {sin_x}")

    assert math.isclose(round(approx_sin(x=1, n=10), 4),
                        0.8415, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_sin(x=3.14, n=10), 4))

    # Get input from user
    x = float(input(getinput_x))
    n = int(input(getinput_ite))
    # Compute and print the approximated cosine
    cos_x = approx_cos(x, n)
    print(f"The approximated cosine of {x} using {n} iterations is: {cos_x}")
    assert math.isclose(round(approx_cos(x=1, n=10), 2),
                        0.54, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_cos(x=3.14, n=10), 2))

    # Get input from user
    x = float(input(getinput_x))
    n = int(input(getinput_ite))
    # Compute and print the approximated sinh
    sinh_x = approx_sinh(x, n)
    print(f"The approximated sinh of {x} using {n} iterations is: {sinh_x}")

    assert math.isclose(round(approx_sinh(x=1, n=10), 2),
                        1.18, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_sinh(x=3.14, n=10), 2))

    # Get inputs from user
    x = float(input(getinput_x))
    n = int(input(getinput_ite))
    # Compute and print the approximated cosh
    cosh_x = approx_cosh(x, n)
    print(f"The approximated cosh of {x} using {n} iterations is: {cosh_x}")

    assert math.isclose(round(approx_cosh(x=1, n=10), 2),
                        1.54, rel_tol=1e-09, abs_tol=1e-09)
    print(round(approx_cosh(x=3.14, n=10), 2))
