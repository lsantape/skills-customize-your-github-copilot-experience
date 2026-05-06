# Advanced Algorithms in Python

This assignment focuses on implementing and analyzing sorting and searching algorithms.

## Getting Started

Create a Python file (e.g., `algorithms.py`) and implement the required algorithms.

## Required Algorithms

### Sorting
- Quicksort
- Mergesort
- Heapsort (optional: compare with built-in sort)

### Searching
- Binary Search
- Linear Search

## Performance Testing

Use Python's `time` module to measure execution times:

```python
import time

start = time.time()
# your algorithm here
end = time.time()
print(f"Time: {end - start:.6f} seconds")
```

## Test Data

Create test arrays of different sizes:
- Small: 10-100 elements
- Medium: 1000-10000 elements
- Large: 100000+ elements

## Analysis

For each algorithm, document:
- Best case time complexity
- Worst case time complexity
- Average case time complexity
- When to use each algorithm