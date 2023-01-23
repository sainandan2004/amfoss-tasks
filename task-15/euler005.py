import math
import os
import random
import re
import sys

def LCM(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = (lcm * i) // math.gcd(lcm, i)
    return lcm

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(LCM(n))
