ValorInteiro = int(input("Qual o valor desejavel: "))
ParOuImpar = (ValorInteiro % 2)
print(ParOuImpar)
if ParOuImpar == 1:
    print("O número é ímpar")
elif ParOuImpar == 0:
    print("O número é par")