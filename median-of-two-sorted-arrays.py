#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:06:06 2023

@author: Tulayev Izzat
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged_list=nums1+nums2
        merged_list.sort()
        if merged_list%2==1:
            return merged_list[len(merged_list)//2]
        mid1 = merged_list[len(merged_list)//2-1]
        mid2 = merged_list[len(merged_list)//2]
        
        return (mid1+mid2)/2
        return 0