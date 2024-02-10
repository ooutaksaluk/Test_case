#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    # Write your code here
    def answer(non):
        for i in range(1, len(non)):
            if non[i] == non[i - 1]
    
    full = 0
    stri = set(s)
    for a1 in stri:
        for a2 in stri:
            if a1 != a2:
                ans = ''.join([char for char in s if char == a1 or char == a2])
                if answer(ans):
                    full = max(full, len(ans))
    
    return full

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()