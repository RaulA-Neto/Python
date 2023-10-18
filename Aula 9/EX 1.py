# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:27:48 2023

@author: joaop
"""

texto = input("digite um texto: ")
texto = texto.replace("a","@")
texto = texto.replace("s","$")
print("texto atualizado: ",texto)