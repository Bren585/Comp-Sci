import random
import os
import PIL
import matplotlib.pyplot as plt

def quickMaths(x,y):
    '''Runs multiple calculations on given x and y'''
    for op in ['+','-','*','/','%']:
        e = 'p = ' + str(x) + op + str(y)
        exec e
        print str(x),op,str(y),'=', p

def luckyNumber():
    '''Will guess your lucky number, given 10'''
    print 'First, I need numbers to guess from.'
    l = []
    for x in range(0,10):
        l.append(raw_input('Number %s: ' % str(x + 1)))
    print 'Is your number %s?' % random.choice(l)
    if raw_input('Y/N: ') == 'Y':
        print 'Cool!'
    else:
        print 'Dang.'
        
directory = os.path.dirname(os.path.abspath(__file__))

loss = PIL.Image.open(os.path.join(directory, 'loss.png'))
comp = PIL.Image.open(os.path.join(directory, 'comp.jpg'))
p5 = PIL.Image.open(os.path.join(directory, 'p5.png'))
caster = PIL.Image.open(os.path.join(directory, 'caster.png'))
foxtail = PIL.Image.open(os.path.join(directory, 'foxtail.jpg'))
edgy = PIL.Image.open(os.path.join(directory, 'edgy-0.png'))

loss = loss.resize((920,570))
p5 = p5.resize((2000,1000))
edgy = edgy.resize((1264,1112))
caster = caster.resize((400,500))
foxtail = foxtail.resize((1520,480))

comp.paste(loss,(2120,640), mask = loss)
comp.paste(p5,(0,2023), mask = p5)
comp.paste(edgy,(2886,2088))
comp.paste(caster,(1540,1130), mask = caster)
comp.paste(foxtail,(4024-1520,0))

fig,ax = plt.subplots(1)
ax.imshow(comp, interpolation = 'none')
fig.show()