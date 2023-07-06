#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:37:59 2023

@author: Tulayev Izzat
"""

def singleNumber(nums) -> int:
    for num in nums:
        if num not in nums[nums.index(num)+1:]:
            return num
    return 0