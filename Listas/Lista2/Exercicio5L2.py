Inteiro = int(input("Digite um numero inteiro com 3 casas decimais: "))
Resto = Inteiro
Milhares = Inteiro // 1000
Resto -= 1000 * Milhares
Centenas = Inteiro // 100
Resto -= 100 * Centenas
Decimais = Inteiro // 10
Resto -= 10 * Decimais
Unidades = Inteiro // 1
Resto -= 1 * Unidades
print(f"{Milhares} Milhares")
print(f"{Centenas} Centenas")
print(f"{Decimais} Decimais")
print(f"{Unidades} Unidades")
