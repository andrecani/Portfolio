import datetime
from datetime import date
DataNasc = int(input("Digite o ano em que nasceu:"))
hoje = datetime.date.today()
Dia = hoje.day
Mes = hoje.month
Ano = hoje.year

Idade = Ano - DataNasc
print(f"Nesse ano de {Ano} você fez/fará {Idade} anos")