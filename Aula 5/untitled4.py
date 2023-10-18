# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:43:32 2023

@author: Aluno
"""

texto = input("Digite seu nome: ")
for x in range(len(texto)):
    print(texto[:x+1])
    