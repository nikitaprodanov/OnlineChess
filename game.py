import chess 

from notifications.end_game_notification import end_game
from notifications.start_game_notification import start_game_notification

board = chess.Board()
who_played = 0
draw = 0
draw_requested = 0

def game(input, id):
	global draw_requested
	global draw
	global who_played
	result = ""

	result = game_input(input, board, id)
	if result:
		return result

	if who_played == id:
		return ["Not your turn!!!"]		
	use_input = input.replace('/', '')
	uci_move = to_uci(use_input)
	if uci_move in list_of_moves(board):
		result = move(use_input, board)
		who_played = id

	if end_condition(board, id):	
		result.append(str(end_condition(board, id)))
	
	return result

def end_condition(board, id):
	if board.is_checkmate(): 
		winner_text = "User" + str(id) + " is the winner!!!" + "\n" + "There is a checkmate. Type '/start/' if you want to start another game!"
		end_game()
		return str(winner_text)
	if board.is_stalemate():
		end_game()
		return "There is a stalemate on the board. Party results as a draw. Type '/start/' if you want to start new game!"

def game_input(input, board, id):
	global draw_requested
	global draw
	global who_played

	if input == "/start/": 
		return start_game(board)

	if input == "/moves/":
		return [str(list_of_moves(board))]

	if input == "/board/":
		return print_board(board)
	
	if input == "/draw/" and draw_requested != id:
		draw_requested = id
		return handle_draw()
	elif input == "/draw/" and draw_requested == id:
		return ["You send the offer, you can't accept it!"]

	if input == "/cancel_draw/":
		cancle_draw()
		return ["Draw wasn't accepted"]	

def list_of_moves(board):
	moves = ""
	for move in board.legal_moves:
		moves += (str(move) + " ")

	return moves

def handle_draw():
	global draw
	draw += 1
	if draw == 1:
		return ["Draw offer sent", "Type '/draw/' to accept the offer", "or type '/cancle_draw/' to reject the draw offer"]
	if draw == 2:
		end_game()
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