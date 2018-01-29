import Tkinter
import PIL.Image, PIL.ImageTk

root = Tkinter.Tk()

red_intvar = Tkinter.IntVar()
red_intvar.set(127)

green_intvar = Tkinter.IntVar()
green_intvar.set(127)

x = 150
y = 150
r = 100

def color_changed(new_intval):
    red = hex(red_slider.get())[2:]
    green = hex(green_slider.get())[2:]
    

red_slider = Tkinter.Scale(root, from_=0, to=255, variable=red_intvar, 
                           orient=Tkinter.HORIZONTAL, 
                           label='Red', command=color_changed)
red_slider.grid(row=1, column=0, sticky=Tkinter.E)

green_slider = Tkinter.Scale(root, from_=0, to=255, variable=green_intvar, 
                             orient=Tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=Tkinter.E)

text = Tkinter.Label(root, text='Drag slider \n to adjust \n red.')
text.grid(row=0, column=0)

canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

red = red_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='#000000', fill='#00FFFF')

root.mainloop()