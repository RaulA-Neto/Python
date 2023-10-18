# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:34:22 2023

@author: joaop
"""

numero = int(input("digite um numero inteiro: "))
if (numero%2 == 0):
    print("este numero é divisivel por 2.")
if (numero%3 == 0):
    print("este numero é divisivel por 3.")
if (numero%5 == 0):
    print("este numero é divisivel por 5.")
if ((numero%2 != 0) and (numero%3 != 0) and (numero%5 != 0)):
    print("este numero não é divisivel por 2, 3 e 5.")