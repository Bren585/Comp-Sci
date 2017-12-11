import random

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

victory = True ## Make False in final
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
        for p in pTrans[int(p)]:
            decr(a,p)

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
        lst[i][-1 - (x-1)] = '[ ]'
        
def PInput(p):
    test = raw_input('Player %s, Your move:')

while not victory:
    A1 = PInput(1)
    for x in range(0,100):
        print ('Hiding response...')
    A2 = raw_input('Player 2, Your move: ')
    for x in range(0,100):
        print ('Hiding response...')