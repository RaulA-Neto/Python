# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:13:19 2023

@author: jtfc6
"""

print("Criptografia de César")
print("Codificação de uma mensagem")
print("")
alfabeto = "abcdefghijklmnopqrstuvwxyz"
chave = " "
while not(chave in alfabeto):
    chave = input("Digite a chave de codificação: ")  # Captura a chave de criptografia
idx = alfabeto.index(chave)     # Posição da chave de criptografia no alfabeto
cifra = ""                      # A sequência de cifragem está inicialmente vazia
while len(cifra)<len(alfabeto): # Enquanto a cifragem não tiver o mesmo tamanho do alfabeto
    cifra += alfabeto[idx]      # Constrói a sequência de cifragem a partir do alfabeto deslocado
    if alfabeto[idx]=='z':      # Se o alfabeto chegou ao "z"
        idx = 0                 # Volta para o índice do "a" para concluir a cifragem
    else:
        idx += 1                # Se ainda não chegou ao final do alfabeto, passa para a próxima letra
mensagem = input("Digite a mensagem a ser codificada: ")
codificada = ""                 # A mensagem codificada está inicialmente vazia
for x in mensagem:              # Para cada elemento da mensagem a ser codificada
    if (x in alfabeto):         # Se o elemento for uma letra do alfabeto
        codificada += cifra[alfabeto.index(x)]   # Insere na mensagem codificada a letra correspondente da cifra
    else:
        codificada += x         # Se o elemento da mensagem não estiver no alfabeto, simplesmente coloca este elemento na mensagem cifrada
print("Mensagem codificada:")
print(codificada)
arquivo = open("msg_codif.txt",'w')
arquivo.write(codificada)
arquivo.close()
print("Mensagem codificada salva no arquivo \'msg_codif.txt\'")
