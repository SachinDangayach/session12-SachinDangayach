# relu.py
import math
import numbers

from ..helper import string_rep

@string_rep
def relu(x:float)->float:
    """
    Function expects real number x as input and returns 0 if x <= 0
    and x otherwise as output
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(0 if x<=0 else x)

@string_rep
def d_relu(x:float)->float:
    """
    Derivate of relu for a real number x is 0 if x <= 0 and 1 otherwise
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(0 if x<=0 else 1)
