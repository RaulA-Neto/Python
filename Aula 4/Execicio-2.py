# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:36:47 2023

@author: Aluno
"""

l = [1,2,3,4,5,6,7,8,9,10]
p = []
l = [x for x in range(10) if x%3==0 and x!=0]
p = l
print(p)