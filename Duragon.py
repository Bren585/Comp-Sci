import random

E = [
'Evil Dragon',
['HP','000','000'],
['MP','000','000']
]

name = []
P = [
str(name) + ' The Hero',
['HP','000','000'],
['MP','000','000']
]

menu = [
['[ ]','FIGHT'],
['[ ]','ITEM'],
['[ ]','SPELL'],
]
mSel = []

def dFormat(lst,i):
    d = lst[i]
    d = d[0] + ': ' + str(d[1]) + '/' + str(d[2])
    return d

def mFormat(lst):
    return str(menu[lst][0]) + str(menu[lst][1])

def display():
    print ''
    print ''
    print ''
    print ''
    print ''
    print E[0]+'          '+P[0]
    print dFormat(E,1)+'          '+dFormat(P,1)
    print dFormat(E,2)+'          '+dFormat(P,2)
    print ''
    print 'Command?'
    print mFormat(0)
    print mFormat(1)
    print mFormat(2)
    
def PSelect():
    display()
    global mSel
    i = raw_input()
    while i != '':
        if mSel == []:
            if i == 'w':
                mSel = 0
            elif i == 's':
                mSel = 2
        else:
            menu[mSel][0] = '[ ]'
            if i == 'w':
                mSel += -1
                if mSel == -1:
                    mSel = 2
            elif i == 's':
                mSel += 1
                if mSel == 3:
                    mSel = 0
        if mSel != []:     
            menu[mSel][0] = '[*]'
        display()
        i = raw_input()
    return mSel