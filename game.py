import chess 

board = chess.Board()
who_played = 0
draw = 0
draw_requested = 0

def game(input, id):
	global draw_requested
	global draw
	global who_played
	result = ""
	if input == "/start/":
		result = start_game(board)
		return result

	if input == "/moves/":
		result = list_of_moves(board)
		return result
	
	if input == "/draw/" and draw_requested != id:
		result = handle_draw()
		draw_requested = id
		return result
	elif input == "/draw/" and draw_requested == id:
		return ["You send the offer, you can't accept it!"]

	if input == "/cancel_draw/":
		cancle_draw()
		return ["Draw wasn't accepted"]

	if who_played == id:
		return ["Not your turn!!!"]		
	use_input = input.replace('/', '')
	uci_move = to_uci(use_input)
	if uci_move in list_of_moves(board):
		result = move(use_input, board)
		who_played = id

	if board.is_checkmate():
		result.append("There is a checkmate. Type '/start/' if you want to start another game!")
		winner_text = "User" + str(id) + " is the winner!!!"
		result.append(str(winner_text))
	if board.is_stalemate():
		result.append("There is a stalemate on the board. Party results as a draw. Type '/start/' if you want to start new game!")
	return result

def list_of_moves(board):
	moves = []
	for move in board.legal_moves:
		moves.append(str(move))

	return moves

def handle_draw():
	global draw
	draw += 1
	if draw == 1:
		return ["Draw offer sent", "Type '/draw/' to accept the offer", "or type '/cancle_draw/' to reject the draw offer"]
	if draw == 2:
		return ["Draw was accepted", "Start a new game by typing '/start/'!"]

def cancle_draw():
	draw = 0

def start_game(board):
	global draw_requested
	global draw
	who_played = 0
	draw = 0
	draw_requested = 0
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