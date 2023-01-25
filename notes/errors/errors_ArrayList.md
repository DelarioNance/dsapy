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
  - [Issue 1 - Using `ArrayList` Source Code in Test Files](#issue-1---using-arraylist-source-code-in-test-files)
    - [Specific Errors](#specific-errors)
    - [Meaning of Errors](#meaning-of-errors)
    - [Possible Reasons for Errors](#possible-reasons-for-errors)
    - [Unsuccessful Methods](#unsuccessful-methods)
    - [Solution for Errors](#solution-for-errors)

---

## Issue 1 - Using `ArrayList` Source Code in Test Files

### Specific Errors
1. When trying to run `from src.ArrayList import ArrayList` in the `dsapy/testing/unit/unit_ArrayList.py` file, the following error arose:
```
ModuleNotFoundError: No module named 'src'
```

### Meaning of Errors
1. When running the `dsapy/testing/unit/unit_ArrayList.py` file, the computer is not aware of the `src` directory that contains the `ArrayList.py` file

### Possible Reasons for Errors
- When running the `unit_ArrayList.py` file, the computer is only aware of files and directories contained with the same directory that `unit_ArrayList.py` is in (i.e., `dsapy/testing/unit`). Since the `src` directory is not in the `dsapy/testing/scripts/unit` directory, the computer is not aware of any module named `src`.

### Unsuccessful Methods
- Method 1
  - Explanation
    - Rather than beginning the file path used for `import` with `src`, start the file path with `dsapy` since it is the lowest directory which contains both the `ArrayList.py` file and the `unit_ArrayList.py` file
  - Specific Approach
    - Run `from dsapy.src.ArrayList import ArrayList` instead of `from src.ArrayList import ArrayList` in the `dsapy/testing/unit/unit_ArrayList.py` file
  - Result
    - Like how no module named `src` could be found, now, no module named `dsapy` could be found
    ```
    ModuleNotFoundError: No module named 'dsapy'
    ```

### Solution for Errors