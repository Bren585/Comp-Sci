import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL

directory = os.path.dirname(os.path.abspath(__file__))

loss = PIL.Image.open(os.path.join(directory, 'loss.png'))
comp = PIL.Image.open(os.path.join(directory, 'comp.jpg'))

loss = loss.resize((920,570))
comp.paste(loss,(2120,640))

fig,ax = plt.subplots(1)
ax.imshow(comp, interpolation = 'none')
fig.show()
