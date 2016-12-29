#!/usr/bin/env python
#coding:utf-8
while True:
    a = raw_input("Please input the year: ... ")
    try:
      obj = int(a)
    except ValueError, e:
      print "value a input type error:", e
    else:
      if a.isdigit():  #对象.replace(rgExp,replaceText,max) re.sub(pattern,repl,string,count,flags)  strip()并不是一个真正意义上的替换函数，它是用来删除一些字符的
        year = int(a)
        if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0): print "%i is a leap year！" %year

def varify(a):
    try:
      obj = int(a)
      return True
    except ValueError, e:
      print "value a input type error:", e
      return False
