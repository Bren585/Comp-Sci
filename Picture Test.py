import matplotlib.pyplot as plt
import os.path
import numpy as np

directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'loss.png')
img = plt.imread(filename)

n = int(raw_input('How much loss: '))

fig, ax = plt.subplots(1,n)
for x in range(0,n):
    ax[x].imshow(img, interpolation = 'none')
    print 'i  |i-i'
    print ' ii|i _'
    print ''
fig.show()