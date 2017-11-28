import time
commands = ['use', 'look', 'grab', 'drop', 'go']
command_index = ['use(item)', 'look(item)', 'grab(item)', 'drop(item)', 'go(item)']
usable = ['thing', 'nothing', 'key', 'lock', 0]
using_index = ["print 'thing used'", "print '...how'", "if ram[start_bound] == 'door' and holding == 'key': print 'The door is unlocked'; alocations.append('door') \nelse: print'where?'", 'print "It is a three digit numerical lock"\nif int(raw_input("Code: ")) == 314: print("The lock is open"); usable.remove(0); usable.insert(4,"box"); usable.remove("lock"); usable.insert(3, 0)\nelse: print "Wrong code"', 'print "The box is open"; grabbable.remove(0); grabbable.insert(2,"key")']
lookable = ['thing', 'nothing', 'room', 'key', 'door', 'lock', 'box', 'writing', 'wall']
looking_index = ["print 'it is a thing'", "print 'there is nothing there'",'print "It is a room. There is a key in a box in the middle of the room."\nprint "There is a locked door at then end of the room. There is writing on the left wall"', 'print "It is a key. It goes to the door"','print "It is a locked door"', 'print "It is a three digit numerical lock"', 'print "It has a lock. You can see a key inside"','print "The writing reads:"\nprint ""\nprint "The number of riddles"\nprint "the number of Llamas"\nprint "The number of losses taken here"', 'print "The writing reads:"\nprint ""\nprint "The number of riddles"\nprint "the number of Llamas"\nprint "The number of losses taken here"']
grabbable = ['thing', 'nothing', 0,]
grabbing_index = ["print 'You grabbed the thing'","print 'You grabbed nothing'", 'print "You grabbed the key"']
locations = ['room', 'nope', 'door']
alocations = ['room']
holding = 'nothing'
location = 'room'
play = True
story_sequence = True
story_progress = 0

ram = [[ ],[ ],[ ]]
start_bound = 0
end_bound = 0
x = 0
y = [ ]
ram_location = 0
def wram(data):
    global ram_location
    x = 0
    while x < len(ram):
        y = ram[x]
        if y == [ ]:
            ram.pop(x)
            ram.insert(x, data)
            ram_location = x
            x = 254
        x = x + 1
    if x >= len(ram) and x != 255 :
        ram.append(data)
        
def cram():
    x = 0
    while x < len(ram):
        ram.pop(x)
        ram.insert(x,'[ ]')
        x = x + 1
    
def use(item):
    if not usable.count(str(item)) == 0:
        code = using_index[usable.index(item)]
        exec(code)
    else:
        print 'You cannot use that'

def look(item):
    if item == 'around':
        code = looking_index[lookable.index(location)]
        exec(code)
    elif not lookable.count(str(item)) == 0:
        code = looking_index[lookable.index(item)]
        exec(code)
    else:
        print 'You cannot look at that'

def grab(item):
    global holding
    if holding == 'nothing':
        if not grabbable.count(str(item)) == 0:
            code = grabbing_index[grabbable.index(item)]
            exec(code)
            holding = item
        else:
            print 'You cannot grab that'
    else:
        print 'You are already holding ' + holding
            
def drop(item):
    global holding
    if holding == item:
        print 'You dropped ' + holding
        holding = 'nothing'
    elif item == 'holding' or item == 'held':
        print 'You dropped ' + holding
        holding = 'nothing'
    else:
        print "You aren't holding that"
        
def go(item):
    global location
    global play
    global story_sequence
    if not locations.count(str(item)) == 0:
        if not alocations.count(str(item)) == 0:
            if not location == item:
                if item == 'door':
                    story_sequence = True
                else:
                    print 'Arrived at ' + item
                    location = item
            else:
                print 'You are already there'
        else: 
            print 'You cannot go there yet'
    else:
        print 'You cannot go there'

story = [
['Welcome, Friend', 'I call you "friend" because you are a Llama', '(and Llamas are friendly)', 'Anyway, you should probably get out of this room', "('cuz you're a Llama)",'You should start by taking a "look around"', '***TYPE "help" FOR HELP***', '***TYPE "exit" TO QUIT***']
,['','You open the door.', 'You step outside into the fresh air.', 'You have never felt so alive', 'Go eat some grass Llama, you deserve it', 'Good job, Llama. Good job.', '', '' ,'---------FIN---------', 'Thanks for playing!', '    -Brendan, lead designer']
]

help = [
'Input commands using the "terminal"',
'Commands consist of two parts: "Command" and "Item"',
'To issue a command, first type the command word',
'Then, type the item(s) you wish to affect',
'always type in lower case',
'',
'example: "grab thing"'
]

while play:
    if  story_sequence:
        x = 0
        curr_story = story[story_progress]
        while x < len(curr_story):
            print curr_story[x]
            time.sleep(.1)
            x = x + 1
        story_progress = story_progress + 1
        story_sequence = False
    if story_progress == len(story):
        break
    player = str(raw_input('Terminal: '))
    if player == 'exit':
        play = False
        break
    elif player == 'holding':
        print 'you are holding ' + holding
    elif player == 'location':
        print 'you are at ' + location
    else:
        split = player.split()
        if  len(split) >= 2:
            command = str(split[0])
            item = str(split[1])
            x = 0
            while x < (len(split) - 2):
                wram(split[x + 2])
                start_bound = ram_location - (len(split) - 3)
                end_bound = ram_location
                x = x + 1
            if not commands.count(command) == 0:
                exec command_index[commands.index(command)]
            else:
                print 'You cannot do that here'
        else:
            if player == 'help':
                x = 0
                while x < len(help):
                    print help[x]
                    time.sleep(.1)
                    x = x + 1
            else:
                print '...what?'