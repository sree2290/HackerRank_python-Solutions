#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    return (" ".join(i.capitalize() for i in s))

if __name__ == '__main__':
