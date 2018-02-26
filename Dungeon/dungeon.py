from Tkinter import *
import PIL.Image, PIL.ImageTk
import os.path

root = Tk()

## DISPLAY #####################################################################
################################################################################

## MAP ################################

field = Canvas(root,width = 128*5, height = 128*5, background = '#000000')
field.grid(row=0,column=0,rowspan = 5, columnspan = 5)

lkup = ['null','create_tile']

fnum = 0
floor = []

def read_floor():
    fname = 'F' + str(fnum) + '.txt'
    with open(fname) as f:
        for y in f:
            row = []
            for x in y:
                if x != '\n':
                    row.append(x)
            floor.append(row)

p_x, p_y = 2 , 2

## TILE ####

directory = os.path.dirname(os.path.abspath(__file__))
tilename = os.path.join(directory, 'tile.png')
PILtile = PIL.Image.open(tilename)
Tktile = PIL.ImageTk.PhotoImage(PILtile)
def create_tile(x,y):
    field.create_image((x*128,y*128), image = Tktile, anchor = NW)

## CHEST ###

## ENEMY ###

## HERO ####

## WALL ####

## DOOR ####

## LOOT ####

def create_map():
    for x in range(-2,3):
        for y in range(-2,3):
            read_floor()
            temp1 = floor[p_x+x][p_y+y]
            temp2 = lkup[int(temp1)]
            temp3 = temp2 + '(' + str(x+2) + ',' + str(y+2) + ')'
            exec temp3

create_map()

## STATUS DISPLAY ######################

## CONTROL PAD #########################

## WHATEVER ############################

root.mainloop()