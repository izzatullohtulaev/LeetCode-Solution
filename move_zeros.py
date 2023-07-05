#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:17:19 2023

@author: Tulayev Izzat
"""

def solve(nums):
    zeros = []
    others = []
    for num in nums:
        if num==0:
            zeros.append(num)
        else:
            others.append(num)
    others.sort()
    merged = others+zeros
    return merged