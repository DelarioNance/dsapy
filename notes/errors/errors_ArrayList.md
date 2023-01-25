# Errors

## Background

### Summary
- A Markdown file containing the errors which arose during the
  creation and testing of the ArrayList class, as well as the 
  methods used to resolve the errors.


### Author
- Delario Nance, Jr. ([email](mailto:denance@davidson.edu))


### Date
- January 25, 2023 - January 25, 2023


### [Table of Contents](#table-of-contents)
- [Errors](#errors)
  - [Background](#background)
    - [Summary](#summary)
    - [Author](#author)
    - [Date](#date)
    - [Table of Contents](#table-of-contents)
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

---

## Issue 1 - Importing `ArrayList` Class in Unit Test Script

### Specific Errors
1. When trying to run `from src.ArrayList import ArrayList` in the `dsapy/testing/unit/unit_ArrayList.py` file, the following error arose:
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

### Specific Errors
1. When trying to run the following code:
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