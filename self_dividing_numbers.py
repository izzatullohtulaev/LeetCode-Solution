#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 19:02:30 2023

@author: Tulayev Izzat
"""
from typing import List

def selfDividingNumbers(left: int, right: int) -> List[int]:
    if left==right:
        return left
    numbers1 = list(range(left, right+1))
    numbers2 = []
    ans = False
    for number in numbers1:
        if number%10==0:
            continue
        str_of_num = str(number)
        while ans:
            for n in str_of_num:    
                int_of_n = int(float(n))
                if number%int_of_n==0:
                    str_of_num.replace(n, '')
                    ans = True
                else:
                    ans = False
                    break
            if ans==False:
                break
            else:
                numbers2.append(number)
    return numbers2