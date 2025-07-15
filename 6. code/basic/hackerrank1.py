"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Constraints



Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
"""
def plusMinus(arr):
    # Initialize counters for positive, negative, and zero values
    pos_count = 0
    neg_count = 0
    zero_count = 0

    # Iterate through the array and count the occurrences
    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1

    # Calculate the proportions
    total_count = len(arr)
    pos_ratio = pos_count / total_count
    neg_ratio = neg_count / total_count
    zero_ratio = zero_count / total_count

    # Print the results with six decimal places
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)
def miniMaxSum(arr):
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = [3, 1, 4, 1, 5, 9, 2]
    miniMaxSum(arr)