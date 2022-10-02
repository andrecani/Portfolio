AccEnergPassada = float(input("Qual o valor da conta de energia do mês passado: "))
AccEnergAtual = float(input("Qual o valor da conta de energia do mês atual: "))
Kwh = 0.38
KwhPassada = AccEnergPassada / Kwh
KwhAtual = AccEnergAtual / Kwh
print(f"O valor de Kwh gastados no mês passado foi de {KwhPassada:.2f}")
print(f"O valor de Kwh gastados no mês atual foi de {KwhAtual:.2f}")
