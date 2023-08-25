import chess
import random
import _src

white = True

def return_infinity():
    return 100000000000
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
    if color == chess.WHITE and board.result() == "1-0":
        total_value = return_infinity()
    elif color == chess.BLACK and board.result() == "0-1":
        total_value = -return_infinity()
    else:
        for square in chess.SQUARES:
            squared_name = chess.square_name(square)
            rank = chess.square_rank(square)
            file = chess.square_file(square)
            piece = board.piece_at(square)
            if piece is not None and piece.color == color:
                piece_value = piece_values[piece.piece_type]
                if piece.piece_type == chess.PAWN:
                    if color == chess.WHITE:
                        piece_value += rank * 10
                    else:
                        piece_value += (7 - rank) * 10
                elif piece.piece_type == chess.KNIGHT:
                    if color == chess.WHITE:
                        piece_value = piece_value + int(_src.knight_dict[squared_name])
                    else:
                        piece_value = piece_value - int(_src.knight_dict[squared_name])
                elif piece.piece_type == chess.BISHOP:
                    if color == chess.WHITE:
                        piece_value = piece_value + int(_src.bishop_dict[squared_name])
                    else:
                        piece_value = piece_value - int(_src.bishop_dict[squared_name])
                elif piece.piece_type == chess.ROOK:
                    if color == chess.WHITE:
                        piece_value = piece_value + int(_src.rook_dict[squared_name])
                    else:
                        piece_value = piece_value - int(_src.rook_dict[squared_name])
                elif piece.piece_type == chess.QUEEN:
                    if color == chess.WHITE:
                        piece_value = piece_value + int(_src.queen_dict[squared_name])
                    else:
                        piece_value = piece_value - int(_src.queen_dict[squared_name])
                elif piece.piece_type == chess.KING:
                    if color == chess.WHITE:
                        piece_value = piece_value + int(_src.king_dict[squared_name])
                    else:
                        piece_value = piece_value - int(_src.king_dict[squared_name])

                total_value += piece_value

    return total_value

def evaluate_position(board):
    white_piece_value = count_piece_values(board, chess.WHITE)
    black_piece_value = count_piece_values(board, chess.BLACK)
    position_value = white_piece_value - black_piece_value
    return position_value if white else -position_value

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_moves(board, depth):
    global white
    best_moves = []
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    white = board.turn == chess.WHITE

    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval > best_eval:
            best_eval = eval
            best_moves = [move]
        elif eval == best_eval:
            best_moves.append(move)

    return best_moves


if __name__ == "__main__":
    board = chess.Board()
    max_depth = 3

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            bot_moves = get_best_moves(board, max_depth)
            if bot_moves:
                bot_move = random.choice(bot_moves)
                board.push(bot_move)
                print("Bot plays:", bot_move)
                print(board)
            else:
                print("Bot has no legal moves. Game over.")
                break
        else:
            while True:
                player_move = input("Enter your move:")
                try:
                    player_move = board.parse_san(player_move)
                    board.push(player_move)
                    print(board)
                finally:
                    break

    print("Game over. Result:", board.result())
