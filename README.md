# Projeto: Jogo da Velha

## Descrição
Aplicação em Python que executa uma partida de jogo da velha no terminal entre usuário e computador.

- Computador: `X`
- Usuário: `O`
- Início da partida: aleatório entre computador e usuário

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
- Limpeza do terminal a cada exibição para mostrar apenas o estado atual
- Entrada da jogada do usuário
- Validação de jogada (inteiro entre `1` e `9` e casa livre)
- Geração de lista de posições livres
- Verificação de vitória para `X` e `O`
- Início aleatório de turno (máquina ou jogador)
- Alternância de turnos entre máquina e jogador
- Controle de fim de jogo com mensagens de vitória da máquina, vitória do usuário ou empate

## Inteligência da Máquina
A jogada da máquina segue uma estratégia simples:

1. Se puder ganhar na jogada atual, joga para vencer.
2. Se o jogador puder ganhar na próxima, bloqueia.
3. Caso contrário, escolhe posição estratégica nesta ordem:
4. Centro.
5. Cantos.
6. Laterais.

## Funções do Código
- `display_board(board)`: limpa o terminal e desenha o tabuleiro.
- `enter_move(board)`: lê e aplica a jogada do usuário.
- `make_list_of_free_fields(board)`: retorna as casas livres como tuplas `(linha, coluna)`.
- `victory_for(board, sign)`: verifica se o jogador (`X` ou `O`) venceu.
- `draw_move(board)`: executa a jogada da máquina com estratégia simples.

## Como Executar
No diretório do projeto:

```powershell
python main.py
```

## Fluxo do Jogo
1. O tabuleiro é iniciado com números de `1` a `9`.
2. O programa sorteia quem começa (`X` ou `O`).
3. A cada turno, o tabuleiro é redesenhado com o estado atualizado.
4. O jogo termina quando há vencedor ou não restam casas livres.
