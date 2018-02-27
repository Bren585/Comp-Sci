from Tkinter import *
import PIL.Image, PIL.ImageTk
import os.path
import numpy

root = Tk()
directory = os.path.dirname(os.path.abspath(__file__))

## DISPLAY #####################################################################
################################################################################

## MAP ################################

field = Canvas(root,width = 128*5, height = 128*5, background = '#000000')
field.grid(row=0,column=0,rowspan = 5, columnspan = 5)

lkup = ['null','create_tile','create_chest0','create_chest1']

fnum = 0
floor = []

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

p_x, p_y = 2 , 2

## EMPTY ###

def null(x,y):
    x = y

## TILE ####

tilename = os.path.join(directory, 'tile.png')
PILtile = PIL.Image.open(tilename)
bTile = PILtile
Tktile = PIL.ImageTk.PhotoImage(PILtile)
def create_tile(x,y):
    field.create_image((x*128,y*128), image = Tktile, anchor = NW)

## CHEST ###

chestname = os.path.join(directory, 'chest0.png')
PILchest = PIL.Image.open(chestname)
Tkchest0 = PIL.ImageTk.PhotoImage(PILchest)
def create_chest0(x,y):
    field.create_image((x*128,y*128), image = Tkchest0, anchor = NW)

chestname = os.path.join(directory, 'chest1.png')
PILchest = PIL.Image.open(chestname)
Tkchest1 = PIL.ImageTk.PhotoImage(PILchest)
def create_chest1(x,y):
    field.create_image((x*128,y*128), image = Tkchest1, anchor = NW)

## ENEMY ###

## HERO ####

## WALL ####

## DOOR ####

## LOOT ####

def create_map():
    for y in range(-2,3):
        for x in range(-2,3):
            read_floor()
            temp1 = floor[p_y+y][p_x+x]
            temp2 = lkup[int(temp1)]
            temp3 = temp2 + '(' + str(x+2) + ',' + str(y+2) + ')'
            exec temp3

create_map()

## STATUS DISPLAY ######################

## CONTROL PAD #########################

## WHATEVER ############################

root.mainloop()