Dicionario = {
'senhor':'matey',
'hotel':'fleabaginn',
'estudante':'swabbie',
'garoto':'matey',
'madame':'proudbeauty',
'professor':'foulblaggart',
'restaurante':'galley',
'seu':'yer',
'com licença':'arr',
'estudantes':'swabbies',
'são':'be',
'advogado':'foulblaggart',
'o':'th’',
'banheiro':'head',
'meu':'me',
'oi':'avast',
'é':'be',
'homem':'matey'
}
print('Tradutor pirata')
print('')
frase = input('Digite uma frase para ser traduzida para o Piratês: ')
frase = frase.lower()      # passa todos os caracteres para minúsculo
separado = frase.split()   # parte a frase em palavras isoladas
traducao = ''
for x in separado:         # para cada palavra na frase
    tem = 0
    for y in Dicionario.keys():  # para cada entrada (key) no dicionário
        if x == y:               # se a palavra consta no dicionário
            traducao = traducao + Dicionario[x] + ' '   # pega a tradução
            tem = 1              # marca que achou a tradução
    if tem == 0:                 # se não achou a tradução
        traducao = traducao + x + ' '  # coloca a palavra em português mesmo
print('Tradução: ')
print(traducao)
