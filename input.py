def is_position(pos1, pos2):
	letters = "abcdefgh"
	nums = [1, 2, 3, 4, 5, 6, 7, 8]
	if pos1 in letters:
		if pos2 in nums:
			return 1

def input_check(input):
	numeral_positions = [1, 2, 3, 4, 5, 6, 7, 8]
	figures = "KQBNR"
	#is it a simple move(not a pawn)
	if len(input) == 3:
		#is the figure real
		if input[1] in figures:
			#is the position real
			if is_position(input[2], input[3]) == 1:
				move = "Simple"

	#is it a pawn move
	if len(input) == 2:
		if input[1] == e:
			if input[2] in numeral_positions:
				move = "PawnMove" 

					


