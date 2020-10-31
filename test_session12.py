# test_session12

import pytest
import re
import inspect
import os
import math
import test_session12
import calculator
from calculator import derivaties_func as derivatives


README_CONTENT_CHECK_FOR = [
                'calculator',
                'module',
                'package',
                'cos',
                'sin',
                'log',
                'relu',
                'sigmoid',
                'softmax',
                'tan',
                'tanh',
                'derivatives',
                'euler',
            ]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    """get file content"""
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    """Check readme description"""
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    """Check readme formatting"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically
    significant indenting.'''
    lines = inspect.getsource(calculator)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    """Check no capital letters are used in function names"""
    functions = inspect.getmembers(calculator, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_count():
    """Check function count"""
    functions = inspect.getmembers(test_session12, inspect.isfunction)
    assert len(functions) > 10, 'Minimum 10 testcase required'

def test_function_repeatations():
    '''to check repeating fucntions'''
    functions = inspect.getmembers(test_session12, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Duplicate testcase found'

############################## Modules Validations #############################

def test_sin_module():

    assert 0.8509035245341184 == calculator.sin(45), "sin_func module from cal package is not working as expected"
    assert 0.5253219888177297 == derivatives.d_sin(45), "sin_func module from cal package is not working as expected"

def test_cos_module():

    assert 0.5253219888177297 == calculator.cos(45), "cos_func module from cal package is not working as expected"
    assert -0.8509035245341184 == derivatives.d_cos(45), "cos_func module from cal package is not working as expected"

def test_tan_module():

    assert 1.6197751905438615 == calculator.tan(45), "tan_func module from cal package is not working as expected"
    assert 3.623671667901403 == derivatives.d_tan(45), "tan_func module from cal package is not working as expected"

def test_tanh_module():

    assert 1.0 == calculator.tanh(45), "tanh_func module from cal package is not working as expected"
    assert 0.0 == derivatives.d_tanh(45), "tanh_func module from cal package is not working as expected"

def test_log_module():

    assert 0.6989700043360187 == calculator.log(5, 10), "log_func module from cal package is not working as expected"
    assert 0.08685889638065035 == derivatives.d_log(5, 10), "log_func module from cal package is not working as expected"

def test_euler_module():

    assert 148.4131591025766 == calculator.euler(5), "euler_func module from cal package is not working as expected"
    assert 1.6487212707001282 == derivatives.d_euler(0.5), "euler_func module from cal package is not working as expected"


def test_sigmoid_module():

    assert 0.6224593312018546 == calculator.sigmoid(0.5), "sigmoid_func module from cal package is not working as expected"
    assert 0.2350037122015945 == derivatives.d_sigmoid(0.5), "sigmoid_func module from cal package is not working as expected"

def test_relu_module():

    assert 0.5 == calculator.relu(0.5), "relu_func module from cal package is not working as expected"
    assert 0 == derivatives.d_relu(-20), "relu_funcmodule from cal package is not working as expected"
    assert 1 == derivatives.d_relu(10), "relu_func module from cal package is not working as expected"

def test_value_errors():

    with pytest.raises(ValueError, match=r".*should be greater than 0*"):
        calculator.log(0, 2)

    with pytest.raises(ValueError, match=r".*value should be greater than 0*"):
        calculator.log(-2, 10)

    with pytest.raises(ValueError, match=r".*base should be greater than 0 and not equal to 1*"):
        calculator.log(5, -10)

    with pytest.raises(ValueError, match=r".*base should be greater than 0 and not equal to 1*"):
        calculator.log(5, 1)

    with pytest.raises(ValueError, match=r".*value should be greater than 0*"):
        derivatives.d_log(0, 10)

    with pytest.raises(ValueError, match=r".*value should be greater than 0*"):
        derivatives.d_log(-2, 10)

    with pytest.raises(ValueError, match=r".*base should be greater than 0 and not equal to 1*"):
        derivatives.d_log(5, -10)

    with pytest.raises(ValueError, match=r".*base should be greater than 0 and not equal to 1*"):
        derivatives.d_log(5, 1)

def test_type_error():

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.sin("60")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.cos("-45")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.tan("4.5")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.tanh("50")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.relu("1.3")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.sigmoid("2.4")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.euler("4")

    with pytest.raises(TypeError, match=r".*invalid type*"):
        calculator.softmax([10, "2", "3"])

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.log("5", 10)

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        calculator.log(3, "10")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_sin("45")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_cos("4.5")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_tan("45")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_tanh([1,3])

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_euler("10")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_sigmoid("3")

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_relu("-5")

    with pytest.raises(TypeError, match=r".*invalid type*"):
        derivatives.d_softmax([20, "3", 5])

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_log("5", 20)

    with pytest.raises(TypeError, match=r".*Input value of invalid type*"):
        derivatives.d_log(5, "20")
