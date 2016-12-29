#!/usr/bin/env python
#coding:utf-8
#a = float(raw_input("Please input the score: ... "))
#print isinstance(a, (int, long, float))
while True:
    a = raw_input("Please input the score: ... ")
    try:
      obj = float(a)
    except ValueError, e:
      print "value a input type error:", e
    else:
      if a.replace('.', '', 1).isdigit():  #对象.replace(rgExp,replaceText,max) re.sub(pattern,repl,string,count,flags)  strip()并不是一个真正意义上的替换函数，它是用来删除一些字符的
        score = float(a)
        if score < 60: print "F"
        elif 60 <= score <70: print "D"
        elif 70 <= score <80: print "C" 
        elif 80 <= score <90: print "B"
        elif 90 <= score <=100: print "A"
        else: break
