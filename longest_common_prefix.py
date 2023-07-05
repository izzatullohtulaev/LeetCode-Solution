#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 08:12:32 2023

@author: Tulayev Izzat
"""

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        
        pref = strs[0]
        plen = len(pref)
        
        for s in strs[1:]:
            
            while pref != s[0:plen]:
                pref = pref[0:plen-1]
                plen -= 1
        
        return plen