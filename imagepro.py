# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:53:05 2018

@author: STUDENT
"""
import cv2
image=cv2.imread("Taylor-Swift.jpg")
#print(type(image))
#print(image.shape)
#print(image.dtype)
#cv2.imshow("mywindow",image)
#cv2.waitKey(30000)
#cv2.destroyAllWindows()
#print(image.ndim)
#r,g,b=image[100,100]
#print("Blue:{} green:{} red:{}".format(b,g,r))
#r=image[:,:,1]
#print(r.max())
#print(r.shape)
#cv2.imshow("colorimage",image)
#cv2.imshow("redcomponent",r)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
greyimage=cv2.imread(r"Taylor-Swift.jpg",cv2.IMREAD_GRAYSCALE)
print(greyimage.shape)
print(greyimage.ndim)
print(image.ndim)
print(image.shape)
rev=greyimage[::-1,::-1]
divide=greyimage[:,:1200]
cv2.imshow("colorimage",image)
#cv2.imshow("greyimage",greyimage)
#cv2.imshow("dividedimage",divide)
k=cv2.waitKey(0)&0xff
if(k==ord('1')):
    cv2.imshow('Grey Image',greyimage)
    k=cv2.waitKey(0)&0xff
    cv2.destroyAllWindows()
if k==ord('2'):
    cv2.imshow('Reverse IMage',rev)
    k=cv2.waitKey(0)&0xff
    cv2.destroyAllWindows()
if k==ord('3'):
    cv2.imshow1('Cropped Image',divide)
    k=cv2.waitKey(0)&0xff
    cv2.destroyAllWindows()