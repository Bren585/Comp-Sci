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
[['NN'],['D1'],['NN']],
[['D0'],['R2'],['R0']],
[['NN'],['R1'],['NN']]
]

def printRow(lst):
    if type(lst) == list:
        p = ''
        for x in range(0, len(lst)):
            p += str(lst[x])
        print p 

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
        z = lst[i]
        z[x] = '[ ]'
        return z

def result(A,B):
    r = rLookup[l.index(A)][l.index(B)]
    if r != 'NN':
        a,p = r.split()

while not victory:
    A1 = raw_input('Player 1, Your move: ')
    for x in range(0,100):
        print ('Hiding response...')
    A2 = raw_input('Player 2, Your move: ')
    for x in range(0,100):
        print ('Hiding response...')