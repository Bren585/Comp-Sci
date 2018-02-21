import Tkinter
import random

root = Tkinter.Tk()

### VARIABLES ############################################################

wordBank = ['HELLO', 'BOY', 'FRIEND', 'BALLOON', 'ENVELOPE','BURRITO','SAUCE','SOS','TACO','JAZZ','WEDNESDAY','DANCE','MEME','COOL','NUMBER','HANGMAN', 'CLOCK', 'COMPUTER', 'CHAIR', 'FLAG', 'MARKER', 'KEYBOARD', 'DOOR', 'WINDOW']
g = ''
strikes = 0
hidden_word = ''
show = []
lst = []
wrng = []
win = False

### GUI COMP #############################################################

canvas = Tkinter.Canvas(root, width = 100, height = 150, background = '#bababa')
canvas.grid(row=0 ,column=2)

inp = Tkinter.Entry(root, width = 50)
inp.grid(row=1 ,column=1, columnspan = 1, rowspan = 2)

def guess():
    global g
    global win
    global strikes
    global lst
    global show
    if not win and strikes <= 6:
        g = inp.get()
        inp.delete(0, Tkinter.END)
        test(g)
        lst.append(g)
        update()
    else:
        for x in range(0,len(show)):
            show[x] = True
        update()

inpButn = Tkinter.Button(root, height = 1, width = 10, text = 'Enter', command = guess)
inpButn.grid(row = 1, column = 0, rowspan = 2)

inc = Tkinter.Text(root, width = 10, height = 10)
inc.grid(row=0 ,column=0)

word = Tkinter.Text(root, width = 12, height = 1, font = ('comic sans MS', 30))
word.grid(row=0 ,column=1)

### ART ####################################################################

frame = [
canvas.create_rectangle(74,13,82,102, fill = '#000000'),
canvas.create_rectangle(31,9,85,15, fill = '#000000')
]

man = [
"canvas.create_oval(40,17,58,35, fill = '#000000')",
"canvas.create_rectangle(47,32,51,72, fill = '#000000')",
"canvas.create_polygon(28,31,49,43,47,46,28,39)",
"canvas.create_polygon(50,42,68,32,70,34,51,46)",
"canvas.create_polygon(46,69,50,72,42,95,38,93)",
"canvas.create_polygon(48,72,51,69,59,93,55,94)"
]

### ENGINE #################################################################

def init():
    global hidden_word
    global show
    hidden_word = random.choice(wordBank)
    for x in range(0,len(hidden_word)):
        show.append(False)
    update()

def test(g):
    global final
    global win
    global strikes
    global show
    if lst.count(g) == 0:
        if hidden_word.count(g) > 0 and len(g) == 1:
            for x in range(0,len(hidden_word)):
                if hidden_word[x] == g:
                    show[x] = True
        elif len(g) >= 2 and hidden_word == g:
            show = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            update()
            win = True
        else:
            wrng.append(g)
            strikes += 1

def update():
    global win
    if strikes <= 6:
        wintest = True
        for x in range(0, len(show)):
            if not x:
                wintest = False
        if wintest:
            win = True
    if win:
        print 'hi'
        inc.delete(1.0, Tkinter.END)
        inc.insert(Tkinter.END, 'You win!\n')
        inc.insert(Tkinter.END, 'Game is Over')
    wDisp()
    mDisp()
    iDisp()
    

def mDisp():
    global strikes
    global thanks
    if not win and strikes <= 6:
        for x in range(0,strikes):
            exec man[x]

def wDisp():
    d = ''
    for x in range(0,len(hidden_word)):
        if show[x]:
            d += hidden_word[x]
        else:
            d += '_'
    word.delete(1.0, Tkinter.END)
    word.insert(Tkinter.END, str(d))

def iDisp():
    inc.delete(1.0, Tkinter.END)
    for x in range(0,len(wrng)):
        inc.insert(Tkinter.END, wrng[x] + ', ')

init()
root.mainloop()