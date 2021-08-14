#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#
def gen_prefix_modular(N, nums, MOD):
    output = [nums[0] % MOD]
    for i in range (1, N):
        output.append((output[i - 1] + nums[i] % MOD) % MOD)
    return output

def smallest_greater_left(N, nums):
    output, stack, sorted_list = [-1] * N, [], []
    for i, a in enumerate(nums):
        sorted_list.append((a, i))
    sorted_list.sort()
    for _, i in sorted_list:
        while stack and stack[-1] >= i:
            output[stack.pop()] = i
        stack.append(i)
    return output

def maximumSum(N, nums, MOD):
    # Write your code here
    output = 0
    prefix_modular = gen_prefix_modular(N, nums, MOD)
    upper_bound_left = smallest_greater_left(N, prefix_modular)
    for i in range (N):
        output = max(output, prefix_modular[i])
        if upper_bound_left[i] != -1:
            output = max(output, prefix_modular[i] - prefix_modular[upper_bound_left[i]] + MOD)
    return output
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        N = int(first_multiple_input[0])

        MOD = int(first_multiple_input[1])

        nums = list(map(int, input().rstrip().split()))

        result = maximumSum(N, nums, MOD)

        fptr.write(str(result) + '\n')

    fptr.close()
