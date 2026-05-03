# Projeto: Jogo da Velha

## Descrição
Aplicação em Python que executa uma partida de jogo da velha no terminal entre usuário e computador.

- Computador: `X`
- Usuário: `O`
- Primeira jogada: computador no centro
- Próximas jogadas do computador: aleatórias entre casas livres

## Estrutura do Tabuleiro
O tabuleiro é uma matriz `3x3` (lista com listas), acessada por:

```python
board[row][column]
```

Cada posição contém:
- `"X"`: casa ocupada pelo computador
- `"O"`: casa ocupada pelo usuário
- `1` a `9`: casa livre (numeração da jogada)

## Funcionalidades Implementadas
- Exibição formatada do tabuleiro no console
- Entrada da jogada do usuário
- Validação de jogada (valor digitado e casa disponível)
- Geração de lista de posições livres
- Verificação de vitória para `X` e `O`
- Jogada automática do computador usando `randrange`
- Controle de fim de jogo com mensagens de:
  - vitória do usuário
  - vitória da máquina
  - empate

## Funções do Código
- `display_board(board)`: desenha o tabuleiro.
- `enter_move(board)`: lê e aplica a jogada do usuário.
- `make_list_of_free_fields(board)`: retorna as casas livres como tuplas `(linha, coluna)`.
- `victory_for(board, sign)`: verifica se o jogador (`X` ou `O`) venceu.
- `draw_move(board)`: executa a jogada do computador.

## Como Executar
No diretório do projeto:

```powershell
python main.py
```

## Fluxo do Jogo
1. O tabuleiro é iniciado com números de `1` a `9`.
2. O computador joga `X` no centro.
3. O usuário informa a casa desejada.
4. O programa alterna as jogadas até ocorrer:
   - vitória do usuário;
   - vitória do computador;
   - ou empate.
