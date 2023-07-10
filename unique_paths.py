#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:10:28 2023

@author: Tulayev Izzat
"""

def uniquePaths(m: int, n: int) -> int:
    if m>n:
        return m*(n-1)
    return n*(m+1)
    return 0