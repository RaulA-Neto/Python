# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 21:55:49 2023

@author: Aluno
"""

agenda = {}
qtdd = int(input("Quantos registros terá a agenda?"))
for x in range (qtdd):
    nome = input("digite o nome da pessoa:")
    tel = input("Digite o telefone da pessoa:")
    agenda[nome] = tel
for (nome,tel) in agenda.items():
    print("O telefone de ",nome,"é",tel)
while True:
    nome = input("digite um nome:")
    if nome in agenda.keys():
         print("O telefone de ",nome,"é",agenda[nome])
    else:
        print("Este nome não está na agenda.")