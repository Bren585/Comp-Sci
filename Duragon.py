import random

E = [
'Dragon',
[['HP'],[000],[000]],
[['MP'],[000],[000]]
]

name = []
P = [
name + 'The Hero',
[['HP'],[000],[000]],
[['MP'],[000],[000]]
]

menu = [
[[' '],['FIGHT']],
[[' '],['ITEM']],
[[' '],['SPELL']],
]

def display():
    print E[0]+'             '+P[0]
    print E[1]