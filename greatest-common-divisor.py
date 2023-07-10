#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 06:24:21 2023

@author: Tulayev Izzat
"""

def findGCD(nums) -> int:
    if min(nums)==1:
        return 1
    dividors = list(range(1, (min(nums)+1)))
    ans = 0
    for dividor in dividors:
        if min(nums)%dividor==0 and max(nums)%dividor==0:
            ans = dividor
    return ans