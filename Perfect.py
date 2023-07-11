import chess.engine

board = chess.Board()
depth = 20
while True:
    if not board.is_game_over():
        engine = chess.engine.SimpleEngine.popen_uci("D:\Programmierung\Python\Projekte\ChessCheat\stockfish\stockfish-windows-x86-64-avx2.exe")
        result = engine.play(board, chess.engine.Limit(depth=depth))
        print("weiß:", result.move)
        print(board)
        board.push(result.move)
        engine.quit()
        engine = chess.engine.SimpleEngine.popen_uci("D:\Programmierung\Python\Projekte\ChessCheat\stockfish\stockfish-windows-x86-64-avx2.exe")
        result = engine.play(board, chess.engine.Limit(depth=depth))
        print("schwarz:", result.move)
        print(board)
        engine.quit()
    else:
        break
print(f"End of game:\n{board.fen()}")