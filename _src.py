import chess


def generate_knight_positions():
    knight_positions = {}

    for square in chess.SQUARES:
        extra_points = 0

        # Berechnen der zusätzlichen Punkte basierend auf der Position des Springers
        file = chess.square_file(square)
        rank = chess.square_rank(square)
        distance_from_center = min(file, 7 - file, rank, 7 - rank)
        extra_points = distance_from_center * 10

        # Hinzufügen des Feldes und der entsprechenden Zusatzpunkte zum Dictionary
        knight_positions[chess.square_name(square)] = extra_points

    return knight_positions


def generate_piece_positions(piece_type):
    piece_positions = {}

    for square in chess.SQUARES:
        extra_points = 0

        # Berechnen der zusätzlichen Punkte basierend auf der Position der Figur
        file = chess.square_file(square)
        rank = chess.square_rank(square)

        if piece_type == chess.PAWN:
            extra_points = rank * 10
        elif piece_type == chess.KNIGHT or piece_type == chess.BISHOP:
            distance_from_center = min(file, 7 - file, rank, 7 - rank)
            extra_points = distance_from_center * 10
        elif piece_type == chess.ROOK:
            extra_points = abs(file - 3.5) * 10 + abs(rank - 3.5) * 10
        elif piece_type == chess.QUEEN:
            extra_points = abs(file - 3.5) * 10 + abs(rank - 3.5) * 10 + min(file, 7 - file, rank, 7 - rank) * 10
        elif piece_type == chess.KING:
            extra_points = abs(file - 3.5) * 10 + abs(rank - 3.5) * 10

        # Hinzufügen des Feldes und der entsprechenden Zusatzpunkte zum Dictionary
        piece_positions[chess.square_name(square)] = extra_points

    return piece_positions


knight_dict = {'a1': 0, 'b1': 0, 'c1': 0, 'd1': 0, 'e1': 0, 'f1': 0, 'g1': 0, 'h1': 0, 'a2': 0, 'b2': 10, 'c2': 10, 'd2': 10, 'e2': 10, 'f2': 10, 'g2': 10, 'h2': 0, 'a3': 0, 'b3': 10, 'c3': 20, 'd3': 20, 'e3': 20, 'f3': 20, 'g3': 10, 'h3': 0, 'a4': 0, 'b4': 10, 'c4': 20, 'd4': 30, 'e4': 30, 'f4': 20, 'g4': 10, 'h4': 0, 'a5': 0, 'b5': 10, 'c5': 20, 'd5': 30, 'e5': 30, 'f5': 20, 'g5': 10, 'h5': 0, 'a6': 0, 'b6': 10, 'c6': 20, 'd6': 20, 'e6': 20, 'f6': 20, 'g6': 10, 'h6': 0, 'a7': 0, 'b7': 10, 'c7': 10, 'd7': 10, 'e7': 10, 'f7': 10, 'g7': 10, 'h7': 0, 'a8': 0, 'b8': 0, 'c8': 0, 'd8': 0, 'e8': 0, 'f8': 0, 'g8': 0, 'h8': 0}
bishop_dict = {'a1': 0, 'b1': 0, 'c1': 0, 'd1': 0, 'e1': 0, 'f1': 0, 'g1': 0, 'h1': 0, 'a2': 0, 'b2': 10, 'c2': 10, 'd2': 10, 'e2': 10, 'f2': 10, 'g2': 10, 'h2': 0, 'a3': 0, 'b3': 10, 'c3': 20, 'd3': 20, 'e3': 20, 'f3': 20, 'g3': 10, 'h3': 0, 'a4': 0, 'b4': 10, 'c4': 20, 'd4': 30, 'e4': 30, 'f4': 20, 'g4': 10, 'h4': 0, 'a5': 0, 'b5': 10, 'c5': 20, 'd5': 30, 'e5': 30, 'f5': 20, 'g5': 10, 'h5': 0, 'a6': 0, 'b6': 10, 'c6': 20, 'd6': 20, 'e6': 20, 'f6': 20, 'g6': 10, 'h6': 0, 'a7': 0, 'b7': 10, 'c7': 10, 'd7': 10, 'e7': 10, 'f7': 10, 'g7': 10, 'h7': 0, 'a8': 0, 'b8': 0, 'c8': 0, 'd8': 0, 'e8': 0, 'f8': 0, 'g8': 0, 'h8': 0}
rook_dict =   {'a1': 70.0, 'b1': 60.0, 'c1': 50.0, 'd1': 40.0, 'e1': 40.0, 'f1': 50.0, 'g1': 60.0, 'h1': 70.0, 'a2': 60.0, 'b2': 50.0, 'c2': 40.0, 'd2': 30.0, 'e2': 30.0, 'f2': 40.0, 'g2': 50.0, 'h2': 60.0, 'a3': 50.0, 'b3': 40.0, 'c3': 30.0, 'd3': 20.0, 'e3': 20.0, 'f3': 30.0, 'g3': 40.0, 'h3': 50.0, 'a4': 40.0, 'b4': 30.0, 'c4': 20.0, 'd4': 10.0, 'e4': 10.0, 'f4': 20.0, 'g4': 30.0, 'h4': 40.0, 'a5': 40.0, 'b5': 30.0, 'c5': 20.0, 'd5': 10.0, 'e5': 10.0, 'f5': 20.0, 'g5': 30.0, 'h5': 40.0, 'a6': 50.0, 'b6': 40.0, 'c6': 30.0, 'd6': 20.0, 'e6': 20.0, 'f6': 30.0, 'g6': 40.0, 'h6': 50.0, 'a7': 60.0, 'b7': 50.0, 'c7': 40.0, 'd7': 30.0, 'e7': 30.0, 'f7': 40.0, 'g7': 50.0, 'h7': 60.0, 'a8': 70.0, 'b8': 60.0, 'c8': 50.0, 'd8': 40.0, 'e8': 40.0, 'f8': 50.0, 'g8': 60.0, 'h8': 70.0}
queen_dict = {'a1': 70.0, 'b1': 60.0, 'c1': 50.0, 'd1': 40.0, 'e1': 40.0, 'f1': 50.0, 'g1': 60.0, 'h1': 70.0, 'a2': 60.0, 'b2': 60.0, 'c2': 50.0, 'd2': 40.0, 'e2': 40.0, 'f2': 50.0, 'g2': 60.0, 'h2': 60.0, 'a3': 50.0, 'b3': 50.0, 'c3': 50.0, 'd3': 40.0, 'e3': 40.0, 'f3': 50.0, 'g3': 50.0, 'h3': 50.0, 'a4': 40.0, 'b4': 40.0, 'c4': 40.0, 'd4': 40.0, 'e4': 40.0, 'f4': 40.0, 'g4': 40.0, 'h4': 40.0, 'a5': 40.0, 'b5': 40.0, 'c5': 40.0, 'd5': 40.0, 'e5': 40.0, 'f5': 40.0, 'g5': 40.0, 'h5': 40.0, 'a6': 50.0, 'b6': 50.0, 'c6': 50.0, 'd6': 40.0, 'e6': 40.0, 'f6': 50.0, 'g6': 50.0, 'h6': 50.0, 'a7': 60.0, 'b7': 60.0, 'c7': 50.0, 'd7': 40.0, 'e7': 40.0, 'f7': 50.0, 'g7': 60.0, 'h7': 60.0, 'a8': 70.0, 'b8': 60.0, 'c8': 50.0, 'd8': 40.0, 'e8': 40.0, 'f8': 50.0, 'g8': 60.0, 'h8': 70.0}
king_dict = {'a1': 70.0, 'b1': 60.0, 'c1': 50.0, 'd1': 40.0, 'e1': 40.0, 'f1': 50.0, 'g1': 60.0, 'h1': 70.0, 'a2': 60.0, 'b2': 50.0, 'c2': 40.0, 'd2': 30.0, 'e2': 30.0, 'f2': 40.0, 'g2': 50.0, 'h2': 60.0, 'a3': 50.0, 'b3': 40.0, 'c3': 30.0, 'd3': 20.0, 'e3': 20.0, 'f3': 30.0, 'g3': 40.0, 'h3': 50.0, 'a4': 40.0, 'b4': 30.0, 'c4': 20.0, 'd4': 10.0, 'e4': 10.0, 'f4': 20.0, 'g4': 30.0, 'h4': 40.0, 'a5': 40.0, 'b5': 30.0, 'c5': 20.0, 'd5': 10.0, 'e5': 10.0, 'f5': 20.0, 'g5': 30.0, 'h5': 40.0, 'a6': 50.0, 'b6': 40.0, 'c6': 30.0, 'd6': 20.0, 'e6': 20.0, 'f6': 30.0, 'g6': 40.0, 'h6': 50.0, 'a7': 60.0, 'b7': 50.0, 'c7': 40.0, 'd7': 30.0, 'e7': 30.0, 'f7': 40.0, 'g7': 50.0, 'h7': 60.0, 'a8': 70.0, 'b8': 60.0, 'c8': 50.0, 'd8': 40.0, 'e8': 40.0, 'f8': 50.0, 'g8': 60.0, 'h8': 70.0}
