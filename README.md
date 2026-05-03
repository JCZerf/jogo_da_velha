# PROJETO: Jogo da Velha (Tic-Tac-Toe)

## Cenário
Este projeto propõe a criação de um programa simples que simula uma partida de jogo da velha entre usuário e computador.

Para simplificar o desafio, as regras e comportamentos esperados já estão definidos.

## Regras do Jogo
- O computador joga com `X`.
- O usuário joga com `O`.
- O primeiro movimento é sempre do computador.
- Na primeira jogada, o computador sempre marca o centro do tabuleiro.
- As casas do tabuleiro são numeradas de `1` a `9`, da esquerda para a direita e de cima para baixo.
- O usuário informa a jogada digitando o número da casa desejada.
- A jogada do usuário deve ser válida:
- deve ser um número inteiro;
- deve estar entre `1` e `9`;
- não pode ser uma casa já ocupada.
- Após cada jogada, o programa deve verificar o estado da partida.
- Resultados possíveis:
- o jogo continua;
- empate;
- vitória do usuário;
- vitória do computador.
- O computador responde com uma jogada aleatória em uma casa livre.
- Não é necessário implementar inteligência artificial.

## Estrutura de Dados Obrigatória
O tabuleiro deve ser representado por uma lista com 3 elementos, em que cada elemento também é uma lista com 3 elementos:

```python
board[row][column]
```

Cada posição do tabuleiro pode conter:
- `"O"` para jogada do usuário;
- `"X"` para jogada do computador;
- um dígito (`"1"` a `"9"`) para indicar casa livre.

## Aparência do Tabuleiro
A exibição do tabuleiro no console deve seguir exatamente o formato abaixo:

```text
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

## Funções Esperadas
O projeto deve implementar as seguintes funções:

- `display_board(board)`: mostra o estado atual do tabuleiro.
- `enter_move(board)`: solicita e valida a jogada do usuário, atualizando o tabuleiro.
- `make_list_of_free_fields(board)`: retorna as casas livres como lista de tuplas `(linha, coluna)`.
- `victory_for(board, sign)`: verifica se houve vitória para `O` ou `X`.
- `draw_move(board)`: realiza a jogada do computador em uma casa livre aleatória.

## Geração de Jogada Aleatória
Para escolher a jogada do computador, utilize `randrange()` do módulo `random`.

Exemplo:

```python
from random import randrange
```

## Objetivo Final
Executar a partida completa em loop:
1. Exibir tabuleiro;
2. Receber jogada do usuário;
3. Verificar fim de jogo;
4. Realizar jogada do computador;
5. Verificar fim de jogo novamente;
6. Repetir até vitória ou empate.
