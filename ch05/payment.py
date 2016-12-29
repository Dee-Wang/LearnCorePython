#!/usr/bin/env python
#coding:utf-8

def Payment():
    more = float(raw_input("Enter opening balance:"))
    one = float(raw_input("Enter monthly payment:"))
    money = float(more-one)
    try:
        return money
    except SyntaxError,e:
       print "SyntaxError"

Payment()
