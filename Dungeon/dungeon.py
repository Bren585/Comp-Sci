from Tkinter import *
import PIL.Image, PIL.ImageTk
import os.path

root = Tk()
root.wm_title('Dungeon Game')
directory = os.path.dirname(os.path.abspath(__file__))

## DISPLAY #####################################################################
################################################################################

## MAP ################################

field = Canvas(root,width = 128*5, height = 128*5, background = '#000000', takefocus = True)
field.grid(row=0,column=0,rowspan = 5, columnspan = 5)

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
        return [1,0]
    if heroD == 'E':
        return [0,1]
    if heroD == 'S':
        return [-1,0]
    if heroD == 'W':
        return [0,-1]

p_x, p_y = 2,2

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
            else:
                temp1 = floor[p_y+y][p_x+x]
                temp2 = lkup[int(temp1)]
                temp3 = temp2 + '(' + str(x+2) + ',' + str(y+2) + ')'
                exec temp3

create_map()

## STATUS DISPLAY ######################

Sdisp = Canvas(root, width = 128*5, height = 256, background = '#000000')
Sdisp.grid(row = 0, column = 6, columnspan = 5, rowspan = 2)

## HERO STATUS

## INVENTORY #

invBOX = Sdisp.create_rectangle(288, 32, 608, 224, fill = '#FFFFFF')
selx = 300
sely = 48
selh = 16
selw = 296
invSEL = Sdisp.create_rectangle(selx, sely, selx + selw, sely + selh, fill = '#CCCCCC')
invTEXT = Sdisp.create_text(304, 48, anchor = NW, text = 'INVENTORY:')

def down(event):
    if event.x >= 288 and event.x <= 608 and event.y >= 32 and event.y <= 224:
        'yeet'

def up(event):
    'yote'

Sdisp.bind('<Button-1>', down)
Sdisp.bind('<ButtonRelease-1>', up)

def sel_move(x = 300, y = 48):
    global selx
    global sely
    selx = x
    sely = y
    Sdisp.coords(invSEL, selx, sely, selx + selw, sely + selh)

sel_move(-100,-100)

inv = []

def write_inv():
    text = 'INVENTORY:\n'
    for i in inv:
        test1 = len(i[0])
        test2 = len(str(i[1]))
        test3 = ''
        for j in range(0,64-(test1+test2)):
            test3 += '.'
        text += str(i[0]) + str(test3) + str(i[1]) + '\n'
    Sdisp.itemconfig(invTEXT, text = text)

def store(item):
    if len(inv) == 0:
        inv.append([item[1],int(item[0])])
    else:
        for i in inv:
            if i[0] == item[1]:
                i[1] += int(item[0])
            else:
                inv.append([item[1],int(item[0])])
            if i[1] == 0:
                inv.remove(i)
    write_inv()

## CONTROL PAD #########################

def moveN():
    global p_y
    global heroD
    global heroS
    global heroSP
    heroD = 'N'
    if p_y > 0:
        test = floor[p_y - 1][p_x]
        if test == '1':
            heroS = heroSP
            heroSPFlip()
            p_y += -1
        else:
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
        test = floor[p_y][p_x + 1]
        if test == '1':
            heroS = heroSP
            heroSPFlip()
            p_x += 1
        else:
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
        test = floor[p_y + 1][p_x]
        if test == '1':
            heroS = heroSP
            heroSPFlip()
            p_y += 1
        else:
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
        test = floor[p_y][p_x - 1]
        if test == '1':
            heroS = heroSP
            heroSPFlip()
            p_x += -1
        else:
            heroS = 0
    else:
        heroS = 0
    create_map()

def Act():
    global floor
    ty, tx = [p_y, p_x]
    ty += dirCheck()[0]
    tx += dirCheck()[1]
    test = floor[ty][tx]
    if test == '2':
        floor[ty][tx] = '3'
        create_map()
        store(read_data(ty,tx))

N = Button(root, width = 10, height = 4, text = 'North', command = moveN)
N.grid(column = 7, row = 2, sticky = 's')

E = Button(root, width = 10, height = 4, text = 'East', command = moveE)
E.grid(column = 8, row = 3, sticky = 'w')

S = Button(root, width = 10, height = 4, text = 'South', command = moveS)
S.grid(column = 7, row = 4, sticky = 'n')

W = Button(root, width = 10, height = 4, text = 'West', command = moveW)
W.grid(column = 6, row = 3, sticky = 'e')

A = Button(root, width = 10, height = 4, text = 'Act', command = Act)
A.grid(column = 7, row = 3)
field.bind('<Return>', Act)

def key_pressed(event):
    k = event.char
    if k == 'w':
        moveN()
    if k == 'a':
        moveW()
    if k == 's':
        moveS()
    if k == 'd':
        moveE()
field.bind('<Key>', key_pressed)

## WHATEVER ############################

root.mainloop()