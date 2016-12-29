#/usr/bin/env python
#coding:utf-8
def timetrans(time):
    tl = time.split(':')
    try:
        hour = float(tl[0])
        minute = float(tl[1])
    except ValueError, e:
        print "您输入的时间格式有误，请重新运行程序，重新正确输入。"
        exit()
    except IndexError, e:
        print "您输入的时间格式有误，请重新运行程序，重新正确输入。"
        exit()
    if hour < 0 or hour > 23:
        print "小时数不能小于0或者超过23，请重新运行程序，重新正确输入。"
        exit()
    if minute < 0 or minute > 59:
        print "分钟数不能小于0或者超过59，请重新运行程序，重新正确输入。"
        exit()
    print "转换成分钟后为：%d 分钟" %(hour*60+minute)

time=raw_input("请输入时间（例如23：45）：")
timetrans(time)
