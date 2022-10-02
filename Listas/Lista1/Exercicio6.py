import math

Co = float(input("Digite o cateto oposto: "))
Ca = float(input("Digite o cateto adjacente: "))
Hipo = math.sqrt((Co ** 2) + (Ca ** 2))
print(f"A hipotenusa do triangulo retangulo equivale a: {Hipo:.2f}")