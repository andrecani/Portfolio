from math import ceil, pi
qc = int(input("Quantos cilindros vai pintar: "))
a = float(input("Qual a altura em metros do cilindro:"))
r = float(input("Qual o raio em metros do cilindro: "))
ac = pi * pow(r, 2)
ar = 2 * pi * r * a
a1c = 2 * ac + ar
at = qc * a1c
qli = at / 10
qla = ceil(qli / 3.6)
c = qla *  99.98
print("Quantidade de latas: ", qla)
print("Custo total: R$ ", round(c, 2))