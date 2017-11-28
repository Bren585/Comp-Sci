# -*- coding: utf-8 -*-
Chess = [
['BR','BK','BB','BC','BQ','BB','BK','BR'],
['BP','BP','BP','BP','BP','BP','BP','BP'],
['','','','','','','',''],
['','','','','','','',''],
['','','','','','','',''],
['','','','','','','',''],
['WP','WP','WP','WP','WP','WP','WP','WP'],
['WR','WK','WB','WC','WQ','WB','WK','WR']
] 
Alphabet_Refrence = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
English_Refrence = ['rook', 'castle', 'knight', 'horse', 'bishop', 'king', 'queen', 'pawn']
Coded_Refrence = ['R', 'R', 'K', 'K', 'B', 'C', 'Q', 'P']
Unicode_Refrence = [['♜','♜','♞','♞','♝','♚','♛','♟'],['♖','♖','♘','♘', '♗','♔','♕','♙']]

player = 0
turn = 1
victor = 0
global gamemode
gamemode = 0

def printRow(row):
    print row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]

def printBoard():
    run = 0
    process = 0
    board_progress = []
    while run < 8:
        while process < 8: ### note to self: Chess[y][x] works plz use it
            if Chess[run][process] == '':
                board_progress.append('[]')
            else:
                color = Chess[run][process][0]
                if color == 'B':
                    color = 0
                if color == 'W':
                    color = 1
                board_progress.append(Unicode_Refrence[color][Coded_Refrence.index(Chess[run][process][1])])
            process += 1
        printRow(board_progress)
        board_progress = []
        run += 1
        process = 0

testM = False
def moveTest(piece, start, end): #YEEEEEEEET FINISH
    global testM
    start = [int(Alphabet_Refrence.index(start[0])), int(start[1])]
    end = [int(Alphabet_Refrence.index(end[0])), int(end[1])]
    if piece[1] == 'R': #inc
        cool
    elif piece[1] == 'K': #inc
        cool
    elif piece[1] == 'B': #inc
        cool
    elif piece[1] == 'C': #inc
        cool
    elif piece[1] == 'Q': #inc
        cool
    elif piece[1] == 'P': #inc
        if piece[0] == 'W': # if the pawn is White
            if end[1] == start[1] + 1: # P move 1 space
                testP1 = Chess[start[1] + 1]
                if testP1[start[0]] == '':
                    testM = True
            elif end[1] == start[1] + 2 and start[1] == 6: # p uses init 2 space move
                testP1 = Chess[start[1] + 1]
                testP2 = Chess[start[1] + 2]
                if testP1[start[0]] == '' and testP2[start[0]] == '':
                    testM = True
            elif end[1] == start[1] + 1 and start[0] - 1 <= end[0] <= start[0] + 1 and end[0] != start[0]: # pawn takes a piece normally
                testP1 = end[1]
                if testP1[end[0]] != '':
                    testM = True
        elif piece[0] == 'B': #inc
            cool
        else:
            testM = False
    else:
        testM = False

print('----------CHESS----------')
print('   by Brendan Koetting   ')
print('                         ')
print('Type "one player" to play')
print('against a computer.      ')
print('Type "two player" to play')
print('against a friend.        ')
print('Type "about" for         ')
print('information about this   ')
print('program.                 ')
action = raw_input()
if action == 'one player':
    gamemode = 1
elif action == 'two player':
    gamemode = 2
elif action == 'about':
    gamemode = 3
else:
    print 'Not a valid gamemode'

if gamemode == 1:
    print 'In developement'

if gamemode == 2:
    print "Actions should be in this format:"
    print '"Piece CurrentPosition EndPosition"'
    while victor == 0:
        printBoard() 
        print ('Player ' + str(player) + ', turn ' + str(turn))
        action = raw_input('Your move: ')
        if len(action.split()) == 3:
            piece, start, end = action.split()
            piece = Coded_Refrence[English_Refrence.index(piece)]
            if turn % 2 == 1:
                piece = 'W' + piece
            elif turn % 2 == 0:
                piece = 'B' + piece
            moveTest(piece, start, end)
            test1 = Chess[Alphabet_Refrence.index(start[0])] 
            if  test1[int(start[1])-1] == piece: 
                test2 = Chess[Alphabet_Refrence.index(end[0])] #Need to insert move viability checking
                if test2[int(end[1])-1] == '':
                    edit1 = Chess[Alphabet_Refrence.index(start[0])]
                    edit1.remove(piece); edit1.insert(int(start[1])-1,'')
                    Chess.remove(Chess[Alphabet_Refrence.index(start[0])]); Chess.insert(Alphabet_Refrence.index(start[0]),edit1)
                    edit2 = Chess[Alphabet_Refrence.index(end[0])]
                    edit2.remove(''); edit2.insert(int(end[1])-1, piece)
                    Chess.remove(Chess[Alphabet_Refrence.index(end[0])]); Chess.insert(Alphabet_Refrence.index(end[0]),edit2)
                elif Coded_Refrence.count(test2[int(end[1])-1]) >= 1:
                    print 'cool' #piece taking
                else:
                    print 'Not a valid move'
            else:
                print 'Not a valid move'
        else:
            print "Actions should be in this format:"
            print '"Piece CurrentPosition EndPosition"'
        
if gamemode == 3:
    print('----------ABOUT----------')
    print('          V 0.1          ')
    print('                         ')
    print('Written by Brendan       ')
    print('Koetting. Follows        ')
    print('standard tournament rules')
    print('as per chessvariant.com  ')
    print('and relevant articles.   ')#fill in with source
    print('Written in Canopy version')
    print('1.5.5.3123.              ')