# -*- coding: utf-8 -*-
"""
Created on Sat Feb 8 2020

@author: huynhant
"""


import random
import string
from unittest import TestCase


def inputChar():
    return chr(random.randint(32,127))

def inputString():
    randomString = chr(random.randint(97, 119))
    for x in range(0, 4):
        randomString += chr(random.randint(97, 119))
    return randomString

def testMe():
    tcCount = 0
    state = 0
    while True:
        tcCount += 1
        c = inputChar()
        s = inputString()
        print("Iteration ", tcCount, ": c = ", c, ", s = ", s, ", state = ", state)

        if c == '[' and state == 0: state = 1
        if c == '(' and state == 1: state = 2
        if c == '{' and state == 2: state = 3
        if c == ' ' and state == 3: state = 4
        if c == 'a' and state == 4: state = 5
        if c == 'x' and state == 5: state = 6
        if c == '}' and state == 6: state = 7
        if c == ')' and state == 7: state = 8
        if c == ']' and state == 8: state = 9

        if state == 9 and s == "reset":
            print("error ")
            exit(200)

testMe()
