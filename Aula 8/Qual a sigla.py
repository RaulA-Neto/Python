# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:55:54 2023

@author: Raul Neto
"""

import random

# Crie um dicionário relacionando estados brasileiros às suas siglas
estados = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Distrito Federal': 'DF',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}

# Seleciona aleatoriamente um estado
estado_selecionado = random.choice(list(estados.keys()))

# Pergunta ao usuário qual é a sigla deste estado
resposta_usuario = input(f'Qual é a sigla do estado {estado_selecionado}? ')

# Verifica se a resposta do usuário está correta
if resposta_usuario.upper() == estados[estado_selecionado]:
    print('Você acertou!')
else:
    print(f'Você errou. A sigla correta para {estado_selecionado} é {estados[estado_selecionado]}.')
