import random


print("********************")
print("BEM VINDO AO JOGO")
print("********************")
print("Fácil (F), Médio (M) ou Difícil (D)")
print("Escolha o seu nível de dificuldade: ")

dif = input().strip().upper  ##Input > Inserir dados// Strip >> desconsiderar espaços >> upper >> converte os caracteres para maiúsculas.

if dif == "F":
    n_tentativa = 12
elif dif == "M":
    n_tentativa = 8
else:
    n_tentativa = 5

   
    nmr_secreto = random.randint(0,99)
    
n_acertou = True
tentativas = 0
pontos = 1000.0


for tentativas in range (1,n_tentativa+1):
    print(f"Tentativa = {tentativas}")
    chute = int(input("Chute um número: "))

    print (f"O número que você chutou é: {chute}")
    acertou = chute == nmr_secreto
    maior = chute > nmr_secreto