from Tkinter import *
import PIL.Image, PIL.ImageTk
import os.path
import random

root = Tk()
root.wm_title('Dungeon Game')
directory = os.path.dirname(os.path.abspath(__file__))

## DISPLAY #####################################################################
################################################################################

## MAP ################################

field = Canvas(root,width = 128*7, height = 128*5, background = '#000000', takefocus = True)
field.grid(row=0,column=0)

lkup = ['null','create_tile','create_chest0','create_chest1', 'create_door','create_bs','create_gs','create_rs']

fnum = 0
floor = []

heroS = 0
heroSP = 1

dead = False

def heroSPFlip():
    global heroSP
    if heroSP == 1:
        heroSP = 2
    elif heroSP == 2:
        heroSP = 1

heroD = 'N'

def dirCheck():
    if heroD == 'N':
        return [-1,0]
    if heroD == 'E':
        return [0,1]
    if heroD == 'S':
        return [1,0]
    if heroD == 'W':
        return [0,-1]

p_x, p_y = 0,0

def read_floor(new = False):
    global floor
    if not new:
        newfloor = []
        fname = 'F' + str(fnum) + '.txt'
        with open(fname) as f:
            r = 0
            for y in f:
                row = []
                c = 0
                for x in y:
                    if x != '\n':
                        row.append(x)
                    if x == '5':
                        new_enemy('b',r,c)
                    if x == '6':
                        new_enemy('g',r,c)
                    if x == '7':
                        new_enemy('r',r,c)
                    c += 1
                newfloor.append(row)
                r += 1
        floor = newfloor

def read_data(y,x):
    fname = 'F' + str(fnum) + 'D.txt'
    with open(fname) as f:
        for i in f:
            rx,ry,q,item = i.split()
            if rx == str(x) and ry == str(y):
                return q, item
    return 'error','error'


## EMPTY ####

def null(x,y):
    x = y

## TILE #####

tilename = os.path.join(directory, 'tile.png')
PILtile = PIL.Image.open(tilename)
Tktile = PIL.ImageTk.PhotoImage(PILtile)
def create_tile(x,y):
    field.create_image((x*128,y*128), image = Tktile, anchor = NW, tags = 'sc')

## CHEST ####

chestname0 = os.path.join(directory, 'chest0.png')
PILchest0 = PIL.Image.open(chestname0)
Tkchest0 = PIL.ImageTk.PhotoImage(PILchest0)
def create_chest0(x,y):
    field.create_image((x*128,y*128), image = Tkchest0, anchor = NW, tags = 'sc')

chestname1 = os.path.join(directory, 'chest1.png')
PILchest1 = PIL.Image.open(chestname1)
Tkchest1 = PIL.ImageTk.PhotoImage(PILchest1)
def create_chest1(x,y):
    field.create_image((x*128,y*128), image = Tkchest1, anchor = NW, tags = 'sc')

## ENEMY ####

bsname = os.path.join(directory, 'bslime.png')
PILbs = PIL.Image.open(bsname)
Tkbs = PIL.ImageTk.PhotoImage(PILbs)
def create_bs(x,y):
    field.create_image((x*128,y*128), image = Tkbs, anchor = NW, tags = 'sc')

gsname = os.path.join(directory, 'gslime.png')
PILgs = PIL.Image.open(gsname)
Tkgs = PIL.ImageTk.PhotoImage(PILgs)
def create_gs(x,y):
    field.create_image((x*128,y*128), image = Tkgs, anchor = NW, tags = 'sc')

rsname = os.path.join(directory, 'rslime.png')
PILrs = PIL.Image.open(rsname)
Tkrs = PIL.ImageTk.PhotoImage(PILrs)
def create_rs(x,y):
    field.create_image((x*128,y*128), image = Tkrs, anchor = NW, tags = 'sc')

## HERO #####

heros = os.path.join(directory, 'hero')
Tkhero = ''
def create_hero(direction,state):
    global Tkhero
    x = str(state) + str(direction) + '.png'
    heroname = os.path.join(heros, x)
    PILhero = PIL.Image.open(heroname)
    Tkhero = PIL.ImageTk.PhotoImage(PILhero)
    field.create_image((256,256), image = Tkhero, anchor = NW, tags = 'sc')

## DOOR #####

doorname = os.path.join(directory, 'door.png')
PILdoor = PIL.Image.open(doorname)
Tkdoor = PIL.ImageTk.PhotoImage(PILdoor)
def create_door(x,y):
    field.create_image((x*128,y*128), image = Tkdoor, anchor = NW, tags = 'sc')

## CREATE MAP

read_floor()

def create_map():
    field.delete('sc')
    for y in range(-2,3):
        for x in range(-2,3):
            if x == 0 and y == 0 and not dead:
                create_hero(heroD,heroS)
            elif x == 0 and y == 0 and dead:
                create_tile(2,2)
            elif p_y+y >= 0 and p_x+x >= 0:
                try:
                    temp1 = floor[p_y+y][p_x+x]
                    temp2 = lkup[int(temp1)]
                    temp3 = temp2 + '(' + str(x+2) + ',' + str(y+2) + ')'
                    exec temp3
                except IndexError:
                    null(0,0)

create_map()

## ENEMY TRACKING ETC ##################

e = []
#[HP,ATK,X,Y,color]
lkp = [[],[],[],[],[],'b','g','r']

def new_enemy(color,y,x):
    if color == 'b':
        e.append([1*fnum,1*fnum,x,y,'b'])
    if color == 'g':
        e.append([2*fnum,2,x,y,'g'])
    if color == 'r':
        e.append([2,2*fnum,x,y,'r'])

def enemy_move():
    ID = 0
    for i in e:
        e_x, e_y = i[2], i[3]
        floor[e_y][e_x] = '1'
        move = []
        for j in ([0,1],[0,-1],[1,0],[-1,0]):
            go = True
            if e_x + j[0] == p_x and e_y + j[1] == p_y and go:
                move = [0,0]
                engage(ID)
                go = False
        if move == []:
            opt = [[0,1],[0,-1],[1,0],[-1,0]]
            random.shuffle(opt)
            for j in opt:
                try:
                    if floor[e_y+j[1]][e_x+j[0]] == '1' and e_y+j[1] > 0 and e_x+j[0] > 0:
                        move = j
                except IndexError:
                    pass
        e_x += move[0]; e_y += move[1]
        i[2], i[3] = e_x, e_y
        if not i[0] <= 0:
            num = lkp.index(i[4])
            floor[e_y][e_x] = num
        ID += 1
    create_map()
        
def engage(ID):
    global hearts
    global e
    global dur
    hearts -= e[ID][1]
    e[ID][0] -= (atk+int(mt))
    if e[ID][0] <= 0:
        floor[e[ID][2]][e[ID][3]] = '1'
        e.pop(ID)
    dur = str(int(dur)-1)
    if dur <= 0:
        equip('Nothing')
    create_map()
    update_status()

## STATUS DISPLAY ######################

Sdisp = field.create_rectangle(128*5,0,128*7,128*5, fill = '#888888')

## HERO STATUS

hearts = 3
max_hearts = 3
atk = 1
weapon = 'Nothing'
mt = 0
dur = 99999999
effect = 'null(0,0)'
desc = 'None'

sBOX = field.create_rectangle(128*5+32, 32, 128*7-32, 256, fill = '#FFFFFF')
sTEXT = field.create_text(128*5+48, 48, anchor = NW, text = '')

def update_status():
    text = 'STATUS:\n\nHP: '
    fill = 0
    for i in range(0,max_hearts):
        if fill < hearts:
            text += u'\u2665' + ' '
            fill += 1
        else:
            text += u'\u2661' + ' '
    text += '\nAttack: %d\n' % (atk + int(mt))
    text += '\n\n'
    text += 'Weapon: %s\n' % (weapon)
    text += 'Might: %s\n' % (mt)
    text += 'Durability: %s\n' % (dur)
    text += 'Effect: %s\n' % (desc)
    field.itemconfig(sTEXT, text = text)
    if hearts <= 0:
        die()
update_status()

def gain(x):
    global max_hearts
    max_hearts += 1
    heal(1)
    update_status()

def heal(x):
    global hearts
    hearts += x
    if hearts > max_hearts:
        hearts = max_hearts
    update_status()

def die():
    global dead
    dead = True
    create_map()

## INVENTORY #

menu = False
def menu_mode():
    global sel
    global menu
    if menu:
        menu = False
        sel_move(-100,-100)
    else:
        menu = True
        if len(inv) > 0:
            sel_move(y = (sel*16)+256+48)
    if sel > len(inv):
        sel = 1

sel = 1

def mUp():
    global sel
    sel -= 1
    if sel <= 0:
        sel = len(inv)
    if len(inv) > 0:
        sel_move(y = (sel*16)+256+48)

def mDown():
    global sel
    sel += 1
    if sel > len(inv):
        sel = 1
    if len(inv) > 0:
        sel_move(y = (sel*16)+256+48)

def mSel():
    use(inv[sel-1])
    menu_mode()
    write_inv()
    update_status()

def use(thing):
    with open('lookup.txt') as f:
        for line in f:
            item, command = line.split()
            if item == thing[0]:
                store([-1,item])
                exec command

def equip(wep):
    global dur
    global mt
    global effect
    global weapon
    global desc
    with open('weapons.txt') as f:
        for line in f:
            name, d, m, eff, de = line.split()
            if wep == name:
                weapon = name
                dur = d
                mt = m
                effect = eff
                desc = de
    update_status()

def brk():
    global dur
    dur = str(int(dur)-1)
    if int(dur) <= 0:
        equip('Nothing')
    update_status()

invBOX = field.create_rectangle(128*5+32,256+32,128*7-32,128*5-32, fill = '#FFFFFF')
selx = 128*5+44
sely = 256+48
selh = 16
selw = 128+40
invSEL = field.create_rectangle(selx, sely, selx + selw, sely + selh, fill = '#CCCCCC')
invTEXT = field.create_text(128*5+48, 256+48, anchor = NW, text = 'INVENTORY:')
invQ = field.create_text(128*7-48, 256+48, anchor = NE, text = '\n')

def sel_move(x = 128*5+44, y = 256+48):
    global selx
    global sely
    selx = x
    sely = y
    field.coords(invSEL, selx, sely, selx + selw, sely + selh)

sel_move(-100,-100)

inv = []

def write_inv():
    text1 = 'INVENTORY:\n'
    text2 = '\n'
    for i in inv:
        text1 += i[0] + '\n'
        text2 += str(i[1]) + '\n'
    field.itemconfig(invTEXT, text = text1)
    field.itemconfig(invQ, text = text2)

def store(item):
    if len(inv) == 0:
        inv.append([item[1],int(item[0])])
    else:
        for i in inv:
            if i[0] == item[1]:
                i[1] += int(item[0])
                if i[1] <= 0:
                    inv.remove(i)
                write_inv()
                return
            if i[1] <= 0:
                inv.remove(i)
        inv.append([item[1],int(item[0])])
    write_inv()

## CONTROL PAD #########################

def moveN():
    global p_y
    global heroD
    global heroS
    global heroSP
    heroD = 'N'
    if p_y > 0:
        try:
            test = floor[p_y - 1][p_x]
            if test == '1':
                heroS = heroSP
                heroSPFlip()
                p_y += -1
            else:
                heroS = 0
        except IndexError:
            heroS = 0
    else:
        heroS = 0
    create_map()

def moveE():
    global p_x
    global heroD
    global heroS
    global heroSP
    heroD = 'E'
    if p_x < len(floor[0]):
        try:
            test = floor[p_y][p_x + 1]
            if test == '1':
                heroS = heroSP
                heroSPFlip()
                p_x += 1
            else:
                heroS = 0
        except IndexError:
            heroS = 0
    else:
        heroS = 0
    create_map()

def moveS():
    global p_y
    global heroD
    global heroS
    global heroSP
    heroD = 'S'
    if p_y < len(floor):
        try:
            test = floor[p_y + 1][p_x]
            if test == '1':
                heroS = heroSP
                heroSPFlip()
                p_y += 1
            else:
                heroS = 0
        except IndexError:
            heroS = 0
    else:
        heroS = 0
    create_map()

def moveW():
    global p_x
    global heroD
    global heroS
    global heroSP
    heroD = 'W'
    if p_x > 0:
        try:
            test = floor[p_y][p_x - 1]
            if test == '1':
                heroS = heroSP
                heroSPFlip()
                p_x += -1
            else:
                heroS = 0
        except IndexError:
            heroS = 0
    else:
        heroS = 0
    create_map()

def Act():
    global floor
    global p_y
    global p_x
    global fnum
    ty, tx = [p_y, p_x]
    ty += dirCheck()[0]
    tx += dirCheck()[1]
    try:
        test = floor[ty][tx]
    except IndexError:
        test = '0'
    if test == '2' and ty >= 0 and tx >= 0:
        floor[ty][tx] = '3'
        if read_data(ty,tx) != ('error','error'):
            store(read_data(ty,tx))
    if test == '4' and ty >= 0 and tx >= 0:
        ny, nx = read_data(ty,tx)
        fnum += 1
        read_floor()
        p_y, p_x = int(ny), int(nx)
    create_map()

def key_pressed(event):
    if not dead:
        k = event.char
        if k == 'w':
            if menu:
                mUp()
            else:
                moveN()
                enemy_move()
        if k == 'a':
            if not menu:
                moveW()
                enemy_move()
        if k == 's':
            if menu:
                mDown()
            else:
                moveS()
                enemy_move()
        if k == 'd':
            if not menu:
                moveE()
                enemy_move()
        if k == 'j':
            if menu and sel > 0:
                mSel()
            else:
                Act()
        if k == 'k':
            menu_mode()
        if k == 't':
            global hearts
            hearts -= 1
            update_status()
    field.after(50)
field.bind('<Key>', key_pressed)

## WHATEVER ############################
field.focus_force()
root.mainloop()