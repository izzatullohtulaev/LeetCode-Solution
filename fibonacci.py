#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 07:23:47 2023

@author: Tulayev Izzat
"""

def fib(n: int) -> int:
    if n==0:
        return 0
    if n==1:
        return 1
    arr = [0, 1]
    for i in list(range(2, n+1)):
        arr.append(arr[i-2]+arr[i-1])
    return arr[-1]