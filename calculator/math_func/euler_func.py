# euler.py
import math
import numbers

from ..helper import string_rep

@string_rep
def euler(x:float)->float:
    """
    Function expects real number as input and returns e raised to the
    power of x at output
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.exp(x))

@string_rep
def d_euler(x:float)->float:
    """
    Derivate of e^x is e^x. Function takes input as real number x and
    returns e^x as output
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.exp(x))
