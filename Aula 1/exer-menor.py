# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:59:46 2023

@author: Aluno
"""

def numeros(a, b, c):
     t = (a,b,c)
     m = min(t)     
     return m 
                  
print('Obtenha o menor numero')                
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))
meno = numeros(n1,n2,n3)
print('O menor numero é: ', meno)