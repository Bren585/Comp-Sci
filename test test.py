import PIL.Image, PIL.ImageTk
import numpy as np
import PIL
import matplotlib.pyplot as plt
import os.path

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'p5.png')
img = PIL.Image.open(filename)

fig,ax = plt.subplots(1)
ax.imshow(img, interpolation = 'none')
fig.show()