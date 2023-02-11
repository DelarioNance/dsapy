# Errors

## Background

### Summary
- A Markdown file containing the errors which arose during the
  creation and testing of the ArrayList class, as well as the 
  methods used to resolve the errors.


### Author
- Delario Nance, Jr. ([email](mailto:denance@davidson.edu))


### Date
- January 24, 2023 - January 27, 2023


### [Table of Contents](#table-of-contents)
- [Errors](#errors)
  - [Background](#background)
    - [Summary](#summary)
    - [Author](#author)
    - [Date](#date)
    - [Table of Contents](#table-of-contents)
- [Setting up Unit Test Script](#setting-up-unit-test-script)
  - [Issue 1 - Importing `ArrayList` Class in Unit Test Script](#issue-1---importing-arraylist-class-in-unit-test-script)
    - [Specific Errors](#specific-errors)
    - [Meaning of Errors](#meaning-of-errors)
    - [Possible Reasons for Errors](#possible-reasons-for-errors)
    - [Unsuccessful Methods](#unsuccessful-methods)
    - [True Reason for Error](#true-reason-for-error)
    - [Solution for Errors](#solution-for-errors)
    - [Resources](#resources)
  - [Issue 2 - Importing `random_array_list` Function in Unit Test Script](#issue-2---importing-random_array_list-function-in-unit-test-script)
    - [Specific Errors](#specific-errors-1)
    - [Meaning of Errors](#meaning-of-errors-1)
    - [True Reason for Errors](#true-reason-for-errors)
    - [Solution for Errors](#solution-for-errors-1)
  - [Issue 3 - Importing `ArrayList` class when Running PyTest](#issue-3---importing-arraylist-class-when-running-pytest)
    - [Specific Errors](#specific-errors-2)
    - [Meaning of Errors](#meaning-of-errors-2)
    - [Unsuccessful Methods](#unsuccessful-methods-1)
    - [True Reason for Error](#true-reason-for-error-1)
    - [Solution for Errors](#solution-for-errors-2)
    - [References](#references)
  - [Issue 4 - Running `test_get_size_of_empty_ArrayList` Unit Test for `ArrayList` Class with PyTest Results in No Tests Being Ran](#issue-4---running-test_get_size_of_empty_arraylist-unit-test-for-arraylist-class-with-pytest-results-in-no-tests-being-ran)
    - [Specific Errors](#specific-errors-3)
    - [True Reason for Error](#true-reason-for-error-2)
    - [Solution for Errors](#solution-for-errors-3)
- [Integration Testing `ArrayList` Class](#integration-testing-arraylist-class)
  - [Issue 1 - Passing `TestCheckingIfEqual` Integration Tests](#issue-1---passing-testcheckingifequal-integration-tests)
    - [Specific Errors](#specific-errors-4)
    - [Possible Reasons for Errors](#possible-reasons-for-errors-1)
    - [True Reason for Error](#true-reason-for-error-3)
    - [Solution for Errors](#solution-for-errors-4)
    - [References](#references-1)
    - [References](#references-2)

---

# [Setting up Unit Test Script](#table-of-contents)

## [Issue 1](#table-of-contents) - Importing `ArrayList` Class in Unit Test Script

Date: January 24, 2023

### Specific Errors
1. When trying to run `from src.ArrayList import ArrayList` in the `dsapy/testing/unit/unit_ArrayList.py` file in VSCode with Code Runner, the following error arose:
```
ModuleNotFoundError: No module named 'src'
```

### Meaning of Errors
1. When running the `dsapy/testing/unit/unit_ArrayList.py` file, the computer is not aware of the `src` directory that contains the `ArrayList.py` file

### Possible Reasons for Errors
- When running the `test_unit_ArrayList.py` file, the computer is only aware of files and directories contained with the same directory that `test_unit_ArrayList.py` is in (i.e., `dsapy/testing/unit`). Since the `src` directory is not in the `dsapy/testing/scripts/unit` directory, the computer is not aware of any module named `src`.

### Unsuccessful Methods
- Method 1
  - Explanation
    - Rather than beginning the file path used for `import` with `src`, start the file path with `dsapy` since it is the lowest directory which contains both the `ArrayList.py` file and the `test_unit_ArrayList.py` file
  - Specific Approach
    - Run `from dsapy.src.ArrayList import ArrayList` instead of `from src.ArrayList import ArrayList` in the `dsapy/testing/unit/unit_ArrayList.py` file
  - Result
    - Like how no module named `src` could be found, now, no module named `dsapy` could be found
    ```
    ModuleNotFoundError: No module named 'dsapy'
    ```

### True Reason for Error
- When running the `test_unit_ArrayList.py` file, Python maintains a list of filepaths which one can see by running the following:
```
import sys
print(sys.path)
```
- With these filepaths, Python can access any file whose file path begins with any of these filepaths. However, when running the `test_unit_ArrayList.py` file, no such filepath contained the `src` directory.

### Solution for Errors
- I included the following lines in the `test_unit_ArrayList.py` file to add into Python's list of filepaths a filepath containing the `src` directory (5):
```
import sys
sys.path.append("c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\src")
```
- Since Python is now aware of the `src` directory, we can change the line `from src.ArrayList import ArrayList` to `from ArrayList import ArrayList`

### Resources
1. [Stack Overflow - Python - ModuleNotFoundError: No module named](https://stackoverflow.com/questions/61532337/python-modulenotfounderror-no-module-named)
2. [How to Import from Another Folder in Python](https://fedingo.com/how-to-import-from-another-folder-in-python/#:~:text=How%20to%20Import%20from%20Another%20Folder%20in%20Python,module%20folder%20location.%20...%202%202.%20Using%20Pythonpath)
3. [YouTube - Importing files from different folder](https://www.youtube.com/watch?v=ZYFug798Tcw)
4. [Stack Overflow - import python module using sys.path.append](https://stackoverflow.com/questions/48885445/import-python-module-using-sys-path-append)
5. [AppDividend - Python sys.path.appen() Method: The Guide](https://appdividend.com/2022/09/27/python-sys-path-append/#:~:text=Python%20sys.path.append%20%28%29%201%20Syntax%20sys.path.append%20%28path%29%202,need%20to%20import%20the%20sys%20module%20first.%20)

---

## [Issue 2](#table-of-contents) - Importing `random_array_list` Function in Unit Test Script

Date: January 25, 2023

### Specific Errors
1. When trying to run the following code in VSCode with Code Runner:
```
import sys
sys.path.append("c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\src")

from ArrayList import ArrayList
from helpers import rand_array_list
```
- I get the following error:
```
ModuleNotFoundError: No module named 'helpers'
```

### Meaning of Errors
2. When running the `dsapy/testing/unit/unit_ArrayList.py` file, the computer is not aware of the `testing` directory that contains the `helpers.py` file.

### True Reason for Errors
- Even though I added `"c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\src"` to Python's filepath so that Python is aware of the `src` folder, Python is still not aware of the `dsapy/testing` directory. Thus, Python is not aware of the `dsapy/testing/helpers.py` file.


### Solution for Errors
- I included the following lines in the `test_unit_ArrayList.py` file to add into Python's list of filepaths a filepath containing the `testing` directory (5):
```
import sys
sys.path.append("c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\src")
sys.path.append("c:\\Users\\Delar\\OneDrive\\Desktop\\Winter Break\\Repos\\DSAPy\\dsapy\\testing")

from ArrayList import ArrayList
from helpers import rand_array_list
```
- Since Python is now aware of the `testing` directory, we can successfully import the `rand_array_list` from the `helpers.py` file into the `test_unit_ArrayList.py` file

---

## [Issue 3](#table-of-contents) - Importing `ArrayList` class when Running PyTest

Date: January 27, 2023

### Specific Errors
1. When trying to run the PyTest unit tests in the `ArrayList_unit_test.py` test script with the terminal command `pytest` in the `dsapy/testing/unit` directory, the following error occured:
```
ImportError while importing test module '/mnt/c/Users/Delar/OneDrive/Desktop/Winter Break/Repos/DSAPy/dsapy/testing/unit/ArrayList_unit_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.8/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ArrayList_unit_test.py:12: in <module>
    from ArrayList import ArrayList
E   ModuleNotFoundError: No module named 'ArrayList'
```

### Meaning of Errors
1. When running the PyTest unit tests in the `ArrayList_unit_test.py` test script, the computer is not aware of the `src` directory that contains the `ArrayList.py` file.

### Unsuccessful Methods
- Method 1
  - Explanation
    - Other people with the same problem have tried adding an empty `__init__.py` file to one of their used directories
  - Specific Approach
    - Add an empty `__init__.py` file to the `testing` directory
  - Result
    - Same error as before
- Method 2
  - Explanation
    - Other people with the same problem have tried adding an empty `__init__.py` file to one of their used directories
  - Specific Approach
    - Add an empty `__init__.py` file to the `src` directory
  - Result
    - Same error as before
- Method 3
  - Explanation
    - Other people with the same problem have tried adding an empty `__init__.py` file to one of their used directories
  - Specific Approach
    - Add an empty `__init__.py` file to both the `testing` and `src` directories
  - Result
    - Same error as before
- Method 4
  - Explanation
    - Other people with the same problem have tried adding an empty `__init__.py` file to one of their used directories
  - Specific Approach
    - Add an empty `__init__.py` file to the `dsapy` directory
  - Result
    - Same error as before
- Method 5
  - Explanation
    - [Other people](https://medium.com/@dirk.avery/pytest-modulenotfounderror-no-module-named-requests-a770e6926ac5) reinstalled PyTest on their virtual environment because they installed PyTest on their system instead of their virtual environment. This meant that they could not properly use PyTest on their virtual environment
  - Specific Approach
    - Run the commands `pip3 uninstall pytest` and `pip3 install pytest` with the command line
  - Result
    - Same error as before
- Method 5
  - Explanation
    - I reinstalled the version of PyTest being used in VSCode with WSL so that it used `python3.9` like my WSL is used and my Python interpreter on VSCode. For some reason PyTest was previously using `python3.8`
  - Specific Approach
    - I ran the commands `python -m pip install pytest` and then `pytest`
  - Result
```
ImportError while importing test module '/mnt/c/Users/Delar/OneDrive/Desktop/Winter Break/Repos/DSAPy/dsapy/testing/unit/ArrayList_unit_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
testing/unit/ArrayList_unit_test.py:13: in <module>
    from ArrayList import ArrayList
E   ModuleNotFoundError: No module named 'ArrayList'    
```

### True Reason for Error
- Even though I could run the `ArrayList_unit_test.py` and `helpers.py` files with VSCode's Code Runner, I could not run them using WSL in the VSCode terminal. The reason for this is because VSCode's Code Runner was using the Python files on my laptop's Windows operating system:
```
c:\Users\Delar\OneDrive\Desktop\Winter Break\Repos\DSAPy\dsapy\testing\unit
C:\Users\Delar\AppData\Local\Programs\Python\Python39\python39.zip
C:\Users\Delar\AppData\Local\Programs\Python\Python39\DLLs
C:\Users\Delar\AppData\Local\Programs\Python\Python39\lib
C:\Users\Delar\AppData\Local\Programs\Python\Python39
C:\Users\Delar\AppData\Local\Programs\Python\Python39\lib\site-packages
```
- However, WSL was using the Python files on its corresponding Linux system:
```
/mnt/c/Users/Delar/OneDrive/Desktop/Winter Break/Repos/DSAPy/dsapy/testing/unit
/usr/lib/python39.zip
/usr/lib/python3.9
/usr/lib/python3.9/lib-dynload
/home/delario-nance-jr/.local/lib/python3.9/site-packages
/usr/local/lib/python3.9/dist-packages
/usr/lib/python3/dist-packages
```
- The following lines in my `ArrayList_unit_test.py` used the filepaths on my laptop's Windows operating system. However, PyTest is ran on WSL (Linux). Therefore, when I used PyTest to try to run my `ArrayList_unit_test.py` Python unit test script, PyTest could not find the Windows filepaths on WSL's Linux operating system.

### Solution for Errors
- I opened a remote window in WSL on VSCode. Then, I cloned the Bitbucket repository for my project in the folder used in this window. By doing this, I am able to use all of my repository's code on a Linux operating system and use the Linux terminal, instead of using my repository's code on my laptop's Windows operating system and using the Linux terminal like before.
- Since I am now using my repository's code to a Linux operating system, I had to change the `sys.path.append` lines in the `ArrayList_unit_test.py` and `helpers.py` files to as follows:
```
In ArrayList_unit_test.py:

WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
WSL_FILEPATH_TO_TESTING = "/home/delario-nance-jr/dsapy/testing" 
sys.path.append(WSL_FILEPATH_TO_TESTING) # helpers


In helpers.py:

# Accessing project directories
WSL_FILEPATH_TO_SRC = "/home/delario-nance-jr/dsapy/src"
sys.path.append(WSL_FILEPATH_TO_SRC) # ArrayList
```

### References
- [Stack Overflow - Pytest ModuleNotFoundError](https://stackoverflow.com/questions/59834619/pytest-modulenotfounderror)
- [Stack Overflow - ModuleNotFoundError with pytest](https://stackoverflow.com/questions/54895002/modulenotfounderror-with-pytest)
- [Medium - pytest: ModuleNotFoundError: No module named 'requests'](https://medium.com/@dirk.avery/pytest-modulenotfounderror-no-module-named-requests-a770e6926ac5)

---

## [Issue 4](#table-of-contents) - Running `test_get_size_of_empty_ArrayList` Unit Test for `ArrayList` Class with PyTest Results in No Tests Being Ran

Date: January 28, 2023

### Specific Errors
1. When try to run the `test_get_size_of_empty_ArrayList` unit test with 
`pytest` in the WSL terminal, no PyTests are ran as shown below:
```
platform linux -- Python 3.9.5, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/delario-nance-jr/dsapy/testing/unit
collected 0 items
```

### True Reason for Error
- The unit test which I wanted to run is as follows:
```
class testGettingSize:
    def test_get_size_of_empty_ArrayList(self):

        empty_arraylist = ArrayList()
        size = len(empty_arraylist)
        assert size == 0
```
- However, PyTest only recognizes classes whose name begins with `Test*`

### Solution for Errors
- Change the name of the `testGettingSize` class to `TestGettingSize` as follows:
```
class TestGettingSize:
    def test_get_size_of_empty_ArrayList(self):

        empty_arraylist = ArrayList()
        size = len(empty_arraylist)
        assert size == 0
```

--- 

# [Integration Testing `ArrayList` Class](#table-of-contents)

---

## [Issue 1](#table-of-contents) - Passing `TestCheckingIfEqual` Integration Tests

### Specific Errors
- After running `pytest testing/integration/` in the WSL terminal with VSCode, the following warnings and errors were shown immediately when trying to determine if two `ArrayList` had the exact same values with the code `assert verdict == False` in the `Array_List_integ_test.py` integration test script
```
=========================================================================================== warnings summary ============================================================================================
testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameValuesButDifferentSizes::test_check_if_ArrayLists_of_same_sixteen_ints_but_different_sizes_are_equal
testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameValuesButDifferentSizes::test_check_if_ArrayLists_of_same_sixteen_ints_but_different_sizes_are_equal
  /.../src/ArrayList.py:87: DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    return self._values == lst_to_compare._values

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================================================================================== short test summary info ========================================================================================
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameSizeAndSameValues::test_check_if_empty_ArrayLists_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameSizeAndSameValues::test_check_if_equal_ArrayLists_of_one_int_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameSizeAndSameValues::test_check_if_equal_ArrayLists_of_sixteen_ints_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameSizeButDifferentValues::test_check_if_ArrayLists_of_one_int_but_different_values_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameSizeButDifferentValues::test_check_if_ArrayLists_of_sixteen_ints_but_different_values_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameSizeButDifferentValues::test_check_if_ArrayLists_of_one_thousand_two_hundred_twenty_nine_ints_but_different_values_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameValuesButDifferentSizes::test_check_if_ArrayLists_of_same_one_int_but_different_sizes_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForSameValuesButDifferentSizes::test_check_if_ArrayLists_of_same_one_thousand_two_hundred_twenty_nine_ints_but_different_sizes_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
FAILED testing/integration/Array_List_integ_test.py::TestCheckingIfEqual::TestCheckingIfEqualForDifferentSizeAndDifferentValues::test_check_if_ArrayLists_of_different_size_and_different_ints_are_equal - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
=============================================================================== 9 failed, 56 passed, 2 warnings in 0.55s ================================================================================
```

### Possible Reasons for Errors
- `ValueError: The trurth value of an array with more than one element is ambiguous` means that either Python or PyTest does not know how to compare `NumPy` arrays with `>1` elements for equality

### True Reason for Error
- If a user wants to compare two NumPy arrays for equality, NumPy forces them to use one of the following examples of NumPy methods:
  - `any`
    - Returns true if any of the values in two NumPy arrays are equal
  - `all`
    - Returns true if all the values in two NumPy arrays of equal shape are equal
  - `array_equal`
    - Returns true if all the values in two NumPy arrays of arbitrary shape are equal

### Solution for Errors
- Instead of using the code `return self._values == lst_to_compare._values` to check if two `ArrayLists` are equal in the `ArrayList` class's `__eq__` method, I now use the following code:
```
def __eq__(self, lst_to_compare: ArrayList) -> bool:
  """Returns true iff this ArrayList contains exactly
  the values in a second user-specified ArrayList to
  compare.

  Args:
      lst_to_compare (ArrayList): The second user-specified 
                                  ArrayList

  Returns:
      bool: True iff this ArrayList and the user-specified
            ArrayLisy contain the same values
  """
  values_in_this_array = self._values[:self._next]
  values_in_other_array = lst_to_compare._values[:lst_to_compare._next]
  return np.array_equal(values_in_this_array, values_in_other_array)
```

### References
- [Data Science Parichay - Check If Two Numpy Arrays are Equal](https://datascienceparichay.com/article/check-if-two-numpy-arrays-are-equal/#:~:text=Summary%20%E2%80%93%20Compare%20two%20Numpy%20arrays%20for%20equality,an%20error%20when%20comparing%20arrays%20of%20different%20lengths.)
- [NumPy - `numpy.array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html)
- [Stack Overflow - ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()](https://stackoverflow.com/questions/10062954/valueerror-the-truth-value-of-an-array-with-more-than-one-element-is-ambiguous)

---

### References
- [Stack Overflow - 'pytest' exits with no error, but with "collected 0 items"](https://stackoverflow.com/questions/37353960/pytest-exits-with-no-error-but-with-collected-0-items)