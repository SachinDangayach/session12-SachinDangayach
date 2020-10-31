# sin_func.py
import math
import numbers

from ..helper import string_rep

@string_rep
def sin(x:float)->float:
    """
    Function expects value x in radian ( math.pi radian = 180 Degree)
    and returns the sin(x)
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.sin(x))

@string_rep
def d_sin(x:float)->float:
    """
    Derivate of sin(x) is cos(x). Function takes input value x in radian and
    returns cos(x)
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.cos(x))
