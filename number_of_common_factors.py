#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 18:54:22 2023

@author: Tulayev Izzat
"""

def commonFactors(a: int, b: int) -> int:
    if a==1 or b==1:
        return 1
    array = []
    min1 = min(a, b)
    for i in list(range(1, min1+1)):
        if a%i==0 and b%i==0:
            array.append(i)
    return len(array)