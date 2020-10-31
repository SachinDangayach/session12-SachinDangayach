# helper.py

def string_rep(func):
    """
    Clouser to provide the string representation of a function
    """
    def inner(*args,**kwargs):
        """function to provide the function call and string representation"""
        result = func(*args,**kwargs)
        print(f'Function: {func.__name__} called with Arguments:{args} returns: {result}')
        return(result)
    return(inner)
