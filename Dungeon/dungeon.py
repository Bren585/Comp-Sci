from Tkinter import *
import PIL.Image, PIL.ImageTk
import os.path

root = Tk()
root.wm_title('Dungeon Game')
directory = os.path.dirname(os.path.abspath(__file__))

## DISPLAY #####################################################################
################################################################################

## MAP ################################

field = Canvas(root,width = 128*7, height = 128*5, background = '#000000', takefocus = True)
field.grid(row=0,column=0)

lkup = ['null','create_tile','create_chest0','create_chest1']

fnum = 0
floor = []

heroS = 0
heroSP = 1

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
            for y in f:
                row = []
                for x in y:
                    if x != '\n':
                        row.append(x)
                newfloor.append(row)
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
bTile = PILtile
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

## LOOT #####

## CREATE MAP

read_floor()

def create_map():
    field.delete('sc')
    for y in range(-2,3):
        for x in range(-2,3):
            if x == 0 and y == 0:
                create_hero(heroD,heroS)
            elif p_y+y >= 0 and p_x+x >= 0:
                try:
                    temp1 = floor[p_y+y][p_x+x]
                    temp2 = lkup[int(temp1)]
                    temp3 = temp2 + '(' + str(x+2) + ',' + str(y+2) + ')'
                    exec temp3
                except IndexError:
                    null(0,0)

create_map()

## STATUS DISPLAY ######################

Sdisp = field.create_rectangle(128*5,0,128*7,128*5, fill = '#888888')

## HERO STATUS

## INVENTORY #

menu = False
def menu_mode():
    global menu
    if menu:
        menu = False
        sel_move(-100,-100)
    else:
        menu = True
        if len(inv) > 0:
            sel_move(y = (sel*16)+256+48)

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

def use(thing):
    item = thing[0]
    q = thing[1]

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
                return
            if i[1] == 0:
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
    ty, tx = [p_y, p_x]
    ty += dirCheck()[0]
    tx += dirCheck()[1]
    try:
        test = floor[ty][tx]
    except IndexError:
        test = '0'
    if test == '2' and ty >= 0 and tx >= 0:
        floor[ty][tx] = '3'
        create_map()
        if read_data(ty,tx) != ('error','error'):
            store(read_data(ty,tx))

def key_pressed(event):
    k = event.char
    if k == 'w':
        if menu:
            mUp()
        else:
            moveN()
    if k == 'a':
        if not menu:
            moveW()
    if k == 's':
        if menu:
            mDown()
        else:
            moveS()
    if k == 'd':
        if not menu:
            moveE()
    if k == 'j':
        if menu:
            mSel()
        else:
            Act()
    if k == 'k':
        menu_mode()
    field.after(50)
field.bind('<Key>', key_pressed)

## WHATEVER ############################
field.focus_force()
root.mainloop()