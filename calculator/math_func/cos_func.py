# cos_func.py
import math
import numbers

from ..helper import string_rep

@string_rep
def cos(x:float)->float:
    """
    Function expects value x in radian ( math.pi radian = 180 Degree)
    and returns the sin(x)
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.cos(x))

@string_rep
def d_cos(x:float)->float:
    """
    Derivate of cos(x) is -sin(x). Function takes input value x in radian and
    returns -sin(x)
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(-math.sin(x))
