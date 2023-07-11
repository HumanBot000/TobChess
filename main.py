import chess
import chess.engine

play_as_white = input("Spielst du als weiß?(y/n):")
if play_as_white.lower() == "y": play_as_white = True
else: play_as_white = False
board = chess.Board()
depth = 20

if play_as_white:
    engine = chess.engine.SimpleEngine.popen_uci("D:\Programmierung\Python\Projekte\ChessCheat\stockfish\stockfish-windows-x86-64-avx2.exe")
    result = engine.play(board, chess.engine.Limit(depth=depth))
    print("Bester Zug:", result.move)
    board.push(result.move)
    engine.quit()
while True:
    move =str(input("Zug des gegners:"))
    try:
        move = board.parse_san(move)
    except chess.IllegalMoveError:
        print("Invalid move")
    finally:
        board.push(move)
        engine = chess.engine.SimpleEngine.popen_uci("D:\Programmierung\Python\Projekte\ChessCheat\stockfish\stockfish-windows-x86-64-avx2.exe")
        result = engine.play(board, chess.engine.Limit(depth=depth))
        print("Bester Zug:", result.move)
        board.push(result.move)
        engine.quit()