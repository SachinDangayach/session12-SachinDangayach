# tan_func.py
import math
import numbers

from ..helper import string_rep

@string_rep
def tan(x:float)->float:
    """
    Function expects value x in radian ( math.pi radian = 180 Degree)
    and returns the tan(x)
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(math.tan(x))

@string_rep
def d_tan(x:float)->float:
    """
    Derivate of tan(x) is sec(x)^2. Function takes input value x in radian and
    returns sec(x)^2
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(1 + math.pow(math.tan(x), 2))
