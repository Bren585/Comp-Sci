import random
import sys

board = [
['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
]

def PInput(prompt):
    x = raw_input(prompt)
    if x.isdigit():
        x = int(x)
        if x >= 1 and x <= 7:
            return x
        else:
            return False
    else:
        return False
 
### <AI BRAIN>  ##############################################################  
def AInput():
    if type(testPWin()) == int:
        return testPWin()
    else:
        guess = random.raandint(1,7)
        return guess

def testPWinL(r,c):
    testFor = ['[O]', '[X]']
    nc = 0
    PWin = False
    d = False
    if c >= 3:
        for x in testFor:
            true = 0
            for z in range(0,4):
                if board[r][c-z] == x:
                    true += 1
            if true == 3 :
                PWin = True
                for z in range(0,4):
                    if board[r][c-z] != x:
                        nc = (c-z)
                if not board[r-1][nc] == '[ ]' or r == 5:
                    d = True
            if d:
                return [PWin, nc, d]
    else:
        return [PWin, nc, d]

def testPWinDL(r,c):
    testFor = ['[O]', '[X]']
    nc = 0
    PWin = False
    d = False
    if c >= 3 and r <= 2:
        for x in testFor:
            true = 0
            for z in range(0,4):
                if board[r-z][c-z] == x:
                    true += 1
            if true == 3 :
                PWin = True
                for z in range(0,4):
                    if board[r-z][c-z] != x:
                        nc = (c-z)
                        nr = (r-z)
                if not board[nr-1][nc] == '[ ]' or nr == 5:
                    d = True
            if d:
                return [PWin, nc, d]
    else:
        return [PWin, nc, d]

def testPWinDR(r,c):
    testFor = ['[O]', '[X]']
    nc = 0
    PWin = False
    d = False
    if c <= 3 and r <= 2:
        for x in testFor:
            true = 0
            for z in range(0,4):
                if board[r-z][c+z] == x:
                    true += 1
            if true == 3 :
                PWin = True
                for z in range(0,4):
                    if board[r-z][c+z] != x:
                        nc = (c+z)
                        nr = (r-z)
                if not board[nr-1][nc] == '[ ]' or nr == 5:
                    d = True
            if d:
                return [PWin, nc, d]
    else:
        return [PWin, nc, d]

def testPWinD(r,c):
    testFor = ['[O]', '[X]']
    nc = 0
    PWin = False
    d = False
    if r <= 2:
        for x in testFor:
            true = 0
            for z in range(0,4):
                if board[r-z][c] == x:
                    true += 1
            if true == 3:
                PWin = True
                d = True
            if d:
                return [PWin, nc, d]
    else:
        return [PWin, nc, d]

def testPWinSq(r,c):
    if testPWinL(r,c)[2]:
        return testPWinL(r,c)[1]
    elif testPWinDL(r,c)[2]:
        return testPWinDL(r,c)[1]
    elif testPWinD(r,c)[2]:
        return testPWinD(r,c)[1]
    elif testPWinDR(r,c)[2]:
        return testPWinDR(r,c)[1]
    else:
        return False

def testPWin():
    for r in range(0,6):
        for c in range(0,7):
            if type(testPWinSq(r,c)) == int:
                return testPWinSq(r,c)
### </AI BRAIN>  #############################################################
### <SETUP> ##################################################################
def printRow(r):
    r = board[r]
    print r[0], r[1], r[2], r[3], r[4], r[5], r[6]

def printBoard():
    for x in range(6):
        printRow(x) 

def testOpen(r,c):
    if board[r][c] == '[ ]':
        return True
    else:
        return False

def testTopOpen(c):
    test = True
    r = 0
    while test and r <= 5:
        if testOpen(r,c):
            r += 1
        else:
            test = False
    if r == 6:
        return 5
    elif r == 0 and not testOpen(r,c):
        return False
    else:
        return r - 1

### </SETUP> ##################################################################
### <TEST WIN> ################################################################

def testWinLeft(r,c):
    if c >= 3:
        testFor = board[r][c]
        if not testFor == '[ ]':
            run = 1
            test = True
            while test and run < 4:
                if not board[r][c-run] == testFor:
                    test = False
                else:
                    run +=1
            return test
        else:
            return False
    else:
        return False

def testWinDL(r,c):
    if c >= 3 and r <= 2:
        testFor = board[r][c]
        if not testFor == '[ ]':
            run = 1
            test = True
            while test and run < 4:
                if not board[r+run][c-run] == testFor:
                    test = False
                else:
                    run +=1
            return test
        else:
            return False
    else:
        return False
        
def testWinDown(r,c):
    if r <= 2:
        testFor = board[r][c]
        if not testFor == '[ ]':
            run = 1
            test = True
            while test and run < 4:
                if not board[r+run][c] == testFor:
                    test = False
                else:
                    run += 1
            return test
        else:
            return False
    else:
        return False

def testWinDR(r,c):
    if c <= 3 and r <= 2:
        testFor = board[r][c]
        if not testFor == '[ ]':
            run = 1
            test = True
            while test and run < 4:
                if not board[r+run][c+run] == testFor:
                    test = False
                else:
                    run +=1
            return test
        else:
            return False
    else:
        return False

def testWinSq(r,c):
    if testWinLeft(r,c) or testWinDL(r,c) or testWinDown(r,c) or testWinDR(r,c):
        return True
    else:
        return False

def testWin():
    test = False
    for r in range(6):
        for c in range(7):
            if testWinSq(r,c):
                test = True
    return test
    
### </TEST WIN> ###############################################################
### <GAME> ####################################################################

print('--------CONNECT 4--------')
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
    sys.exit()

### <ONE PLAYER> ##############################################################
if gamemode == 1:
    print "In Development. Try again later!"
    play = True
    turn = 0
    player = 1
    print "To place a disc, simply"
    print "type the number row you" 
    print "wish to place it. The rows"
    print "count from left to right,"
    print "starting at 1 and ending"
    print "at 7. "
    while play:
        printBoard()
        print 'Player %d' % (player)
        if player == 1:
            action = PInput('Your move: ')
        if player == 2:
            action = AInput()
        if action == False:
            print "Invalid move. Please try a number between 1 and 7."
        else:
            c = int(action) - 1
            if 0 <= c <= 6:
                if type(testTopOpen(c)) == int:
                    r = testTopOpen(c)
                    if player == 1:
                        board[r][c] = '[O]'
                        player = 2
                    elif player == 2:
                        board[r][c] = '[X]'
                        player = 1
                    if testWin():
                        if player == 1:
                            print "Player 2 Wins!"
                            printBoard()
                            break
                        if player == 2:
                            print "Player 1 Wins!"
                            printBoard()
                            break
                else:
                    print "Invalid move"
            else:
                print "Invalid move"

### </ONE PLAYER> #############################################################
### <TWO PLAYER> ##############################################################

if gamemode == 2:
    play = True
    turn = 0
    player = 1
    print "To place a disc, simply"
    print "type the number row you" 
    print "wish to place it. The rows"
    print "count from left to right,"
    print "starting at 1 and ending"
    print "at 7. "
    while play:
        printBoard()
        print 'Player %d' % (player)
        action = PInput('Your move: ')
        if action == False:
            print "Invalid move. Please try a number between 1 and 7."
        else:
            c = int(action) - 1
            if 0 <= c <= 6:
                if type(testTopOpen(c)) == int:
                    r = testTopOpen(c)
                    if player == 1:
                        board[r][c] = '[O]'
                        player = 2
                    elif player == 2:
                        board[r][c] = '[X]'
                        player = 1
                    if testWin():
                        if player == 1:
                            print "Player 2 Wins!"
                            printBoard()
                            break
                        if player == 2:
                            print "Player 1 Wins!"
                            printBoard()
                            break
                else:
                    print "Invalid move"
            else:
                print "Invalid move"
                
### </TWO PLAYER> #############################################################

if gamemode == 3:
    print('----------ABOUT----------')
    print('          V 0.1          ')
    print('                         ')
    print('Written by Brendan       ')
    print('Koetting. Follows        ')
    print('standard Connect 4 rules.')
    print('Written in Canopy version')
    print('1.5.5.3123.              ')