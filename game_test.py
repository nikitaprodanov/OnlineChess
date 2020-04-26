import chess
import unittest
from game import *


class FlaskTestCase(unittest.TestCase):

	def test_start(self):
		board = chess.Board()
		self.assertEqual(print_board(board), start_game(board))

	def test_moves(self):
		board1 = chess.Board()
		board2 = chess.Board()
		input = "e4"
		board1.push_san(str(input))
		self.assertEqual(print_board(board1), move(input, board2))

	def test_uci1(self):
		board = chess.Board()
		input = "e4"
		self.assertEqual(to_uci(input), "e2e4")

	def test_uci2(self):
		board = chess.Board()
		input = "e3"
		self.assertEqual(to_uci(input), "e2e3")

	def test_main_start(self):
		board = chess.Board()
		result = start_game(board)
		self.assertEqual(game("/start/", 1), result)

	def test_main_moveset(self):
		board = chess.Board()
		result = list_of_moves(board)
		self.assertEqual(game("/moves/", 1), result)

	def test_main_moveset(self):
		board = chess.Board()
		result = ["Draw wasn't accepted"]
		self.assertEqual(game("/cancel_draw/", 1), result)
	
	def test_moves_check(self):
		board = chess.Board()
		moves = []
		for move in board.legal_moves:
			moves.append(str(move))
		self.assertEqual(list_of_moves(board), moves)

	def test_draw(self):
		draw = 2
		result = ['Draw offer sent',
   		"Type '/draw/' to accept the offer",
   		"or type '/cancle_draw/' to reject the draw offer"]
		self.assertEqual(handle_draw(), result)

	def test_print(self):
		board = chess.Board()
		result = ['r n b q k b n r',
		 		  'p p p p p p p p',
		 		  '¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤',
		 		  '¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤',
		 		  '¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤',
		 		  '¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤',
		 		  'P P P P P P P P', 
		 		  'R N B Q K B N R']
		self.assertEqual(print_board(board), result)

		
if __name__ == '_main__':
	unittest.main()		
