frase = 'Curso em video Python'

print(frase)

# FATIAMENTO

print(frase[9]) # Mostra o caracter referente a posição definida pelo número.
print(frase[9:13]) # Mostra os caracteres a partir da  posição definida pelo número anterior aos dois pontos até a posição do número após os dois pontos.
print(frase[9:21:2]) # Mostra os caracteres a partir da  posição definida pelo número anterior aos dois pontos até a posição do número após os dois pontos pulando as casas de 2 em 2.
print(frase[:5]) # Mostra os caracteres partindo do primeiro ate a posição referente ao número definido após os dois pontos.
print(frase[15:]) # Mostra os caracteres partindo do  número definido antes dos dois pontos até o final da string.
print(frase[9::3]) # Mostra os caracteres a partir da  posição definida pelo número anterior aos dois pontos até o fim da frase pulando as casas de 3 em 3.

# ANÁLISE

print(len(frase)) # Mostra quantos caracteres a string possui.
print(frase.count('o')) # Mostra quantas letras "o" a string possui.
print(frase.count('o', 0, 13)) # Mostra quantas letras "o" a string possui partindo da primeira casa definida até a segunda.
print(frase.find('deo')) # Mostra em que posição começa esse valor.
print('Curso' in frase) # Mostra se existe o valor na string em forma de True e False.

# TRANSFORMAÇÃO

print(frase.replace('Python', 'Android')) # Substituirá o primeiro valor pelo segundo na string.
print(frase.upper()) # Mostra a string em letras maiúsculas.
print(frase.lower()) # Mostra a sting em letras minúsculas.
print(frase.capitalize()) # Mostra a string com apenas o primeiro caracter em maiúsculo.
print(frase.title()) # Mostra a string com todas as casas pós espaço em maiúscula.

frase = '   Aprenda Pyhton  '

print(frase)
print(frase.strip()) # Mostra a string excluindo espaços inciais e finais.
print(frase.rstrip()) # Mostra a string excluindo espaços finais.
print(frase.lstrip()) # Mostra a string excluindo espaços inciais.

frase = 'Curso em video Python'

print(frase)

# DIVISÃO

print(frase.split()) # Mostra a string dividida pelo espaço criando novas listas.

# JUNÇÃO

print('-'.join(frase)) # Mostra a string com o valor definido entre os caracteres.
