import datetime
from datetime import date
Usu = float(input("Que horas são: "))
agora = datetime.datetime.now()
minutos_totais = agora.hour * 60 + agora.minute
segundos_totais = minutos_totais * 60 + agora.second
print(f"Agora é {agora}")
print(f"Já sepassaram {minutos_totais} min.")
print(f"Já sepassaram {segundos_totais} seg.")

