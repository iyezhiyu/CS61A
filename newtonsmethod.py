# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:00:35 2017

@author: ZY
"""

def improve(update, close, guess=1):
    while not close(guess):
        guess=update(guess)
    return guess

def newton_update(f,df):
    def update(x):
        return x-f(x)/df(x)
    return update

def find_zero(f,df):
    def near_zero(x):
        return approx_eq(f(x),0)
    return improve(newton_update(f,df),near_zero)

def approx_eq(a,b):
    if abs(a-b)<0.0000000001:
        return True
    return False

def square_root_newton(a):
    def f(x):
        return x*x-a
    def df(x):
        return 2*x
    return find_zero(f,df)

ans=square_root_newton(1000)
