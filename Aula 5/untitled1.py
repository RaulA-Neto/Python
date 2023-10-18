# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:19:47 2023

@author: Aluno
"""

texto = input('digite o texto: ')
texto = texto.lower()
print('Seu texto possui', len(texto), 'caracteres')
cont = 0
vogais = 'aeiou'
for x in texto:
    if x in vogais:
        cont = cont + 1
print('O Seu possui texto possui', cont,'vogais')
