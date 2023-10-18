# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 21:45:22 2023

@author: joaop
"""

b1=float(input("Digite a nota do 1o. bimestre.:"))
b2=float(input("Digite a nota do 2o. bimestre.:"))
media = (b1+b2)/2
if (media >= 7.0):
    print("Aprovado!")
elif (media < 3.5) and (media < 7.0):
        print("Fazer exame!")
else:
    print("Reprovado... :()")