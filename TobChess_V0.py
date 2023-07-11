import random

import chess
#bot = Weiß

def count_piece_values(board, color):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }

    total_value = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == color:
            total_value += piece_values[piece.piece_type]

    return total_value


board = chess.Board()
while True:
    start_white_piece_value = count_piece_values(board, chess.WHITE)
    start_black_piece_value = count_piece_values(board, chess.BLACK)
    start_diff = start_white_piece_value - start_black_piece_value #Umso höher umso besser für weiß
    best_moves = []
    best_diff = 0
    for i in board.legal_moves:
        board.push(i)
        one_white_piece_value = count_piece_values(board, chess.WHITE)
        one_black_piece_value = count_piece_values(board, chess.BLACK)
        one_diff = one_white_piece_value - one_black_piece_value
        if one_diff == best_diff:
            best_moves.append(i)
            best_diff = one_diff
        elif one_diff > best_diff:
            best_moves = []
            best_moves.append(i)
            best_diff = one_diff
        board.pop()
    end_move = random.choice(best_moves)
    print(f"I play {end_move} with a new diff of {best_diff}")
    board.push(end_move)
    print(board)
    player_move = str(input("Enter your move:"))
    try:
        player_move = board.parse_san(player_move)
    except chess.IllegalMoveError:
        print("Invalid move")
    finally:
        board.push(player_move)
        print(board)
