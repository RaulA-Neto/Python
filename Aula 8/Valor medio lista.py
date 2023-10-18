
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:32:02 2023

@author: Raul Neto
"""

# Solicita ao usuário o número de elementos da lista
num_elementos = int(input("Digite o número de elementos da lista: "))

# Inicializa uma lista vazia para armazenar os elementos
lista = []

# Solicita ao usuário que insira cada elemento da lista
for i in range(num_elementos):
    elemento = float(input(f"Digite o {i+1}º elemento da lista: "))
    lista.append(elemento)

# Calcula o valor médio da lista
if num_elementos > 0:
    valor_medio = sum(lista) / num_elementos
else:
    valor_medio = 0

# Exibe a lista e o valor médio
print("Lista:", lista)
print("Valor médio:", valor_medio)
