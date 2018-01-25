from Tkinter import *
import os.path
import PIL.Image, PIL.ImageTk

root = Tk()

canvas = Canvas(root, height = 600, width = 600, relief = RAISED, bg = 'white')
canvas.grid()

checkbox = canvas.create_rectangle(100, 200, 200, 300, dash = [1,4])
cross = canvas.create_line(100,200,200,300,150,250,100,300,200,200, fill = 'red', width = 20)
message = canvas.create_text(380, 250, text = 'Try this!', font = ('Arial', -100))
shadow = canvas.create_oval(100, 450, 500, 550, fill = '#888888', outline = '#888888')
name = canvas.create_text(300,500, text = 'Brendan K', font = ('Arial', -100))

circles = []
for r in range(10, 60, 10):
    circles.append(canvas.create_oval(300-r, 400-r, 300+r, 400+r, outline='red'))

canvas.itemconfig(circles[2], outline = 'black')
a, b, c, d = canvas.coords(circles[2])
canvas.coords(circles[2],a,b-5,c,d-5)

canvas.itemconfig(circles[0], fill = 'black', width = 3)
a, b, c, d = canvas.coords(circles[0])
canvas.coords(circles[0],a+5,b,c+5,d)

canopy = canvas.create_arc(0, 50, 600, 650, start = 30, extent = 120,
                            width = 50, style = ARC, outline = 'green')

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'canopyIcon.jpg')
img = PIL.Image.open(filename)
img.resize((100,100))
tkimg = PIL.ImageTk.PhotoImage(img)
icon = canvas.create_image((300,50), image = tkimg)

root.mainloop()