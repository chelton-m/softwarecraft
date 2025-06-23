"""
Leetcode link: https://leetcode.com/problems/largest-number/description/
Title: Largest Element in an Array
Difficulty: Easy
Category: Array
Tags: Array, Searching
Problem Statement: Given an array, we have to find the largest element in the array.

Examples:

Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2:
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 

"""


def largest_element(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num
