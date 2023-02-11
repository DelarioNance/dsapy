# `ArrayList` Test Plan

Author: Delario Nance, Jr.

Date: January 18, 2023 - February 5, 2023

## Introduction
A test plan organizing the `ArrayList` functionalities to setup test, unit test, integration test, and end-to-end test.

## Table of Contents
- [`ArrayList` Test Plan](#arraylist-test-plan)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [**Setup** Tests](#setup-tests)
    - [Creating `ArrayList`](#creating-arraylist)
  - [**Unit** Tests](#unit-tests)
    - [Getting Size](#getting-size)
    - [Printing](#printing)
    - [Checking if Empty](#checking-if-empty)
    - [Getting Value](#getting-value)
      - [Getting Value using Non-Negative Index](#getting-value-using-non-negative-index)
      - [Getting Value using Negative Index](#getting-value-using-negative-index)
    - [Setting Value Without Error](#setting-value-without-error)
    - [Adding Value Without Error](#adding-value-without-error)
    - [Removing Value Without Error](#removing-value-without-error)
  - [**Integration** Tests](#integration-tests)
    - [Setting Value With Correct New Value](#setting-value-with-correct-new-value)
    - [Adding Value With Correct New Size](#adding-value-with-correct-new-size)
    - [Adding Value With Correct New Value](#adding-value-with-correct-new-value)
    - [Removing Value With Correct New Size](#removing-value-with-correct-new-size)
    - [Checking for Equality](#checking-for-equality)
    - [Removing Value With Correct Old Values](#removing-value-with-correct-old-values)
  - [**End-to-End** Tests](#end-to-end-tests)
    - [Finding Minimum](#finding-minimum)
    - [Finding Maximum](#finding-maximum)
    - [Searching](#searching)
    - [Reversing](#reversing)
    - [Selection Sorting](#selection-sorting)
    - [Bubble Sorting](#bubble-sorting)
    - [Insertion Sorting](#insertion-sorting)
    - [Merge Sorting](#merge-sorting)
    - [Quick Sorting](#quick-sorting)

## **Setup** Tests

### [Creating `ArrayList`](#arraylist-test-plan)
1. Create an empty `ArrayList`
2. Create an `ArrayList` of `1` random integer in `[-1000,1000]` 
3. Create an `ArrayList` of `10` random integers in `[-1000,1000]`
4. Create an `ArrayList` of `100` random integers in `[-1000,1000]`
5. Create an `ArrayList` of `10000` random integers in `[-1000,1000]`

---
---

## **Unit** Tests

### [Getting Size](#arraylist-test-plan)

6. Get size of an empty `ArrayList`, without adding elements
7. Get size of `ArrayList` of `1` random integer in `[-1000,1000]`, without adding elements
8. Get size of `ArrayList` of `10` random integers in `[-1000,1000]`, without adding elements
9. Get size of `ArrayList` of `100` random integers in `[-1000,1000]`, without adding elements
10. Get size of `ArrayList` of `10000` random integers in `[-1000,1000]`, without adding elements

---
---

### [Printing](#arraylist-test-plan)

11. Print empty `ArrayList`
12. Print `ArrayList` of first positive integer
13. Print `ArrayList` of first `10` positive integers
14. Print `ArrayList` of first `100` positive integers
15. Print `ArrayList` of first `10000` positive integers

---
---

### [Checking if Empty](#arraylist-test-plan)

16. Check if empty `ArrayList` is empty
17. Check if `ArrayList` of a random integer number of `1729` random integers in `[-1000,1000]` is empty

---
---

### [Getting Value](#arraylist-test-plan)

#### [Getting Value using Non-Negative Index](#arraylist-test-plan)

18. Get value in an `ArrayList` of `1` random integer value in `[-1000,1000]`, using non-negative index

---

19. Get value at start index in an `ArrayList` of `10` random integer values in `[-1000,1000]`, using non-negative index
20. Get value at after-start index in an `ArayList` of `10` random integer values in `[-1000,1000]`, using non-negative index 
21. Get value at middle index in an `ArrayList` of `10` random integer values in `[-1000,1000]`, using non-negative index
22. Get value at before-end index in an `ArayList` of `10` random integer values in `[-1000,1000]`, using non-negative index
23. Get value at end index in an `ArrayList` of `10` random integer values in `[-1000,1000]`, using non-negative index

---

24. Get value at start index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using non-negative index
25. Get value at after-start index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using non-negative index
26. Get value at middle index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using non-negative index
27. Get value at before-end index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using non-negative index
28. Get value at end index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using non-negative index

---

29. Get value at start index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using non-negative index
30. Get value at after-start index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using non-negative index
31. Get value at middle index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using non-negative index
32. Get value at before-end index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using non-negative index
33. Get value at end index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using non-negative index

#### [Getting Value using Negative Index](#arraylist-test-plan)

18. Get value in an `ArrayList` of `1` random integer value in `[-1000,1000]`, using negative index

---

19. Get value at start index in an `ArrayList` of `10` random integer values in `[-1000,1000]`, using negative index
20. Get value at after-start index in an `ArayList` of `10` random integer values in `[-1000,1000]`, using negative index 
21. Get value at middle index in an `ArrayList` of `10` random integer values in `[-1000,1000]`, using negative index
22. Get value at before-end index in an `ArayList` of `10` random integer values in `[-1000,1000]`, using negative index
23. Get value at end index in an `ArrayList` of `10` random integer values in `[-1000,1000]`, using negative index

---

24. Get value at start index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using negative index
25. Get value at after-start index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using negative index
26. Get value at middle index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using negative index
27. Get value at before-end index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using negative index
28. Get value at end index in an `ArrayList` of `100` random integer values in `[-1000,1000]`, using negative index

---

29. Get value at start index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using negative index
30. Get value at after-start index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using negative index
31. Get value at middle index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using negative index
32. Get value at before-end index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using negative index
33. Get value at end index in an `ArrayList` of `10000` random integer values in `[-1000,1000]`, using negative index

---
---

### [Setting Value Without Error](#arraylist-test-plan)

34. Set the value `1729` at the only index in an `ArrayList` with `1` random integer in `[-1000,1000]`, without error
35. Set the value `1729` at the middle index in an `ArrayList` with `10` random integers in `[-1000,1000]`, without error
36. Set the value `1729` at the middle index in an `ArrayList` with `100` random integers in `[-1000,1000]`, without error
37. Set the value `1729` at the middle index in an `ArrayList` with `10000` random integers in `[-1000,1000]`, without error

---
---

### [Adding Value Without Error](#arraylist-test-plan)

38. Add a random integer value in `[-1000,1000]` to an empty `ArrayList`, without error
39. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^1 - 1` random integer in `[-1000,1000]`, without error
40. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^1` random integers in `[-1000,1000]`, without error
41. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^1 + 1` random integers in `[-1000,1000]`, without error
42. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, without error
43. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^4` random integers in `[-1000,1000]`, without error
44. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, without error
45. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, without error
46. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^13` random integers in `[-1000,1000]`, without error
47. Add a random integer value in `[-1000,1000]` to an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, without error

---
---

### [Removing Value Without Error](#arraylist-test-plan)

48. Remove the value from an `ArrayList` of `1` random integer in `[-1000,1000]`, without error
49. Remove the value at start index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, without error
50. Remove the value at after-start index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, without error
51. Remove the value at middle index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, without error
52. Remove the value at before-end index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, without error
53. Remove the value at end index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, without error

---

54. Remove the value at start index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, without error
55. Remove the value at after-start index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, without error
56. Remove the value at middle index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, without error
57. Remove the value at before-end index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, without error
58. Remove the value at end index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, without error

---

59. Remove the value at start index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, without error
60. Remove the value at after-start index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, without error
61. Remove the value at middle index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, without error
62. Remove the value at before-end index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, without error
63. Remove the value at end index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, without error


---

64. Remove the value at start index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, without error
65. Remove the value at after-start index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, without error
66. Remove the value at middle index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, without error
67. Remove the value at before-end index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, without error
68. Remove the value at end index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, without error

---

69. Remove the value at start index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, without error
70. Remove the value at after-start index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, without error
71. Remove the value at middle index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, without error
72. Remove the value at before-end index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, without error
73. Remove the value at end index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, without error

---

74. Remove the value at start index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, without error
75. Remove the value at after-start index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, without error
76. Remove the value at middle index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, without error
77. Remove the value at before-end index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, without error
78. Remove the value at end index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, without error

---
---

## **Integration** Tests

### [Setting Value With Correct New Value](#arraylist-test-plan)

1. Set `1` at the only index in an `ArrayList` with `1` random integer in `[-1000,1000]`, with correct value
2. Set each consecutive integer value in `[1,10]` at each consecutive index in an `ArrayList` with `10` random integers in `[-1000,1000]`, with correct values
3. Set each consecutive integer value in `[1,100]` at each consecutive index in an `ArrayList` with `100` random integers in `[-1000,1000]`, with correct values
4. Set each consecutive integer value in `[1,10000]` at each consecutive index in an `ArrayList` with `10000` random integers in `[-1000,1000]`, with correct values

---
---

### [Adding Value With Correct New Size](#arraylist-test-plan)

5. Add `1729` to an empty `ArrayList`, with correct new size

---

6. Add `1729` to an `ArrayList` of `2^1 - 1` random integer in `[-1000,1000]`, with correct new size
7. Add `1729` to an `ArrayList` of `2^1` random integers in `[-1000,1000]`, with correct new size
8. Add `1729` to an `ArrayList` of `2^1 + 1` random integers in `[-1000,1000]`, with correct new size

---

9. Add `1729` to an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct new size
10. Add `1729` to an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct new size
11. Add `1729` to an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct new size

---

12. Add `1729` to an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct new size
13. Add `1729` to an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct new size
14. Add `1729` to an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct new size

---
---

### [Adding Value With Correct New Value](#arraylist-test-plan)

15. Add `1729` to an empty `ArrayList`, with correct value

---

16. Add `1729` to an `ArrayList` of `2^1 - 1` random integer in `[-1000,1000]`, with correct value
17. Add `1729` to an `ArrayList` of `2^1` random integers in `[-1000,1000]`, with correct value
18. Add `1729` to an `ArrayList` of `2^1 + 1` random integers in `[-1000,1000]`, with correct value

---

19. Add `1729` to an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct value
20. Add `1729` to an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct value
21. Add `1729` to an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct value

---

22. Add `1729` to an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct value
23. Add `1729` to an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct value
24. Add `1729` to an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct value

---
---

### [Removing Value With Correct New Size](#arraylist-test-plan)

25. Remove the value from an `ArrayList` of `1` random integer in `[-1000,1000]`, with correct new size

---

26. Remove the value at start index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct new size
27. Remove the value at after-start index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct new size
28. Remove the value at middle index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct new size
29. Remove the value at before-end index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct new size
30. Remove the value at end index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct new size

---

31. Remove the value at start index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct new size
32. Remove the value at after-start index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct new size
33. Remove the value at middle index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct new size
34. Remove the value at before-end index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct new size
35. Remove the value at end index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct new size

---

36. Remove the value at start index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct new size
37. Remove the value at after-start index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct new size
38. Remove the value at middle index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct new size
39. Remove the value at before-end index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct new size
40. Remove the value at end index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct new size

---

41. Remove the value at start index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct new size
42. Remove the value at after-start index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct new size
43. Remove the value at middle index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct new size
44. Remove the value at before-end index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct new size
45. Remove the value at end index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct new size

---

46. Remove the value at start index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct new size
47. Remove the value at after-start index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct new size
48. Remove the value at middle index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct new size
49. Remove the value at before-end index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct new size
50. Remove the value at end index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct new size

51. Remove the value at start index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct new size
52. Remove the value at after-start index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct new size
53. Remove the value at middle index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct new size
54. Remove the value at before-end index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct new size
55. Remove the value at end index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct new size

---
---

### [Checking for Equality](#arraylist-test-plan)

56. Check if two equal `ArrayLists` of `0` random integers in `[-1000,1000]` are equal
57. Check if two equal `ArrayLists` of `1` random integer in `[-1000,1000]` are equal
58. Check if two equal `ArrayLists` of `16` random integer in `[-1000,1000]` are equal
59. Check if two equal `ArrayLists` of `1729` random integers in `[-1000,1000]` are equal

---

59. Check if two same-size `ArrayLists` of different `1` random integer in `[-1000,1000]` are not equal
60. Check if two same-size `ArrayLists` of different `16` random integers in `[-1000,1000]` are not equal
61. Check if two same-size `ArrayLists` of different `1729` random integers in `[-1000,1000]` are not equal

---

62. Check if two different-size `ArrayLists` of same `1` random integer in `[-1000,1000]` are not equal
63. Check if two different-size `ArrayLists` of same `16` random integers in `[-1000,1000]` are not equal
64. Check if two different-size `ArrayLists` of same `1729` random integers in `[-1000,1000]` are not equal

---

65. Check if two different-size `ArrayLists` of different `1` random integer in `[-1000,1000]` are not equal
66. Check if two different-size `ArrayLists` of different `16` random integers in `[-1000,1000]` are not equal
67. Check if two different-size `ArrayLists` of different `1729` random integers in `[-1000,1000]` are not equal

---
---

### [Removing Value With Correct Old Values](#arraylist-test-plan)

68. Remove the value from an `ArrayList` of `1` random integer in `[-1000,1000]`, with correct old values

---

69. Remove the value at start index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct old values
70. Remove the value at after-start index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct old values
71. Remove the value at middle index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct old values
72. Remove the value at before-end index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct old values
73. Remove the value at end index from an `ArrayList` of `2^4 - 1` random integers in `[-1000,1000]`, with correct old values

---

74. Remove the value at start index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct old values
75. Remove the value at after-start index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct old values
76. Remove the value at middle index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct old values
77. Remove the value at before-end index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct old values
78. Remove the value at end index from an `ArrayList` of `2^4` random integers in `[-1000,1000]`, with correct old values

---

79. Remove the value at start index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct old values
80. Remove the value at after-start index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct old values
81. Remove the value at middle index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct old values
82. Remove the value at before-end index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct old values
83. Remove the value at end index from an `ArrayList` of `2^4 + 1` random integers in `[-1000,1000]`, with correct old values

---

84. Remove the value at start index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct old values
85. Remove the value at after-start index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct old values
86. Remove the value at middle index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct old values
87. Remove the value at before-end index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct old values
88. Remove the value at end index from an `ArrayList` of `2^13 - 1` random integers in `[-1000,1000]`, with correct old values

---

89. Remove the value at start index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct old values
90. Remove the value at after-start index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct old values
91. Remove the value at middle index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct old values
92. Remove the value at before-end index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct old values
93. Remove the value at end index from an `ArrayList` of `2^13` random integers in `[-1000,1000]`, with correct old values

---

94. Remove the value at start index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct old values
95. Remove the value at after-start index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct old values
96. Remove the value at middle index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct old values
97. Remove the value at before-end index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct old values
98. Remove the value at end index from an `ArrayList` of `2^13 + 1` random integers in `[-1000,1000]`, with correct old values

---
---

## **End-to-End** Tests

### [Finding Minimum](#arraylist-test-plan)

1. Find minimum of `ArrayList` of `1` random integer in `[-1000,1000]`
2. Find minimum of `ArrayList` of `10` random integers in `[-1000,1000]`
3. Find minimum of `ArrayList` of `100` random integers in `[-1000,1000]`
4. Find minimum of `ArrayList` of `10000` random integers in `[-1000,1000]`

---
---

### [Finding Maximum](#arraylist-test-plan)

5. Find maximum of `ArrayList` of `1` random integer in `[-1000,1000]`
6. Find maximum of `ArrayList` of `10` random integers in `[-1000,1000]`
7. Find maximum of `ArrayList` of `100` random integers in `[-1000,1000]`
8. Find maximum of `ArrayList` of `10000` random integers in `[-1000,1000]`

---
---

### [Searching](#arraylist-test-plan)

9. Search for value `0` in empty `ArrayList`
10. Search for value `500` in `ArrayList` of `1` random integer number in `[1,1000]`
11. Search for value `500` in `ArrayList` of `10` random integer number in `[1,1000]`
12. Search for value `500` in `ArrayList` of `100` random integer number in `[1,1000]`
13. Search for value `500` in `ArrayList` of `10000` random integer number in `[1,1000]`

---
---

### [Reversing](#arraylist-test-plan)

14. Reverse `ArrayList` of `1` random integer in `[-1000,1000]`
15. Reverse `ArrayList` of `10` random integer in `[-1000,1000]`
16. Reverse `ArrayList` of `100` random integer in `[-1000,1000]`
17. Reverse `ArrayList` of `10000` random integer in `[-1000,1000]`

---
---

### [Selection Sorting](#arraylist-test-plan)

18. Selection sort `ArrayList` of `1` random integer in `[-1000,1000]`
19. Selection sort `ArrayList` of `10` random integer in `[-1000,1000]`
20. Selection sort `ArrayList` of `100` random integer in `[-1000,1000]`
21. Selection sort `ArrayList` of `10000` random integer in `[-1000,1000]`

---
---

### [Bubble Sorting](#arraylist-test-plan)

22. Bubble sort `ArrayList` of `1` random integer in `[-1000,1000]`
23. Bubble sort `ArrayList` of `10` random integer in `[-1000,1000]`
24. Bubble sort `ArrayList` of `100` random integer in `[-1000,1000]`
25. Bubble sort `ArrayList` of `10000` random integer in `[-1000,1000]`

---
---

### [Insertion Sorting](#arraylist-test-plan)

26. Insertion sort `ArrayList` of `1` random integer in `[-1000,1000]`
27. Insertion sort `ArrayList` of `10` random integer in `[-1000,1000]`
28. Insertion sort `ArrayList` of `100` random integer in `[-1000,1000]`
29. Insertion sort `ArrayList` of `10000` random integer in `[-1000,1000]`

---
---

### [Merge Sorting](#arraylist-test-plan)

30. Merge sort `ArrayList` of `1` random integer in `[-1000,1000]`
31. Merge sort `ArrayList` of `10` random integer in `[-1000,1000]`
32. Merge sort `ArrayList` of `100` random integer in `[-1000,1000]`
33. Merge sort `ArrayList` of `10000` random integer in `[-1000,1000]`

---
---

### [Quick Sorting](#arraylist-test-plan)

34. Quick sort `ArrayList` of `1` random integer in `[-1000,1000]`
35. Quick sort `ArrayList` of `10` random integer in `[-1000,1000]`
36. Quick sort `ArrayList` of `100` random integer in `[-1000,1000]`
37. Quick sort `ArrayList` of `10000` random integer in `[-1000,1000]`










