# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:40:28 2023

@author: joaop
"""

lista = []
for i in range(5):
    palavra = input("digite uma palavra: ")
    lista.append(palavra)
lista.sort()
print("veja as palavras ordenadas: ")
for i in range(5):
    print(lista[i])