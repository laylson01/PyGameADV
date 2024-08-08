import random
import time

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

    random.seed(time.time)
    nmr_secreto = random.randit(0,50)
    
n_acertou = True
tentativas = 0
pontos = 1000.0