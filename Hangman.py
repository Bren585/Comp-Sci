import Tkinter
import random

root = Tkinter.Tk()

### VARIABLES ############################################################

wordBank = []
final = False
g = ''
strikes = 0
hidden_word = ''
show = []
lst = []
wrng = []
win = False

### GUI COMP #############################################################

man = Tkinter.Canvas(root, width = 100, height = 150, background = '#bababa')
man.grid(row=0 ,column=2)

inp = Tkinter.Entry(root, width = 60)
inp.grid(row=1 ,column=0, columnspan = 2, rowspan = 2)

gType = [
Tkinter.Radiobutton(root, text = 'Letter', variable = final, value = False),
Tkinter.Radiobutton(root, text = 'Final', variable = final, value = True)
]
gType[0].grid(row=1 ,column=2, sticky = 'w')
gType[1].grid(row=2 ,column=2, sticky = 'w')

inc = Tkinter.Text(root, width = 10, height = 10)
inc.grid(row=0 ,column=0)

word = Tkinter.Text(root, width = 40, height = 10, text = '')
word.grid(row=0 ,column=1)

### ART ####################################################################

### ENGINE #################################################################

def init():
    for x in len(word):
        show.append(False)

def test(g):
    global final
    global win
    global strikes
    if final:
        if word == g:
            win = True
        else:
            wrng.append(g)
            strikes += 1
    else:
        if word.count(g) > 0:
            for x in len(word):
                if word[x] == g:
                    show[x] = True
        else:
            wrng.append(g)
            strikes += 1

def update():
    wDisp()
    mDisp()

def mDisp():
    global strikes
    for x in range(0,strikes):
        exec 'art[x]'

def wDisp():
    d = ''
    for x in len(word):
        if show[x]:
            d += word[x]
        else:
            d += '_'
    word.config(text = d)
    

def guess():
    global g
    g = inp.get()
    inp.delete(0, Tkinter.END)
    lst.append(g)
    test(g)
    update()

root.mainloop()