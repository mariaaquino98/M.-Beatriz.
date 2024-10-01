valor_saque = int(input("informe o valor do saque"))

notas200 = valor_saque / 200
notas100 = (valor_saque%200) / 100
notas50 = (valor_saque%100) / 50
notas20 = (valor_saque%50) / 20
notas10 = (valor_saque%20) / 10
notas5 = (valor_saque%10) / 5

print("notas de 200: " + str(int(notas200)))
print("notas de 200: " + str(int(notas100)))
print("notas de 200: " + str(int(notas50)))
print("notas de 200: " + str(int(notas20)))
print("notas de 200: " + str(int(notas10)))
print("notas de 200: " + str(int(notas5)))

