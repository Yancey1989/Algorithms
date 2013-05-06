#!/usr/bin/env python
#-*- coding:utf8 -*-
def quick_sort(data, l, r):
    if l < r:
         q = partitation(data, l, r)
         quick_sort(data, l, q-1)
         quick_sort(data, q+1, r)

def partitation(data, p, r):
    x = data[r]
    i = p - 1
    j = p
    while j < r:
        if data[j] < x:
            i += 1 
            data[i], data[j] = data[j], data[i]
        j += 1
    data[i+1], data[r] =data[r], data[i+1]
    return i + 1

if __name__ == '__main__':
    data = [9,8,7,6,5,4,3,2,1]
    quick_sort(data, 0, len(data)-1)
    print data
