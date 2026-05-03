from random import randrange
import os


jogo_da_velha = [[y * 3 + x + 1 for x in range(3)] for y in range(3)]


def display_board(board):
    # Limpa o terminal para exibir apenas o estado atual do jogo.
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(3):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        for j in range(3):
            print(f'|   {board[i][j]}   ', end='')
        print('|')
        print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    freer_fields = make_list_of_free_fields(board)
    try:
        move = int(input('Qual casa deseja selecionar (1-9): '))
        if move < 1 or move > 9:
            return True

        for i in range(3):
            for j in range(3):
                if move == board[i][j]:
                    opcao = (i, j)
                    if opcao in freer_fields:
                        board[i][j] = 'O'
                        return False
    except ValueError:
        return True

    return True


def make_list_of_free_fields(board):
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    combinacoes = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    contador = 0
    for i in range(len(combinacoes)):
        for j in range(3):
            a, b = combinacoes[i][j]
            if board[a][b] == sign:
                contador += 1
        if contador == 3:
            return True
        contador = 0

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)

    if len(free_fields) == 9:
        board[1][1] = 'X'
        return

    def find_winning_move(sign):
        for i, j in free_fields:
            original = board[i][j]
            board[i][j] = sign
            if victory_for(board, sign):
                board[i][j] = original
                return (i, j)
            board[i][j] = original
        return None

    winning_move = find_winning_move('X')
    if winning_move:
        i, j = winning_move
        board[i][j] = 'X'
        return

    blocking_move = find_winning_move('O')
    if blocking_move:
        i, j = blocking_move
        board[i][j] = 'X'
        return

    strategic_order = [
        (1, 1),
        (0, 0), (0, 2), (2, 0), (2, 2),
        (0, 1), (1, 0), (1, 2), (2, 1),
    ]
    for pos in strategic_order:
        if pos in free_fields:
            i, j = pos
            board[i][j] = 'X'
            return

    i, j = free_fields[randrange(len(free_fields))]
    board[i][j] = 'X'


print('*** Jogo da velha ***\n')
turno_atual = 'X' if randrange(2) == 0 else 'O'
quem_comeca = 'máquina (X)' if turno_atual == 'X' else 'jogador (O)'
print(f'Quem começa: {quem_comeca}\n')

while True:
    if turno_atual == 'X':
        draw_move(board=jogo_da_velha)
        display_board(board=jogo_da_velha)
        if victory_for(board=jogo_da_velha, sign='X'):
            print('*** A máquina ganhou! ***')
            break
    else:
        display_board(board=jogo_da_velha)
        while enter_move(board=jogo_da_velha):
            print('Opção inválida! Escolha uma casa livre de 1 a 9.')
        display_board(board=jogo_da_velha)
        if victory_for(board=jogo_da_velha, sign='O'):
            print('*** Você ganhou! ***')
            break

    if not make_list_of_free_fields(jogo_da_velha):
        print('*** Empate! ***')
        break

    turno_atual = 'O' if turno_atual == 'X' else 'X'
