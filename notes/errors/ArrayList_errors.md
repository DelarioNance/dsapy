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

---

# Setting up Unit Test Script

## Issue 1 - Importing `ArrayList` Class in Unit Test Script

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

## Issue 2 - Importing `random_array_list` Function in Unit Test Script

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

## Issue 3 - Importing `ArrayList` class when Running PyTest

Date: January 25, 2023

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