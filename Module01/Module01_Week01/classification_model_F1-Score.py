# Module 1, Week 1, Q1
import math

#Classification model wwith F1-Score.

def calc_f1_score (tp , fp , fn):
    """
    Calculate the F1-score given true positives, false positives, and false negatives.

    Parameters:
    tp (int): The number of true positives. Must be a non-negative integer.
    fp (int): The number of false positives. Must be a non-negative integer.
    fn (int): The number of false negatives. Must be a non-negative integer.

    Returns:
    tuple: A tuple containing F1-score, printout error and return none if inputs are invalid.
    """
    # Check if inputs are integers and greater than 0
    if not (isinstance(tp, int) and isinstance(fp, int) and isinstance(fn, int)):
        print("Error: tp, fp, and fn must be int.")
        return

    # Check if inputs are greater than 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("Error: tp, fp, and fn must be greater than zero.")
        return

    # Calculate precision and recall
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    # Calculate F1-score
    f1 = 2 * (precision * recall) / (precision + recall)

    # Output precision, recall, and F1-score
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")
    return f1

# Test:
if __name__ == "__main__":
    calc_f1_score (tp =2, fp =3, fn =5)
    calc_f1_score (tp =2, fp =0, fn =5)

    assert math.isclose(round ( calc_f1_score (tp =2, fp =3, fn =5) , 2), 0.33, rel_tol=1e-09, abs_tol=1e-09)
    print ( round ( calc_f1_score (tp =2, fp =4, fn =5) , 2))