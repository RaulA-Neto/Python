# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:55:04 2023

@author: Raul Neto
"""

# Dicionário de estados e siglas
dic = {
    'Rio Grande do Sul': 'RS',
    'Santa Catarina': 'SC',
    'Paraná': 'PR',
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Minas Gerais': 'MG',
    'Espírito Santo': 'ES'
}

# Exemplo de acesso às siglas
estado = 'Rio Grande do Sul'
sigla = dic[estado]
print(f'A sigla de {estado} é {sigla}')
