import chess 

board = chess.Board()

def game(input):
	string_board = str(board)
	result_board = []
	line = ""
	for p in range(len(string_board)):
		if string_board[p] == '\n':
			result_board.append(line)
			line = ""
			continue
		line += string_board[p]
	result_board.append(line)
	return result_board