#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:04:05 2019

@author: rikeshpuri
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def convertToFloat32(rows, cols, matrixString):
    t_list=[]
    np.matrix(matrixString)
    t=matrixString.replace("],[",",")
    t=t.replace("[","")
    t=t.replace("]","")
    a=t.split(",")
    a_int =[int(x) for x in a]
    t_list.append(a_int)
    b=np.array(t_list)
    return np.float32(b.reshape(rows,cols))

#1
def rotateFromCenter(img, val):
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),int(val),1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst


#2
def translatoion(img, val):
    
    rows,cols = img.shape
    M = convertToFloat32(2,3,val)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst
    
#3
def affine(img, val):
    rows,cols = img.shape
    
    matrix = val.split('&')
    pts1 = convertToFloat32(3,2,matrix[0])
    pts2 = convertToFloat32(3,2,matrix[1])
    
    M = cv2.getAffineTransform(pts1,pts2)
    
    dst = cv2.warpAffine(img,M,(cols,rows))
   
    return dst
    
    
#4
def threshBinary(img,val):  
    val = val.split('&')
    ret,dst = cv2.threshold(img,int(val[0]),int(val[1]),cv2.THRESH_BINARY)
    return dst

#5
def threshBinaryInv(img,val): 
    val = val.split('&')
    ret,dst = cv2.threshold(img,int(val[0]),int(val[1]),cv2.THRESH_BINARY_INV)
    return dst

#6
def threshTrunc(img,val): 
    val = val.split('&')
    ret,dst = cv2.threshold(img,int(val[0]),int(val[1]),cv2.THRESH_TRUNC)
    return dst
    
  
#7
def threshTozero(img,val): 
    val = val.split('&')
    ret,dst = cv2.threshold(img,int(val[0]),int(val[1]),cv2.THRESH_TOZERO)
    return dst
    

#8 
def threshTozeroInv(img,val): 
    val = val.split('&')
    ret,dst = cv2.threshold(img,int(val[0]),int(val[1]),cv2.THRESH_TOZERO_INV)
    return dst

    

#9
def adaptiveMean(img,val): 
    
    val = val.split('&')
    maxValue = int(val[0])
    blockSize = int(val[1])
    C = int(val[2])
    img = cv2.medianBlur(img,5)

    dst = cv2.adaptiveThreshold(img,maxValue,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,blockSize,C)
    return dst
    
    
   
#10
def adaptiveGaussian(img,val): 
    
    val = val.split('&')
    maxValue = int(val[0])
    blockSize = int(val[1])
    C = int(val[2])
    img = cv2.medianBlur(img,5)
    
    dst = cv2.adaptiveThreshold(img,maxValue,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,blockSize,C)
    return dst
    
  
    
#11
def threshOtsu(img,val):
    ret2,dst = cv2.threshold(img,0,int(val),cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return dst
    

#12
def averagingBlur(img,val):
    dst = cv2.blur(img,(5,5))
    return dst
    

#13
def gaussianBlur(img,val):
    dst = cv2.GaussianBlur(img,(5,5),0)
    return dst
    
   
#14
def medianBlur(img,val):
    dst = cv2.medianBlur(img,5)
    return dst
    

#15
def bilateriaBlur(img,val):
    dst = cv2.bilateralFilter(img,9,75,75)
    return dst
      
    
#16
def cannyEdge(image, val):
    dst = cv2.Canny(image,100,200)
    return dst