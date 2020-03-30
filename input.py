
def input_check(input):
	numeral_positions = [1, 2, 3, 4, 5, 6, 7, 8]
	letteral_positions = "abcdefgh"
	figures = "KQBNRe"
	#is it a simple move(not a pawn)
	if len(input) == 3:
		#is the figure real
		if input[1] in figures:
			#is the position real
			if input[2] in letteral_positions and input[3] in numeral_positions:
				move = "MoveS"

	#is it a pawn move
	if len(input) == 2:
		if input[1] == e:
			if input[2] in numeral_positions:
				move = "MoveP"

	#is it a complex move(same type of pieces)
	if len(input) == 4:
		#is the figure real
		if input[1] in figures:
			#is the fig position real_letter
			if input[2] in letteral_positions:
				#is the position real
				if input[3] in letteral_positions and input[4] in numeral_positions:
					move = "ComplexMoveL"
			#is the figure real_number
			elif input[2] in numeral_positions:
				#is the position real
				if input[3] in letteral_positions and input[4] in numeral_positions:
					move = "ComplexMoveN"
					#If both figs are placed on the same letter-file,
					#one on d4 and the other one on d2, you write down N4f3 or N2f3,
					#the numbers define where the fig came from.		

	#is it a capture 
	if len(input) == 4:
		#is it pawn or not
		if input[1] in figures:
			#is it an attack move
			if input[2] == 'x':
				if input[3] in letteral_positions and input[4] in numeral_positions:
					move = "Capture"
		elif input[1] in letteral_positions:
			#is it an attack move
			if input[2] == 'x':
				if input[3] == 'e':
					if input[4] in numeral_positions:
						move = "CaptureP"

	#is it a castling
	if input == "0-0":
		move = "CastlingK"

	if input == "0-0-0":
		move = "CastlingQ"

	#is it a check
	if len(input) == 3:
		if input[1] in figures:
			if input[2] in letteral_positions and input[3] in numeral_positions:
				if input[4] == '+':
					move = "Check"
	elif len(input) == 4:
		if input[1] in figures:
			if input[2] in letteral_positions and input[3] in numeral_positions:
				if input[4] == '+' and input[5] == '+':
					move = "CheckD"

	#is it a promotion
	if len(input) == 3:
		if input[1] == 'e':
			if input[2] in numeral_positions:
				if input[3] in figures and input[3] != 'e':
					move = "Promotion"
	return move			

















					


