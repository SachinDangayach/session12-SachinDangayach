# soft_max_func.py
import math
import numbers

from ..helper import string_rep

@string_rep
def softmax(x:list)->list:
    """
    Function expects a list of values x as return a list of values
    as per computed softmax values
    """
    if not isinstance(x, list):
        raise TypeError("Input value of invalid type")

    for value in x:
        if not isinstance(value, numbers.Real):
            raise TypeError(f"Input list has {value} of invalid type")

    if not len(list):
        raise TypeError(f"No input value is provided")

    max_value = max(x)
    total = [math.exp(i - max_list) for i in x]
    result = [i/sum(total) for i in total]

    return(result)

@string_rep
def d_softmax(x:float)->float:
    """
    Derivate of softmax depends on  index of S(z_i), and z_j !
    Meaning if we are computing frac{S(z_i)}{\partial z_i} the rule is
    always: S(z_i) times (1 - S(z_i)). However, if we are computing frac{S(z_i)}{\partial z_j},
    where we are taking the derivative of the output of neuron i,
    that is S(z_i), w.r.t the input of neuron j, that is z_j.
    In this case the rule changes to: -S(z_i) times S(z_j)
    reference from https://www.mldawn.com/the-derivative-of-softmaxz-function-w-r-t-z/
    """
    if not isinstance(x, list):
        raise TypeError("Input value of invalid type")

    for value in x:
        if not isinstance(value, numbers.Real):
            raise TypeError(f"Input list has {value} of invalid type")

    if not len(list):
        raise ValueError(f"No input value is provided")

    max_list = max(x)
    total = [math.exp(i - max_list) for i in x]
    softmax_out = [i/sum(total) for i in total]

    result = []
    for idx, input_val in enumerate(x):
        res_index = []
        for sm_idx, softmax_val in enumerate(softmax_out):
            if idx == sm_idx:
                sm_diff = softmax_val * (1 - softmax_val)
            else:
                sm_diff = -1 * softmax_val * softmax_out[idx]
            res_index.append(sm_diff)
        result.append(res_index)

    return(result)
