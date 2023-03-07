# `ArrayList` Documentation

Author: Delario Nance, Jr.

Date: February 26, 2023 - February 26, 2023

## Introduction
A Markdown file containing the documentation of the `ArrayList` class.

## Table of Contents
- [`ArrayList` Documentation](#arraylist-documentation)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Time and Space Complexities](#time-and-space-complexities)

## Time and Space Complexities
| Type              | Method                              | Time Complexity    | Space Complexity   |
| ----------------- | ----------------------------------- | ------------------ | ------------------ |
| **Magic Methods** | `__init__`                          | $O(n)$             | $O(n)$             |
|                   | `_round_to_next_multiple`           | $O(1)$             | $O(1)$             |
|                   | `_lengthen`                         | $O(n)$             | $O(n)$             |
|                   | `__len__`                           | $O(1)$             | $O(1)$             |
|                   | `__getitem__`                       | $O(1)$             | $O(1)$             |
|                   | `__setitem__`                       | $O(1)$             | $O(1)$             |
|                   | `_get_corresponding_positive_index` | $O(1)$             | $O(1)$             |
|                   | `__str__`                           | ?                  | ?                  |
|                   | `__eq__`                            | $O(n)$             | $O(1)$             |
| **Primary**       | `append`                            | $O(1)$ (amortized) | $O(1)$ (amortized) |
|                   | `remove`                            | $O(n)$             | $O(1)$             |
|                   | `_shift_values_left_to_index`       | $O(n)$             | $O(1)$             |
|                   | `max`                               | $O(n)$             | $O(1)$             |
|                   | `_get_index_of_max`                 | $O(n)$             | $O(1)$             |
|                   | `min`                               | $O(n)$             | $O(1)$             |
|                   | `_get_index_of_min`                 | $O(n)$             | $O(1)$             |
|                   | `copy`                              | $O(n)$             | $O(n)$             |
|                   | `reverse`                           | $O(n)$             | $O(1)$             |
|                   | `_swap`                             | $O(1)$             | $O(1)$             |
| **Sorting**       | `selection_sort`                    | $O(n^2)$           | $O(1)$             |
|                   | `bubblesort`                        | $O(n^2)$           | $O(1)$             |
|                   | `_bubble_max_right`                 | $O(n)$             | $O(1)$             |
|                   | `_bubble_min_right`                 | $O(n)$             | $O(1)$             |
|                   | `insertion_sort`                    | $O(n^2)$           | $O(1)$             |
|                   | `_insert_min_in_left_subarray`      | $O(n)$             | $O(1)$             |
|                   | `_insert_max_in_left_subarray`      | $O(n)$             | $O(1)$             |
|                   | `mergesort`                         | $O(n \log{n})$     | $O(n \log{n})$?    |
|                   | `_mergesort`                        | $O(n \log{n})$     | $O(n \log{n})$?    |
|                   | `_merge`                            | $O(n)$             | $O(n)$             |
| **Booleans**      | `contains`                          |                    |                    |