# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

catalogo = {'Maria':'111-1111',
            'João':'222-2222',
            'Antonio':'333-3333',
            'Sônia':'444-4444'}

for (chave,valor) in catalogo.items():
    print("O telefone de",chave,"é",valor)
print("Meu catálogo possui",len(catalogo),"registros")
print("")
    
# Update item do catálogo
catalogo['Maria'] = '123-4567'

for (chave,valor) in catalogo.items():
    print("O telefone de",chave,"é",valor)
print("Meu catálogo possui",len(catalogo),"registros")
print("")

#Apagar item do catálogo
del catalogo['Maria']

for (chave,valor) in catalogo.items():
    print("O telefone de",chave,"é",valor)
print("Meu catálogo possui",len(catalogo),"registros")
print("")

'''
#Apagar todos os registros
catalogo.clear()

for (chave,valor) in catalogo.items():
    print("O telefone de",chave,"é",valor)
print("Meu catálogo possui",len(catalogo),"registros")
print("")
'''

#Compor dois dicionários
novo = {'Tereza':'555-5555','Joaquim':'666-6666'}
catalogo.update(novo)
for (chave,valor) in catalogo.items():
    print("O telefone de",chave,"é",valor)
print("Meu catálogo possui",len(catalogo),"registros")
print("")

