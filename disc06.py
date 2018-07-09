# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 19:47:25 2017

@author: ZY
"""

from lab07 import *

#question 1.2.2
def reverse(lnk):
    if lnk.rest is Link.empty or lnk is Link.empty:
        return lnk
    rest_rev=reverse(lnk.rest)
    lnk.rest.rest=lnk
    lnk.rest=Link.empty
    return rest_rev