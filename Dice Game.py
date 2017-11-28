import random
import time
log = []
Win = ('You Win!', 'Congrats!', 'A victor is you!', 'Terrific!')
Lose = ('Aww, too bad.' 'Better luck next time!', "That's unlucky.", "#blamesos")

print ('------DICE GAME------')
print ('      by Brendan     ')
print ('                     ')
print ('Welcome to Dice Game!')
print ('Dice Game is very    ')
print ('simple. Just type    ')
print ('"roll" to roll three ')
print ('dice. If all three   ')
print ('unique, you win! Type')
print ('"log" to see your    ')
print ('roll history, and    ')
print ('"exit" to exit!      ')

while True:
    command = raw_input()
    if command == 'roll':
        print "Here we go!"
        time.sleep(.2)
        print "Roll one..."
        time.sleep(2)
        x = random.randint(1,6)
        print str(x) + '!'
        time.sleep(1)
        print "Roll two..."
        time.sleep(2)
        y = random.randint(1,6)
        print str(y) + '!'
        time.sleep(1)
        print "Roll three..."
        time.sleep(2)
        z = random.randint(1,6)
        print str(z) + '!'
        time.sleep(1)
        if x != y and y != z and z != x:
            r = random.randint(0,3)
            print Win[r]
            r = 'Win'
        else:
            r = random.randint(0,3)
            print Lose[r]
            r = 'Lose'
        log.append([x, y, z, r])
    elif command == 'log':
        w = 0
        while w < len(log):
            n = log[w]
            print str(w + 1) + ": " + str(n[0]) + ", " + str(n[1]) + ", " + str(n[2]) + ", " + str(n[3])
            w = w + 1
    elif command == 'exit':
        print 'Goodbye!'; break
    else:
        print ("I'm sorry, I don't  ")
        print ("recognize that      ")
        print ('command. Type "exit"')
        print ('to exit.')