from random import randint
Valor1 = randint(1, 100)
Valor2 = randint(1, 100)
Valor3 = randint(1, 100)
print(f"{Valor1}, {Valor2}, {Valor3}")
maiorAB = (Valor1 + Valor2 + abs (Valor1 - Valor2) ) / 2
maiorABC = (maiorAB + Valor3 + abs (maiorAB - Valor3) ) / 2
print(f"O maior valor é: {maiorABC:.0f}")