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
['[ ]','SPELL']
]

fight = [
['[ ]','SWORD'],
['[ ]','BOW'],
['[ ]','RETURN']
]

mSel = []

def dFormat(lst,i):
    d = lst[i]
    d = d[0] + ': ' + str(d[1]) + '/' + str(d[2])
    return d

def cFormat(lst,i):
    return str(lst[i][0]) + str(lst[i][1])

def displayMain():
    print ''
    print ''
    print ''
    print ''
    print ''
    print E[0]+'          '+P[0]
    print dFormat(E,1)+'          '+dFormat(P,1)
    print dFormat(E,2)+'          '+dFormat(P,2)
    print ''

def displayComm():
    print 'Command?'
    print cFormat(menu,0)
    print cFormat(menu,1)
    print cFormat(menu,2)

def displayF():
    print 'Fight:'
    print cFormat(fight,0)
    print cFormat(fight,1)
    print cFormat(fight,2)
    
def displayI():
    print 'Item:'
    print cFormat(0)
    print cFormat(1)
    print cFormat(2)

def displayS():
    print 'Spell:'
    print cFormat(0)
    print cFormat(1)
    print cFormat(2)

def moveSel(lst,i):
    global mSel
    if mSel == []:
        if i == 'w':
            mSel = 0
        elif i == 's':
            mSel = 2
    else:
        lst[mSel][0] = '[ ]'
        if i == 'w':
            mSel += -1
            if mSel == -1:
                mSel = 2
        elif i == 's':
            mSel += 1
            if mSel == 3:
                mSel = 0
    if mSel != []:     
        lst[mSel][0] = '[*]'
        
def f():
    global mSel
    mSel = []
    displayMain()
    displayF()
    i = raw_input()
    while i != '':
        moveSel(fight,i)
        displayMain()
        displayF()
        i = raw_input()
    if mSel == []:
        PSelect()
        fight[mSel][0] = '[ ]'
    else:
        exec ['s()','b()','PSelect()'][mSel]

def i():
    global mSel
    mSel = []
    displayMain()
    displayI()
    
def s():
    global mSel
    mSel = []
    displayMain()
    displayS()

def PSelect():
    displayMain()
    displayComm()
    i = raw_input()
    while i != '':
        moveSel(menu,i)
        displayMain()
        displayComm()
        i = raw_input()
    if mSel == []:
        PSelect()
        menu[mSel][0] = '[ ]'
    else:
        exec ['f()','i()','s()'][mSel]

def dCalc(a,d):
    r = a - d
    if r > 0:
        return r
    else:
        return 0

def decr(lst,i,x):
    a = lst[i][1]
    a = str(int(a) - x)
    if int(a) <= 0:
        lst[i][1] = 0
        return
    while len(a) != 3:
        a = '0' + a
    lst[i][1] = a

def incr(lst,i,x):
    a = lst[i][1]
    a = str(int(a) + x)
    if int(a) >= 999:
        lst[i][1] = 999
        return
    while len(a) != 3:
        a = '0' + a
    lst[i][1] = a
