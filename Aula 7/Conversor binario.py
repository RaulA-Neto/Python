# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

binario = [1,0,1,0,1,1]
b_rev = binario[::-1]
pesos = [2**x for x in range(len(binario))]
decimal = 0
for x in range(len(binario)):
        decimal = decimal + b_rev[x]*pesos[x]
print(decimal)