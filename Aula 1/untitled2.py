# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:31:48 2023

@author: Aluno
"""

def g_to_r(graus):
    rad = 3.1415*graus/180
    return rad

print('Transformação de graus em radianos')
g = int(input('digite os graus a serem convertidos: '))
r = g_to_r(g)
print('O valor em radianos é: ', r)