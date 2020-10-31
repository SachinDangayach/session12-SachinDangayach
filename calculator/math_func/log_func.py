# log.py
import math
import numbers

from ..helper import string_rep

@string_rep
def log(x:float,base:float)->float:
    """
    Function expects positive real number as input. base should be greater than
    0 and not 1. Function returns log(x) to the base n as output
    """
    if not (isinstance(x, numbers.Real) and isinstance(base, numbers.Real)):
        raise TypeError("Input value of invalid type")

    if x <= 0:
        raise ValueError("Input value should be greater than 0")

    if base <= 0 or base == 1:
        raise ValueError("base should be greater than 0 and not equal to 1")

    return(math.log(x, base))

@string_rep
def d_log(x:float,base:float)->float:
    """
    Derivate of e^x is e^x. Function takes input as real number x and
    returns e^x as output
    """
    if not (isinstance(x, numbers.Real) and isinstance(base, numbers.Real)):
        raise TypeError("Input value of invalid type")

    if x <= 0:
        raise ValueError("Input value should be greater than 0")

    if base < 0 or base == 1:
        raise ValueError("base should be greater than 0 and not equal to 1")

    return(1 / (x * math.log(base)))
