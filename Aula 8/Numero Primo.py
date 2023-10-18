# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:49:15 2023

@author: Raul Neto
"""

numero = int(input("Digite um número inteiro: "))

if numero > 1:

    for i in range(2, numero // 2 + 1):
       
        if (numero % i) == 0:
            print(numero, "não é um número primo")
            break
    else:
        print(numero, "é um número primo")
else:
    print(numero, "não é um número primo")
