# Jogo de Adivinhação (JOGO EM CONSTRUÇÃO)

Bem-vindo ao jogo de adivinhação! Este é um simples jogo em Python onde o jogador tenta adivinhar um número secreto gerado aleatoriamente.

## Descrição

O programa gera um número aleatório entre 0 e 99, e o jogador tem um número limitado de tentativas para adivinhar esse número. O número de tentativas disponíveis é determinado pelo nível de dificuldade escolhido pelo jogador.

## Níveis de Dificuldade

- **Fácil (F)**: 12 tentativas
- **Médio (M)**: 8 tentativas
- **Difícil (D)**: 5 tentativas

## Pontuação

O jogador começa com uma pontuação de 1000 pontos. A cada tentativa, pontos são subtraídos com base na diferença entre o chute do jogador e o número secreto.

## Instruções

1. Execute o programa.
2. Escolha o nível de dificuldade digitando 'F' para Fácil, 'M' para Médio ou 'D' para Difícil.
3. Tente adivinhar o número secreto digitando um número entre 0 e 99.
4. Após cada tentativa, o programa informará se o chute foi maior ou menor que o número secreto.
5. O jogo termina quando o jogador acerta o número secreto ou esgota todas as tentativas.

## Exemplo de Uso

```
********************
BEM VINDO AO JOGO
********************
Escolha o seu nível de dificuldade: 
Fácil (F), Médio (M) ou Difícil (D)
F
Tentativa = 1
Chute um número: 50
o número que vc chutou é: 50
Seu chute foi menor que o número secreto
Tentativa = 2
Chute um número: 75
o número que vc chutou é: 75
Seu chute foi maior que o número secreto
Tentativa = 3
Chute um número: 60
o número que vc chutou é: 60
PARABÉNS, VOCÊ ACERTOU!!
FIM DE JOGO
Você acertou o número secreto em 3 tentativas
Sua pontuação foi de 970.0 pontos.
```
## Requisitos
- Python 3.x
## Como Executar

1. Certifique-se de ter o Python 3.x instalado no seu sistema.
2. Copie o código para um arquivo chamado `jogo_adivinhacao.py`.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo está salvo.
4. Execute o comando: `python jogo_adivinhacao.py`.
