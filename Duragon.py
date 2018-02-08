import random
import Tkinter
import PIL.Image, PIL.ImageTk
import os.path

root = Tkinter.Tk()

disp = Tkinter.Canvas(root,width=400, height=300, background = '#808080')
disp.grid(row=0, column=1)

disp.create_rectangle(12,12,132,82, fill='#FFFFFF')
disp.create_rectangle(268,218,388,288, fill='#FFFFFF')

directory = os.path.dirname(os.path.abspath(__file__))
Efilename = os.path.join(directory, 'Dra.png')
EImg = PIL.Image.open(Efilename)
Etkimg = PIL.ImageTk.PhotoImage(EImg)
icon = disp.create_image((330,100), image = Etkimg)

Pfilename = os.path.join(directory, 'Her.png')
PImg = PIL.Image.open(Pfilename)
Ptkimg = PIL.ImageTk.PhotoImage(PImg)
icon = disp.create_image((75,240), image = Ptkimg)

label = Tkinter.Label(root, text = 'Press Any Button to Begin')
label.grid(row=1,column=1)

mSel = []

def b1c():
    global gameStart
    global mSel
    mSel = 0
    if gameStart == 0:
        Game()
        gameStart = 1

def b2c():
    global gameStart
    global mSel
    mSel = 0
    if gameStart == 0:
        Game()
        gameStart = 1

def b3c():
    global gameStart
    global mSel
    mSel = 0
    if gameStart == 0:
        Game()
        gameStart = 1

b1 = Tkinter.Button(root, text = ' ', width=1, height=1, command = b1c)
b1.grid(row=2, column=0)
b2 = Tkinter.Button(root, text = ' ', width=1, height=1, command = b2c)
b2.grid(row=3, column=0)
b3 = Tkinter.Button(root, text = ' ', width=1, height=1, command = b3c)
b3.grid(row=4, column=0)

b1l = Tkinter.Label(root, text = '')
b1l.grid(row=2, column=1)
b2l = Tkinter.Label(root, text = '')
b2l.grid(row=2, column=2)
b3l = Tkinter.Label(root, text = '')
b3l.grid(row=2, column=3)

log = Tkinter.Text(root, width=20)
log.grid(column=3,row=0,rowspan=10)

def lg(text):
    log.insert(Tkinter.END, text + '\n')

def dFormat(lst,i):
    d = lst[i]
    d = d[0] + ': ' + str(d[1]) + '/' + str(d[2])
    return d

E = [
'Evil Dragon',
['HP','900','900'],
['MP','500','500'],
['den','5'],
['atk','10']
]

ED = [
disp.create_text(18,18, anchor='nw', text=E[0]),
disp.create_text(18,36, anchor='nw', text=dFormat(E,1)),
disp.create_text(18,54, anchor='nw', text=dFormat(E,2))
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

PD = [
disp.create_text(274,224, anchor='nw', text=P[0]),
disp.create_text(274,242, anchor='nw', text=dFormat(P,1)),
disp.create_text(274,260, anchor='nw', text=dFormat(P,2))
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

Turn = 0

##############################################################################

def dUpdate():
    for i in range(0,len(ED)):
        disp.itemconfig(ED[i], text=dFormat(E,i))
    for i in range(0,len(PD)):
        disp.itemconfig(PD[i], text=dFormat(P,i))

def displayComm():
    label.config(text = 'COMMAND?')
    b1l.config(text = menu[0][1])
    b2l.config(text = menu[1][1])
    b3l.config(text = menu[2][1])

def displayF():
    label.config(text = 'FIGHT:')
    b1l.config(text = fight[0][1])
    b2l.config(text = fight[1][1])
    b3l.config(text = fight[2][1])
    
def displayI():
    label.config(text = 'ITEM:')
    b1l.config(text = item[0][1])
    b2l.config(text = item[1][1])
    b3l.config(text = item[2][1])

def displayS():
    label.config(text = 'SPELL:')
    b1l.config(text = spell[0][1])
    b2l.config(text = spell[1][1])
    b3l.config(text = spell[2][1])

##############################################################################

def wait():
    global mSel
    mSel = []
    label.config(text = 'Press any button to Continue')
    wait2()
    
def wait2():
    global mSel
    if mSel == []:
        root.after(10,wait2())  

##############################################################################

def f():
    global mSel
    mSel = []
    dUpdate()
    displayF()
    wait2()
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
    dUpdate()
    displayI()
    wait2()
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
    dUpdate()
    displayS()
    wait2()
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
        PSelect()

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
    dUpdate()
    lg('TURN %s START' % Turn)

##############################################################################

def PSelect():
    global mSel
    mSel = []
    dUpdate()
    displayComm()
    wait2()
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
    dUpdate()
    print 'Evil Dragon uses %s!' % (act)
    print ''
    if ail2 == 'None':
        if ail1 == 'None':
            lg('')
        else:
            lg(ail1[0] + '\'s ' + ail1[1] + ' was ' + ail1[2] + '!')
    else:
        if ail1 == 'None':
            lg(ail2[0] + '\'s ' + ail2[1] + ' was ' + ail2[2] + '!')
        else:
            lg(ail1[0] + '\'s ' + ail1[1] + ' was ' + ail1[2] + '!')
            lg(ail2[0] + '\'s ' + ail2[1] + ' was ' + ail2[2] + '!')
    wait()
        
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
    x = dCalc(int(atk[4][1]) + mt, int(den[3][1]))*10
    decr(den, 1, x)
    lg(den[0] + ' took %d damage!' % x)

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
        wait()
        PSelect()
        phaseEnd()
        if not vic:
            ESelect()
            phaseEnd()
    if P[1][1] != 0:
        dUpdate()
        lg('Congratulations, Hero!')
        lg('You defeated the Dragon!')
        wait()
    else:
        dUpdate()
        lg('GAME OVER')
        wait()

gameStart = 0
root.mainloop()