import random


def jogar():
 print("***********************************")
 print("*Bem vindo ao jogo de adivinhação!*")
 print("***********************************")

 pontos = 1000

 numero_secreto = round(random.randrange(1,101))
 total_de_tentativas = 3

 print("Qual o nível de dificuldade?")
 print("(1) Fácil (2) Médio (3) DIfícil")

 nivel = int(input("Defina o nível:  "))

 if (nivel == 1):
  total_de_tentativas = 20
 elif (nivel == 2):
  total_de_tentativas = 10
 else:
  total_de_tentativas = 5

 for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite seu número entre 1 e 100:")
    print("você digitou: ", chute_str)
    chute = int(chute_str)
    if (chute < 1 or chute > 100):
        print("Você deve digitar o número entre 1 e 100!")
        continue
    acertou = numero_secreto == chute
    maior = chute>numero_secreto
    menor = chute<numero_secreto
    if (acertou):
     print("você acertou e fez {} pontos!".format(pontos))
     break
    else:
     if (maior):
      print("você errou! chute é maior que o numero secreto")
      if (rodada == total_de_tentativas):
        print ("O numero secreto era {}. Você fez {} pontos".format(numero_secreto,pontos))
     elif (menor):
      print("você errou! chute é menor que o numero secreto")
      if (rodada == total_de_tentativas):
        print ("O numero secreto era {}. Você fez {} pontos".format(numero_secreto,pontos))
     pontos_perdidos = abs(numero_secreto - chute) // 3
     pontos = pontos - pontos_perdidos


 print("Fim do jogo")

 print("numero secreto era: ",numero_secreto)

if (__name__ == "__main__"):
 jogar()
