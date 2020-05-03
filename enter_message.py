def rules_message():
	return ["Positions:",
	"Each square of the chessboard is identified by a unique coordinate pair-a",
	"letter and a number. The vertical columns of squares, called files, are labeled",
	"a through h from White's left (the queenside) to right (the kingside). The",
	"horizontal rows of squares, called ranks, are numbered 1 to 8 starting from",
	"White's side of the board. Thus each square has a unique identification of file",
	"letter followed by rank number. (For example, White's king starts the game on",
	"square e1; Black's knight on b8 can move to open squares a6 or c6.) ",
	"Pieces:",
	"Each piece type (other than pawns) is identified by an uppercase letter.",
	"English-speaking players use the letters K for king, Q for queen, R for rook, B",
	"for bishop, and N for knight (since K is already used). ",
	"Regular(non capture) moves:",
	"Each move of a piece is indicated by the piece's uppercase letter, plus the",
	"coordinate of the destination square. For example, Be5 (move a bishop to e5),",
	"Nf3 (move a knight to f3). For pawn moves, a letter indicating pawn is not",
	"used, only the destination square is given. For example, c5 (move a pawn to",
	"c5).",
	"Captures:",
	"When a piece makes a capture, an x is inserted immediately before the ",
	"destination square. For example, Bxe5 (bishop captures the piece on e5). When a ",
	"pawn makes a capture, the file from which the pawn departed is used to identify ",
	"the pawn.","Castling:","Castling is indicated by the special notations 0-0 (for kingside castling) and",
	"0-0-0 (queenside castling)."]

def news_message():
	return ["Developer update for second milestone:",
	"-Chat based chess with all the functionalities of the original game:",
	"	--moving figures;",
	"	--capturing figures;",
	"	--castling;",
	"	--draws;",
	"-Comprehensive list of information about the text uci(universal chess",
	"interface) and a place to ask questions about the game;",
	"-User experience overhall, you don't need to scroll down tha page every time",
	"you get a new message;",
	"-Private player room where you and your friends can talk and play;",
	"-News room where you can see all the latest updates on the project."]

def lobby_message():
	return ["This is the main room where all online users can chat!",
	"Start with the rules room to get in touch how to play!",
	"Or visit the news room to see what's new!"]