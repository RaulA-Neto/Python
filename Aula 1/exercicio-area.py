# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:41:19 2023

@author: Aluno
"""
def a_to_l(alt, larg):
    area = alt*larg
    return area

print('calcule a area de um retangulo')
alt = int(input('digite a altura: '))
larg = int(input('digite a largura: '))
r = a_to_l(alt,larg)
print('O valor da area sera: ', r)
