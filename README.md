
# EPAI Session 12 Assignment by Sachin Dangayach

This assignment is based on the concepts of "Packages".  We have created Modules in earlier assignment. To create the package, we add \_\_init__.py file in the folder. There are Namespace packages where we don't add \_\_init.py__ file. Packages and Modules helps to make code more manageable where logically similar entities and placed together and thus it help in not only during development but also for the end users to consume the developed functionalities . In this assignment we have created a calculator package with following functionalities-
#
Build a calculator package that has separate module for:  

1.  sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
2.  The modules shall include their derivatives as well
3.  If we do import calculator, we should be able to access all the above function (except derivatives)
4.  For derivates we must do: from package import derivatives.
5.  Outputs are returned as well as printed using only f-string
6.  Write simple test cases to check the outputs of each operator and their derivative

### Solution:-
Build the package with following structure
**Calculator**
- \_\_init.py__
- math_func (contains following modules)
--	sin
-- cos
-- tan
-- tanh
-- sigmoid
-- softmax
-- relu
-- euler
-- log
-- \__init__.py
- derivatives module to expose derivative functions inside math_func
- helper module for formatted output using f string

## Test Cases-

### Below are test cases functions in test_session12.py file.

## Check for coding standards-

## 1. test_readme_exists :
Test for readme exists

## 2. test_readme_contents :
Test for readme contents are more than 500 words

## 3. test_readme_proper_description :
Test for all important functions/class described well in your README.md file

## 4. test_readme_file_for_formatting :
Test for readme formatting

## 5. test_indentations :
Test for source code formatting. No tabs but four spaces are used for indentation

## 6. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

## 7. test_function_count :
Test to check minimum 20 functions are provided

## 8. test_function_repeatations:
Test for no function is repeated

## 9. test_doc_string:
Test to check doc strings

## 10. test_function_name_had_cap_letters :
Test for no function is with capitals in source code

## Test cases for assignments

## 11. test_value_errors:
Test to check the value errors in case incorrect values are passed as arguments

## 12. test_type_error:
Test to check the type error in case values passed as argument are not of required type
