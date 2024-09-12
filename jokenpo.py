import random

jogada = input("ESCOLHA UMA OPÇÃO PLAYER: [ 0 PEDRA | 1 - PAPEL | 2 - TESOURA]")
cpu = random .randint(0,2)

#player ganha?
if jogada == 0 and cpu == 2:
    print("player venceu!")
if jogada == 1 and cpu == 0:
    print("player venceu!")
if jogada == 2 and cpu == 1:
    print("player venceu!")

#cpu ganhar
if jogada == 0 and cpu == 1:
    print ("cpu venceu!")
if jogada == 1 and cpu == 2:
    print ("cpu venceu!")
if jogada == 2 and cpu == 0:
    print ("cpu venceu!")

#empate
if jogada == 0 and cpu == 0:
    print ("empate!")
if jogada == 1 and cpu == 1:
    print ("empate!")
if jogada == 2 and cpu == 2:
    print ("empate!")
