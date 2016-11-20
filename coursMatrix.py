# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:06:28 2016

@author: Yan JIN

Simple matrix operation
"""
import numpy as np
from numpy import linalg as LA
a = np.array([[1,-2j],[2j,5]])
print a

w,v = LA.eigh(a)
print w;v

print np.dot(a,v[:,0]) - w[0] * v[:,0]
print np.dot(a,v[:,1]) - w[1] * v[:,1]

A =  np.matrix(a)
print A

w,v = LA.eigh(A)
print w;v

