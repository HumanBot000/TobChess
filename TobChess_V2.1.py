import random
import chess

def count_piece_values(board, color):
    piece_values = {
        chess.PAWN: 100,
        chess.KNIGHT: 300,
        chess.BISHOP: 300,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 0
    }

    total_value = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == color:
            total_value += piece_values[piece.piece_type]

    return total_value

def evaluate_position(board):
    white_piece_value = count_piece_values(board, chess.WHITE)
    black_piece_value = count_piece_values(board, chess.BLACK)
    position_value = white_piece_value - black_piece_value
    return position_value

def get_best_moves(board, color, depth):
    if depth == 0:
        return []

    best_moves = []
    best_diff = -1000000

    for move in board.legal_moves:
        board.push(move)
        opponent_best_moves = get_best_moves(board, not color, depth - 1)
        if opponent_best_moves:
            opponent_move = random.choice(opponent_best_moves)
            board.push(opponent_move)
            diff = evaluate_position(board) - evaluate_position(board) + evaluate_position(board)
            board.pop()
        else:
            diff = evaluate_position(board) - evaluate_position(board)

        if diff == best_diff:
            best_moves.append(move)
        elif diff > best_diff:
            best_moves = [move]
            best_diff = diff

        board.pop()
    return best_moves

board = chess.Board()
max_depth = 3

while True:
    # Zug des Bots (Weiß)
    bot_moves = get_best_moves(board, chess.WHITE, max_depth)
    if bot_moves:
        bot_move = random.choice(bot_moves)
        board.push(bot_move)
        print("Bot plays:", bot_move)
        print(board)
    else:
        print("Bot has no legal moves. Game over.")
        break

    # Zug des menschlichen Spielers (Schwarz)
    player_move = input("Enter your move:")
    player_move = board.parse_san(player_move)
    board.push(player_move)
    print(board)
