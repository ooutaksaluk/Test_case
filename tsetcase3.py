#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    blank = ''
    for stri in s:
        if stri.isalpha():
            shift = k % 26
            if stri.islower():
                encrypted_char = chr(((ord(stri) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(stri) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = stri
        blank += encrypted_char
    return blank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()