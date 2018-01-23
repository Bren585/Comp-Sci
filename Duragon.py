import random

E = [
'Evil Dragon',
['HP','900','900'],
['MP','500','500'],
['den','5'],
['atk','10']
]

#print "What is the Hero's name?"
#name = raw_input()
P = [
#str(name) + ' The Hero'
[],
['HP','400','400'],
['MP','100','100'],
['den','4'],
['atk','8']
]

ail = [
['E', []],
['P', []]
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

item = [
['[ ]','POTION'],
['[ ]','BOMB'],
['[ ]','RETURN']
]

spell = [
['[ ]','GIGADYNE'],
['[ ]','SHIELD'],
['[ ]','RETURN']
]

mSel = []

Turn = 0

##############################################################################

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
    print cFormat(item,0)
    print cFormat(item,1)
    print cFormat(item,2)

def displayS():
    print 'Spell:'
    print cFormat(spell,0)
    print cFormat(spell,1)
    print cFormat(spell,2)

##############################################################################

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

##############################################################################

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
    else:
        fight[mSel][0] = '[ ]'
        exec ['sd()','bw()','PSelect()'][mSel]

def sd():
    dmg(P,E,3)

def bw():
    dmg(P,E,5)
    decr(P,3,3)
    ail[1][1].append([1,'incr(P,3,3)'])

##############################################################################

def it():
    global mSel
    mSel = []
    displayMain()
    displayI()
    i = raw_input()
    while i != '':
        moveSel(item,i)
        displayMain()
        displayI()
        i = raw_input()
    if mSel == []:
        PSelect()
    else:
        item[mSel][0] = '[ ]'
        exec ['pt()','bm()','PSelect()'][mSel]
        
pt = True
def pt():
    global pt
    if pt:
        incr(P,1,100)
        pt = False
        ail[1][1].append([2,'pt = True'])
    else:
        PSelect()

bm = True
def bm():
    global bm
    if bm:
        dmg([[],[],[],[],[[],[10]]],E,0)
        decr(E,3,3); decr(E,4,3)
        bm = False
        ail[0][1].append([3,'incr(E,3,3); incr(E,4,3)'])
        ail[1][1].append([3,'bm = True'])
    else:
        PSelect()

##############################################################################

def s():
    global mSel
    mSel = []
    displayMain()
    displayS()
    i = raw_input()
    while i != '':
        moveSel(spell,i)
        displayMain()
        displayS()
        i = raw_input()
    if mSel == []:
        PSelect()
    else:
        spell[mSel][0] = '[ ]'
        exec ['gd()','sh()','PSelect()'][mSel]

def gd():
    if P[2][1] >= 15:
        dmg(P,E,10)
        decr(P,2,15)
    else:
        PSelect()

sh = True
def sh():
    global sh
    if sh and P[2][1] >= 10:
        incr(P,3,7)
        decr(P,2,10)
        sh = False
        ail[1][1].append([3,'decr(P,3,7); sh = True'])
    else:
        PSelect

##############################################################################

def cooldown(x):
    l = len(ail[x][1])
    for i in range(0,l):
        turn, name = ail[x][1].pop(0)
        turn += -1
        if turn <= 0:
            exec(name)
        else:
            ail[x][1].append([turn,name])

def turnStart():
    global Turn
    Turn += 1
    cooldown(0)
    cooldown(1)
    displayMain()
    print ''
    print '             TURN %d' % Turn
    print '             START'
    print ''

##############################################################################

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
    else:
        menu[mSel][0] = '[ ]'
        exec ['f()','it()','s()'][mSel]

##############################################################################

def ESelect():
    HP, MP = int(E[1][1]), int(E[2][1])
    if HP <= 200:
        coin = random.choice(0,1)
        exec ['dsp()','reg("w")'][coin] #desperation / regenerate (weak)
        return
    if MP <= 0:
        exec 'str()' #struggle
        return
    if HP >= 700:
        r = False
        for x in ail[0]:
            if x[1][:4] == 'decr':
                r = True
            elif x[1][:4] == 'incr':
                r = False
        if not r:
            coin = random.choice(0,1)
            exec 'buf(coin)' #sharpen claws
            return
    else:
        prob = random.randint(0,100)
        if 0 <= prob and prob <= 30:
            exec 'clw()' #claw
        if 31 <= prob and prob <= 50:
            exec 'sma()' #smash
        if 51 <= prob and prob <= 70:
            exec 'fir()' #fireball
        if 71 <= prob and prob <= 90:
            exec 'wbl()' #windblast
        if 91 <= prob and prob <= 100:
            exec 'reg("s")' #regenerate (strong)

##############################################################################

##############################################################################

def dCalc(a,d):
    r = a - d
    if r > 0:
        return r
    else:
        return 0

def dmg(atk,den,mt):
    decr(den, 1, dCalc(int(atk[4][1]) + mt, int(den[3][1]))*10)

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

###############################################################################

def Game():
        turnStart()
        raw_input()
        PSelect()
        #ESelect()
        #turnEnd()