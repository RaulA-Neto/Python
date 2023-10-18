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
    if x in Dicionario.keys():
        traducao = traducao + Dicionario[x] + ' '   # pega a tradução
    else:
        traducao = traducao + x + ' '   # pega a tradução
print('Tradução: ')
print(traducao)
