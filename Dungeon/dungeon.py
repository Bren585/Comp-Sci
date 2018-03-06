import Tkinter
import PIL.Image, PIL.ImageTk
import os.path

root = Tkinter.Tk()
directory = os.path.dirname(os.path.abspath(__file__))

## DISPLAY #####################################################################
################################################################################

## MAP ################################

field = Tkinter.Canvas(root,width = 128*5, height = 128*5, background = '#000000')
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
p_x, p_y = 2,2

def read_floor():
    global floor
    floor = []
    fname = 'F' + str(fnum) + '.txt'
    with open(fname) as f:
        for y in f:
            row = []
            for x in y:
                if x != '\n':
                    row.append(x)
            floor.append(row)

## EMPTY ###

def null(x,y):
    x = y
    x == 0

## TILE ####

tilename = os.path.join(directory, 'tile.png')
PILtile = PIL.Image.open(tilename)
bTile = PILtile
Tktile = PIL.ImageTk.PhotoImage(PILtile)
def create_tile(x,y):
    field.create_image((x*128,y*128), image = Tktile, anchor = Tkinter.NW, tags = 'sc')

## CHEST ###

chestname = os.path.join(directory, 'chest0.png')
PILchest = PIL.Image.open(chestname)
Tkchest0 = PIL.ImageTk.PhotoImage(PILchest)
def create_chest0(x,y):
    field.create_image((x*128,y*128), image = Tkchest0, anchor = Tkinter.NW, tags = 'sc')

chestname = os.path.join(directory, 'chest1.png')
PILchest = PIL.Image.open(chestname)
Tkchest1 = PIL.ImageTk.PhotoImage(PILchest)
def create_chest1(x,y):
    field.create_image((x*128,y*128), image = Tkchest1, anchor = Tkinter.NW, tags = 'sc')

## ENEMY ###

## HERO ####

heros = os.path.join(directory, 'hero')
Tkhero = ''
def create_hero(direction,state):
    global Tkhero
    x = str(state) + str(direction) + '.png'
    heroname = os.path.join(heros, x)
    PILhero = PIL.Image.open(heroname)
    Tkhero = PIL.ImageTk.PhotoImage(PILhero)
    field.create_image((256,256), image = Tkhero, anchor = Tkinter.NW, tags = 'sc')

## WALL ####

## DOOR ####

## LOOT ####

def create_map():
    field.delete('sc')
    for y in range(-2,3):
        for x in range(-2,3):
            if x == 0 and y == 0:
                create_hero(heroD,heroS)
            else:
                read_floor()
                temp1 = floor[p_y+y][p_x+x]
                temp2 = lkup[int(temp1)]
                temp3 = temp2 + '(' + str(x+2) + ',' + str(y+2) + ')'
                exec temp3

create_map()

## STATUS DISPLAY ######################

bar = Tkinter.Canvas(root, width = 128*5, height = 128, background = '#FFFFFF')
bar.grid(row = 0, column = 6, columnspan = 5)

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

N = Tkinter.Button(root, width = 10, height = 4, text = 'North', command = moveN)
N.grid(column = 7, row = 1, sticky = 's')

E = Tkinter.Button(root, width = 10, height = 4, text = 'East', command = moveE)
E.grid(column = 8, row = 2, sticky = 'w')

S = Tkinter.Button(root, width = 10, height = 4, text = 'South', command = moveS)
S.grid(column = 7, row = 3, sticky = 'n')

W = Tkinter.Button(root, width = 10, height = 4, text = 'West', command = moveW)
W.grid(column = 6, row = 2, sticky = 'e')

A = Tkinter.Button(root, width = 10, height = 4, text = 'Act')
A.grid(column = 7, row = 2)

## WHATEVER ############################

root.mainloop()