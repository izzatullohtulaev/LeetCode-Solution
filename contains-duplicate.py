#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:52:22 2023

@author: Tulayev Izzat
"""

def containsDuplicate(self, nums):
    for num in nums:
        if num in nums[nums.index(num):]:
            return True
    return False 