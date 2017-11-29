usable = ['item']
item = 'print(item used)'

def use(item):
    if not usable.count(item) == 0:
        exec item
    else:
        print ('You cannot use that')
        
        
play = True
while play:
    player = raw_input('Terminal: ')