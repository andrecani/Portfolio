from random import randint
cidades = ["Curitiba", "Londrina", "Araucaria", "Colombo"]
print(cidades)
print(f"Tamanho: {len(cidades)}")
print(f"Cidade 0: {cidades[0]}")
for i in range(0, len(cidades), 1):
    print(f"Cidade '{cidades[i]}' tem {len(cidades[i])} letras")

posicao = randint(0, len(cidades) - 1)
print(posicao)
segredo = cidades[posicao]
print(segredo)
tela = ['_'] * len(segredo)
print(tela)

letra = input("Qual letra: ")
letra = letra[0].upper()
for i in range(len(segredo)): # loop do 0 ao final do segredo
    if letra == segredo[i].upper(): # acertou esta letra
        tela[i] = segredo[i]

print(tela)