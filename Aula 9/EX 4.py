# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:46:17 2023

@author: joaop
"""

lista = []
frase = input('digite uma frase: ')
lista = frase.split()
reverso = ' '
for i in range (-1,-len(lista)-1,-1):
    reverso = reverso + lista[i] + ' '
print(reverso)