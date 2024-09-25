saldo = int(input("quanto vai ser guardado?"))
tempo = int (input("por quanto tempo?"))
taxa = 5/100
juros = (saldo*(1+taxa)**tempo-saldo)
montante = saldo+juros
print("seu dinheiro rendeu "+str(juros)+ "reais")
print("saldo atual:  "+str(montante)+ "reais")
