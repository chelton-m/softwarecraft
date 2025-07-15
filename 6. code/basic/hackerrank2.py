"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Python's min() and max() functions use a linear search algorithm to find the minimum or maximum value in an iterable 
(e.g., a list, tuple, etc.). Here's a breakdown of how they work:

Algorithm Details
Time Complexity:

O(n): They iterate through all elements in the input iterable once, making them efficient for unsorted data.

Steps:

Initialize: Assume the first element is the current min/max.

Compare: Iterate through the remaining elements, updating the min/max whenever a smaller/larger value is found.

Return: The final min/max after all elements are checked.

Example Implementation (for min())
python
Copy
def custom_min(iterable):
    if not iterable:
        raise ValueError("iterable is empty")
    current_min = iterable[0]
    for item in iterable[1:]:
        if item < current_min:
            current_min = item
    return current_min
Key Points
Handles Any Iterable: Works for lists, tuples, dictionaries (keys), strings (characters), etc.

Custom Comparisons:

For objects, uses the __lt__ (for <) and _gt__ (for >) methods.

Supports the key parameter (e.g., min(people, key=lambda x: x.age)).

Edge Cases:

Raises ValueError for empty iterables unless a default value is provided (e.g., min([], default=0)).

Optimizations
Built-in Efficiency: Python’s implementation is optimized in C (for CPython), making it faster than a pure-Python loop.

Short-Circuiting:

For generators/iterators, all elements must be evaluated (no early termination).

Example Usage
python
Copy
numbers = [3, 1, 4, 1, 5, 9, 2]
print(min(numbers))  # Output: 1
print(max(numbers))  # Output: 9
When to Use
Unsorted Data: Ideal for one-pass scenarios where sorting would be wasteful (O(n log n)).

Simple Comparisons: For finding extremes without additional context.

If you need repeated min/max queries on dynamic data,
consider using a heap (via heapq), which optimizes these operations to O(1) for min (or O(n) for heap construction).
"""


def timeConversion(s):
    


if __name__ == '__main__':
    s = '12:00:00AM'
    timeConversion(s)
