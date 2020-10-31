# tanh_func.py
import math
import numbers

from ..helper import string_rep

@string_rep
def tanh(x:float)->float:
    """
    Function expects value real number as input
    and returns the tanh(x)
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.tanh(x))

@string_rep
def d_tanh(x:float)->float:
    """
    Derivate of sin(x) is 1 - tanh2 x. Function takes real number as input
    and returns 1 - tanh^2(x))
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(1 - math.pow(math.tanh(x), 2))
