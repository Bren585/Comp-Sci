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
    r = test.index(test[-1])
    empty = False
    run = 0
    while not empty and run < len(test) - 1:
        if test[r - run] == '[ ]':
            run + 1
        else:
            return run
    if run == len(test) - 1:
        return False

victory = False
responses = ['shoot', 'reload', 'shield']


while not victory:
    A1 = raw_input('Player 1, Your move: ')
    for x in range(0,100):
        print ('Hiding response...')
    A2 = raw_input('Player 2, Your move: ')
    for x in range(0,100):
        print ('Hiding response...')