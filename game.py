import chess 

board = chess.Board()
who_played = 0

def game(input, id):
	global who_played
	result = ""
	if input == "/start/":
		result = start_game(board)
		return result

	if input == "/moves/":
		result = list_of_moves(board)
		return result

	if who_played == id:
		return ["Not your turn!!!"]		
	use_input = input.replace('/', '')
	uci_move = to_uci(use_input)
	if uci_move in list_of_moves(board):
		result = move(use_input, board)
		who_played = id

	if board.is_checkmate():
		result.append("There is a checkmate. Type '/start/' if you want to start another game")
	return result

def list_of_moves(board):
	moves = []
	for move in board.legal_moves:
		moves.append(str(move))

	return moves

def start_game(board):
	who_played = 0
	result = ""
	board = chess.Board()
	result = print_board(board)
	return result

def to_uci(input):
	uci_move = board.parse_san(str(input))
	return str(uci_move)

def move(input, board):
 	result = ""
 	board.push_san(str(input))
 	result = print_board(board)
 	return result

def print_board(board):
	string_board = str(board)
	result_board = []
	line = ""
	for p in range(len(string_board)):
		if string_board[p] == '\n':
			result_board.append(line)
			line = ""
			continue
		if string_board[p] == '.':
			line += '¤'
			continue
		line += string_board[p]
	result_board.append(line)
	return result_board