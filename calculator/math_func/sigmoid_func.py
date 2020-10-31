# sigmoid_func.py
import math
import numbers

from ..helper import string_rep

@string_rep
def sigmoid(x:float)->float:
    """
    Function expects value real number as input and returns
    sigmoid (1/1+e^x) as output
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    return(1 / (1 + math.exp(-x)))

@string_rep
def d_sigmoid(x:float)->float:
    """
    Derivate of sigmoid(x) is sigmoid(x)(1-sigmoid(x)). Function takes input value x as real
    number
    """
    if not isinstance(x, numbers.Real):
        raise TypeError("Input value of invalid type")

    sigmd = 1 / (1 + math.exp(-x))
    return(sigmd * (1 - sigmd))
