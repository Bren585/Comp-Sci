import random
import Tkinter

root = Tkinter.Tk()

disp = Tkinter.Canvas(root,width=400, height=300, background = '#FFFFFF')
disp.grid(row=0, column=1)

label = Tkinter.Label(root, text = 'Please Wait...')
label.grid(row=1,column=1)

b1 = Tkinter.Button(root, text = ' ', width=1, height=1)
b1.grid(row=2, column=0)
b2 = Tkinter.Button(root, text = ' ', width=1, height=1)
b2.grid(row=3, column=0)
b3 = Tkinter.Button(root, text = ' ', width=1, height=1)
b3.grid(row=4, column=0)

b1l = Tkinter.Label(root, text = '')
b1l.grid(row=2, column=1)
b2l = Tkinter.Label(root, text = '')
b2l.grid(row=2, column=2)
b3l = Tkinter.Label(root, text = '')
b3l.grid(row=2, column=3)

log = Tkinter.Text(root, width=20)
log.grid(column=3,row=0,rowspan=5)

E = [
'Evil Dragon',
['HP','900','900'],
['MP','500','500'],
['den','5'],
['atk','10']
]

name = []
print "What is the Hero's name?"
name = raw_input()
P = [
str(name) + ' The Hero',
['HP','600','600'],
['MP','150','150'],
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
    label.congfig(text = 'COMMAND?')
    b1l.config(text = menu[0][1])
    b2l.config(text = menu[1][1])
    b3l.config(text = menu[2][1])

def displayF():
    label.congfig(text = 'FIGHT:')
    b1l.config(text = fight[0][1])
    b2l.config(text = fight[1][1])
    b3l.config(text = fight[2][1])
    
def displayI():
    label.congfig(text = 'ITEM:')
    b1l.config(text = item[0][1])
    b2l.config(text = item[1][1])
    b3l.config(text = item[2][1])

def displayS():
    label.congfig(text = 'SPELL:')
    b1l.config(text = spell[0][1])
    b2l.config(text = spell[1][1])
    b3l.config(text = spell[2][1])

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
        
ptC = True
def pt():
    global ptC
    if ptC:
        incr(P,1,100)
        ptC = False
        ail[1][1].append([2,'ptC = True'])
    else:
        PSelect()

bmC = True
def bm():
    global bmC
    if bmC:
        dmg([[],[],[],[],[[],10]],E,0)
        decr(E,3,3); decr(E,4,3)
        bmC = False
        ail[0][1].append([3,'incr(E,3,3); incr(E,4,3)'])
        ail[1][1].append([3,'bmC = True'])
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
    if int(P[2][1]) >= 15:
        dmg(P,E,10)
        decr(P,2,15)
    else:
        PSelect()

shC = True
def sh():
    global shC
    if shC and int(P[2][1]) >= 10:
        incr(P,3,7)
        decr(P,2,10)
        shC = False
        ail[1][1].append([3,'decr(P,3,7); shC = True'])
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
        coin = random.choice([0,1])
        exec ['dsp()','reg("w")'][coin] #desperation / regenerate (weak)
        return
    if HP >= 700:
        r = True
        if len(ail[0][1]) >= 1:
            for x in ail[0][1]:
                if x[1][:4] == 'incr':
                    r = False
        if not r:
            coin = random.choice([0,1])
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

def buf(coin):
    if coin == 0:
        incr(E,3,3)
        ail.append([3,'decr(E,3,3)'])
        displayEAct('Sharpen Claws', [E[0], 'defense', 'increased'])
    if coin == 1:
        incr(E,4,3)
        ail.append([3,'decr(E,4,3)'])
        displayEAct('Sharpen Claws', [E[0], 'attack', 'increased'])

def clw():
    dmg(E, P, 3)
    displayEAct('Claw')

def sma():
    dmg(E, P, -1)
    decr(P,3,3)
    ail.append([2, 'incr(P,3,3)'])
    displayEAct('Smash', [name, 'defense', 'decreased'])

def fir():
    if int(E[2][1]) >= 15:
        dmg(E,P,6)
        decr(E,2,15)
        displayEAct('Fireball')
    else:
        exec 'stg()'

def wbl():
    if int(E[2][1]) >= 20:
        dmg(E,P,8)
        decr(E,2,20)
        displayEAct('Windblast')
    else:
        exec 'stg()'

def reg(amount):
    if int(E[2][1]) >= 25:
        decr(E,2,25)
        if amount == 'w':
            incr(E,1,70)
            displayEAct('Desperate Regeneration')
        if amount == 's':
            incr(E,1,150)
            displayEAct('Regeneration')
    else:
        exec 'stg()'

def dsp():
    incr(E,4,2); incr(E,3,2)
    ail.append([2,'decr(E,4,2); decr(E,3,2)'])
    dmg(E, P, 2)
    displayEAct('Desperation', [E[0], 'attack', 'increased'], [E[0], 'defense', 'increased'])

def stg():
    dmg(E, P, 2)
    dmg(E, E, -1)
    displayEAct('Struggle')

def displayEAct(act, ail1 = 'None', ail2 = 'None'):
    displayMain()
    print 'Evil Dragon uses %s!' % (act)
    print ''
    if ail2 == 'None':
        if ail1 == 'None':
            print ''
            print ''
        else:
            print ail1[0] + '\'s ' + ail1[1] + ' was ' + ail1[2] + '!'
            print ''
    else:
        if ail1 == 'None':
            print ail2[0] + '\'s ' + ail2[1] + ' was ' + ail2[2] + '!'
            print ''
        else:
            print ail1[0] + '\'s ' + ail1[1] + ' was ' + ail1[2] + '!'
            print ail2[0] + '\'s ' + ail2[1] + ' was ' + ail2[2] + '!'
    raw_input()
        
##############################################################################

def phaseEnd():
    global vic
    if int(P[1][1]) <= 0:
        vic = True
    if int(E[1][1]) <= 0:
        vic = True

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
vic = False
def Game():
    global vic
    vic = False
    while not vic:
        turnStart()
        raw_input()
        PSelect()
        phaseEnd()
        if not vic:
            ESelect()
            phaseEnd()
    if P[1][1] != 0:
        displayMain()
        print ''
        print '      CONGRATULATIONS, HERO!'
        print '      YOU HAVE SLAIN THE DRAGON!'
        print ''
        raw_input()
    else:
        displayMain()
        print ''
        print '                GAME'
        print '                OVER'
        print ''
        raw_input()

root.mainloop()