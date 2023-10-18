# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:50:54 2023

@author: Raul Neto
"""

# Defina a lista de números inteiros
numeros = [10, 5, 8, 3, 12, 6]

# Número de elementos da lista
num_elementos = len(numeros)

# Maior elemento da lista
maior_elemento = max(numeros)

# Menor elemento da lista
menor_elemento = min(numeros)

# Soma dos elementos da lista
soma_elementos = sum(numeros)

# Valor médio dos elementos da lista
valor_medio = soma_elementos / num_elementos

# Lista ordenada de forma crescente
lista_crescente = sorted(numeros)

# Lista ordenada de forma decrescente
lista_decrescente = sorted(numeros, reverse=True)

# Exibe os resultados
print("Número de elementos:", num_elementos)
print("Maior elemento:", maior_elemento)
print("Menor elemento:", menor_elemento)
print("Soma dos elementos:", soma_elementos)
print("Valor médio dos elementos:", valor_medio)
print("Lista ordenada crescente:", lista_crescente)
print("Lista ordenada decrescente:", lista_decrescente)
