import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL

directory = os.path.dirname(os.path.abspath(__file__))


comp = PIL.Image.open(u'c:\\Users\\fhsplab\\Desktop\\Comp-Sci\\Dra.png')


fig,ax = plt.subplots(1)
ax.imshow(comp, interpolation = 'none')
fig.show()
