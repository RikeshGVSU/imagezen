#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:29:49 2019

@author: rikeshpuri
"""

'''
 Using all possible combination
'''

import filters
import itertools
import cv2
import sys
import numpy as np
from collections import defaultdict

#print ('Number of arguments:' + str(len(sys.argv)) + 'arguments.')
#print ('Argument List:' +  str(sys.argv[2]))

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def allSunsets(S):
    com = {*()}
    for i in range(len(S)+1):
        newCom = itertools.combinations(S, i)
        for n in newCom:
            com.add(n)
    return com
    
def getTotalImages(d, subs):
    
    total = 0
    for i in subs:
        m = 1
        for x in i:
            m = m * (len(d[x]) if len(d[x]) else 1)
        total = total + m
    return total
    
             
        
def recursive_call_filters(x, each_combination, d, imgName, img):
    imgNameCopy = imgName
    imgCopy = img
    try:
        if not d[each_combination[x]]:
#            print (each_combination[x])
#            print (d[each_combination[x]])
            imgName = imgNameCopy + each_combination[x]
            function=getattr(filters,each_combination[x]) 
            img = function(imgCopy, d[each_combination[x]])
            recursive_call_filters(x+1, each_combination, d, imgName, img)
        for each_list_items in d[each_combination[x]]:
#            print (each_combination[x])
#            print (each_list_items)
            imgName = imgNameCopy + each_combination[x] + each_list_items
            function=getattr(filters,each_combination[x]) 
            img = function(imgCopy, each_list_items)
            recursive_call_filters(x+1, each_combination, d, imgName, img)
    except IndexError:
#        print ('_______________________________')
#        psrint (imgName)
#        print('--------------------------------')
        cv2.imwrite('silverCap2/' + imgName + '.png',img)
    

d = defaultdict(list)
with open("test.txt") as fin:
    for line in fin:
        if ":" in line:
            k, v = line.rstrip().split(":")
            d[k].extend(map(str.strip,v.split("&&"))  if v.strip() else [])
        else:
            d[k].append(line.rstrip())
    # print(d)
    
image = d['image']
num_filters = d['num_filters'][0]   
del d['image']
del d['num_filters']
S = list(d.keys())
if (num_filters == 'all'):
    subs = allSunsets(S)
else:
    subs = findsubsets(S, int(num_filters))
#print(subs)
#print('Total Images: ' + str(getTotalImages(d, subs)))
for eachImage in image:
    print(eachImage)
    for i in subs:
        img = cv2.imread(eachImage,0)
        x = 0
        recursive_call_filters(x, i, d, str(eachImage), img)