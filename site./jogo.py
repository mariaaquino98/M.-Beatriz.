import random 

palavras = ["beatriz","harry potter","computador","chocolate"]
palavraEscolhida = random.choice(palavras)
print(" a palavra sorteada tem " + str(len
                                       (palavraEscolhida))+ "letras")
l = input("INFORME UMA LETRA")

erro = len(palavraEscolhida) - 1
erros = 0

while erros < erro :
    for letra in palavraEscolhida:
     if(l == letra):
        print("A letra" + str(l) + "estar na posicao" + str
              (palavraEscolhida.index(l) + 1))
     else:
        erros += 1
                               
                               
print(palavraEscolhida)