from random import randrange


jogo_da_velha = [[y * 3 + x + 1 for x in range(3)] for y in range(3)]


def display_board(board):
    # A função aceita um parâmetro contendo o status atual da placa
    # e o imprime no console.
    for i in range(3):
        print('+-------+-------+-------+')
        print('|       |       |       |')
        for j in range(3):
            print(f'|   {board[i][j]}   ', end='')
        print('|')
        print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board):
    # A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada,
    # verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
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
    # A função navega pelo tabuleiro e constrói uma lista de todas as casas livres;
    # a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # A função analisa o estado da placa a fim de verificar se
    # o jogador usando 'O's ou 'X's ganhou o jogo
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
    # A função desenha o movimento do computador e atualiza o tabuleiro.
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

    # 1) Se puder ganhar agora, ganha.
    winning_move = find_winning_move('X')
    if winning_move:
        i, j = winning_move
        board[i][j] = 'X'
        return

    # 2) Se o usuário puder ganhar na próxima, bloqueia.
    blocking_move = find_winning_move('O')
    if blocking_move:
        i, j = blocking_move
        board[i][j] = 'X'
        return

    # 3) Senão, escolhe posição estratégica simples.
    strategic_order = [
        (1, 1),  # centro
        (0, 0), (0, 2), (2, 0), (2, 2),  # cantos
        (0, 1), (1, 0), (1, 2), (2, 1),  # laterais
    ]
    for pos in strategic_order:
        if pos in free_fields:
            i, j = pos
            board[i][j] = 'X'
            return

    # Fallback (não deve acontecer): joga aleatório entre casas livres.
    i, j = free_fields[randrange(len(free_fields))]
    board[i][j] = 'X'


print('*** Jogo da velha ***\n')
jogadas = 0
while jogadas < 9:
    draw_move(board=jogo_da_velha)
    jogadas += 1
    display_board(board=jogo_da_velha)

    if victory_for(board=jogo_da_velha, sign='X'):
        print('*** A máquina ganhou! ***')
        break

    if jogadas == 9:
        print('*** Empate! ***')
        break

    while enter_move(board=jogo_da_velha):
        print('Opção inválida! Escolha uma casa livre de 1 a 9.')

    jogadas += 1
    display_board(board=jogo_da_velha)

    if victory_for(board=jogo_da_velha, sign='O'):
        print('*** Você ganhou! ***')
        break
