import random
import sys

player1 = [
[raw_input('Who is Player 1? Name: ')],
['HP:  ','[O]','[O]','[O]','[O]'],
['AMMO:','[ ]','[ ]','[ ]','[ ]','[ ]'],
['SHLD:','[O]','[O]','[O]']
]

player2 = [
[raw_input('Who is Player 2? Name: ')],
['HP:  ','[O]','[O]','[O]','[O]'],
['AMMO:','[ ]','[ ]','[ ]','[ ]','[ ]'],
['SHLD:','[O]','[O]','[O]']
]

victory = False
l = ['shoot', 'reload', 'shield']

rLookup = [
['N N','D 1','N N'],
['D 0','R 2','R 0'],
['N N','R 1','N N']
]

rTrans = [], 'D', 'R', []
pTrans = [player1], [player2], [player1, player2]

def result(A,B):
    r = rLookup[l.index(A)][l.index(B)]
    if r != 'N N':
        a,p = r.split()
        a = rTrans.index(a)
        p = pTrans[int(p)]
        if a == 1:
            decr(a,p)
        elif a == 2:
            incr(a,p)

def printRow(lst):
    if type(lst) == list:
        pr = ''
        for x in range(0, len(lst)):
            pr += str(lst[x])
        print pr 

def printDisplay():
    for x in range(0,4):
        printRow(player1[x])
    print ''
    for x in range(0,4):
        printRow(player2[x])

def testEmpty(i,lst):
    test = lst[i]
    r = test.index(test[-1],-1)
    run = 0
    while run < len(test) - 1:
        if test[r - run] == '[ ]':
            run += 1
        else:
            return run
    if run == len(test) - 1:
        return False

def decr(i,lst):
    x = testEmpty(i,lst)
    if type(x) == int:
        lst[i][-1 - x] = '[ ]'
        
def incr(i,lst): 
    x = testEmpty(i,lst)
    if type(x) == int and x != 0:
        lst[i][-1 - (x-1)] = '[O]'
    elif lst[i][1] == '[ ]':
        lst[i][1] = '[O]'
        
def PInput(p):
    printDisplay()
    test = raw_input('Player %s, Your move: ' % p)
    if test == 'test':
        sys.exit()
    if l.count(test) == 1:
        p = [[],player1,player2][p]
        if test == 'shoot' and not testEmpty(2,p):
            print 'You have no Ammo.'
            return False
        elif test == 'shield' and not testEmpty(3,p):
            print 'You have no Shield.'
            return False
        elif test == 'reload' and testEmpty(2,p) == 0 and type(testEmpty(2,p)) == int:
            print 'Your clip is full.' # no it isnt
            return False
        else:
            return test
    else:
        print 'Actions include only "shoot," "reload" and "shield."'
        return False

while not victory:
    A1 = PInput(1)
    while type(A1) == bool:
        A1 = PInput(1)
    for x in range(0,100):
        print ('Hiding response...')
    A2 = PInput(2)
    while type(A2) == bool:
        A1 = PInput(2)
    for x in range(0,100):
        print ('Hiding response...')
    for p in [player1,player2]:
        if not testEmpty(3,p):
            p[3] == ['SHLD:','[O]','[O]','[O]']
    for A in [[A1, player1],[A2, player2]]:
        if A[0] == 'shoot':
            decr(2,A[1])
        elif A[0] == 'shield':
            decr(3,A[1])
    result(A1,A2)
    if not testEmpty(1, player1) and type(testEmpty(1, player1)) == bool:
        victory = True
        print '%s Wins!' % player2[0]
    if not testEmpty(1, player2) and type(testEmpty(1, player1)) == bool:
        victory = True
        print '%s Wins!' % player1[0]