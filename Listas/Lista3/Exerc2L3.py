from datetime import date
AnoNasc = int(input("Qual o ano em que você nasceu: "))
Calculo = date.today().year - AnoNasc
print(Calculo)
if Calculo >= 18:
    print("Você tem idade suficiente para fazer a carteira de motorista")
else:
    print("Você é menor de idade, não pode fazer a carteira de motorista")