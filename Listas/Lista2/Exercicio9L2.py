Saque = int(input('Valor de saque: '))
tempValue = Saque #Cria uma nova variável para poder modificar o valor do saque
cedulas = [200, 100, 50, 20, 10, 5, 2, 1] #Lista de notas
cedulaIdx = 0 #Index da lista de notas
while(tempValue > cedulas[-1]): #Enquanto o valor temporario for maior que a menor nota da lista
    targetCedula = cedulas[cedulaIdx] #Guarda o valor da nota atual
    nCedulas = tempValue // targetCedula #pega o numero de cedulas
    #tempValue -= (nCedulas * targetCedula) dá pra usar essa forma ao invés do resto da divisao
    tempValue = tempValue % targetCedula #Pega o resto do valor da divisao pela nota
    print(f"{nCedulas} de {targetCedula}R$") #Printa o valor
    cedulaIdx+=1 #Altera a celula alvo