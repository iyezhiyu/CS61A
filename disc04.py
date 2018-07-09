# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:32:55 2017

@author: ZY
"""

#question 2.3.2
def memory(n):
    def abc(ff):
        nonlocal n
        n=ff(n)
        print(n)
        return abc
    return abc