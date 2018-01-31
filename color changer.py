import Tkinter
import PIL.Image, PIL.ImageTk

root = Tkinter.Tk()

red_intvar = Tkinter.IntVar()
red_intvar.set(127)

green_intvar = Tkinter.IntVar()
green_intvar.set(127)

blue_intvar = Tkinter.IntVar()
blue_intvar.set(127)

def hexstring(num):
    x = str(hex(num)[2:])
    if len(x) < 2:
        x = '0' + x
    return x

x = 150
y = 150
r = 100

def color_changed(new_intval):
    red = hexstring(red_slider.get())
    green = hexstring(green_slider.get())
    blue = hexstring(blue_slider.get())
    color = '#' + str(red) + str(green) + str(blue)
    canvas.itemconfig(circle_item, fill = color)
    
def printC():
    red = hexstring(red_slider.get())
    green = hexstring(green_slider.get())
    blue = hexstring(blue_slider.get())
    color = '#' + str(red) + str(green) + str(blue)
    out.config(text = color)

red_slider = Tkinter.Scale(root, from_=0, to=255, variable=red_intvar, 
                           orient=Tkinter.HORIZONTAL, 
                           label='Red', command=color_changed)
red_slider.grid(row=1, column=0, sticky=Tkinter.E)

green_slider = Tkinter.Scale(root, from_=0, to=255, variable=green_intvar, 
                             orient=Tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=Tkinter.E)

blue_slider = Tkinter.Scale(root, from_=0, to=255, variable=blue_intvar, 
                             orient=Tkinter.HORIZONTAL,
                             label='Blue', command=color_changed)
blue_slider.grid(row=3, column=0, sticky=Tkinter.E)

text = Tkinter.Label(root, text='Drag sliders \n to adjust \n color.')
text.grid(row=0, column=0)

canvas = Tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0, rowspan=2, column=1)

red = red_intvar.get()
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r,
                                 outline='#000000', fill='#FFFF00')

button = Tkinter.Button(root, text = 'Print Color', command = printC)
button.grid(row=2,column=1)

out = Tkinter.Label(root, text='')
out.grid(row=3,column=1)

root.mainloop()