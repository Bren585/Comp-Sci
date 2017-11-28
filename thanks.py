import random
import matplotlib.pyplot as plt
import time
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Frequency = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, .150, 1.974, .074]

def hundred_roll():
    y = []
    for x in range(100):
        y += [random.randint(1,6) + random.randint(1,6)]
    plt.hist(y)
    plt.show()


def dice_total():
    z = int(raw_input('Number of dice: '))
    y = 0
    for x in range(z):
        y += random.randint(1,6)
    print 'Total = ' + str(y)
    
def AIGuess():
    x = float(random.randint(0,99999))
    x = x/1000
    t = 0
    guess = 0
    while t <= x:
        t += Frequency[guess]
        if x > t:
            guess += 1
    return Alphabet[guess]
    
def hangman():
    wordList = ['sos', 'meme', 'potato']
    print "Lets play hangman!"
    print "Do you want to guess or pick a word?"
    print 'Type "g" to guess or "p" to pick.'
    x = raw_input()
    if x == 'g':
        print "Okay!"
        print "Let me pick a word..."
        time.sleep(1)
        print "Hmmm..."
        time.sleep(1)
        print "Got a word!"
        word = wordList[random.randint(0,len(wordList) - 1)]
        result = 0
        guessed = []
        strikes = 0
        while result == 0:
            display = ''
            for y in word:
                if y == ' ':
                    display += ' '
                elif guessed.count(y) > 0:
                    display += y
                else:
                    display += '_'
            print display
            if strikes >= 6:
                print 'Dang! You lose. The word was "%s."' % (word)
                result = 1
            elif display.count('_') == 0:
                print "You win!"
                result = 1
            else:
                print str(strikes) + '/6 strikes!'
                curr = raw_input('Your Guess: ')
                if guessed.count(curr) == 0:
                    guessed.append(curr)
                    if word.count(curr) == 0:
                        print "Nope!"
                        strikes += 1
                elif guessed.count(curr) >= 1:
                    print "You already guessed that!"
    elif x == 'p':
        print "Now pick a word!"
        print "(I promise I won't look)"
        word = raw_input('Word: ')
        print "Now watch me go!"
        result = 0
        guessed = []
        strikes = 0
        while result == 0:
            display = ''
            for y in word:
                if y == ' ':
                    display += ' '
                elif guessed.count(y) > 0:
                    display += y
                else:
                    display += '_'
            print display
            if strikes >= 6:
                print 'Dang! I lose.'
                result = 1
            elif display.count('_') == 0:
                print "I win!"
                result = 1
            else:
                print str(strikes) + '/6 strikes!'
                curr = AIGuess()
                print 'I guess "%s!"' % (curr)
                if guessed.count(curr) == 0:
                    guessed.append(curr)
                    if word.count(curr) == 0:
                        print "Dang! Guessed wrong."
                        strikes += 1
                elif guessed.count(curr) >= 1:
                    print "I already guessed that!"
                    
def GuessGame():
    print "I've picked a number 1-100. Can you guess it?"
    num = random.randint(1,100)
    t = 0
    g = 0
    meme = 0
    while g != num:
        t += 1
        g = int(raw_input('Guess #%d: ' % (t)))
        if g != num:
            if g <= num:
                print "Higher"
                meme = 0
            elif g >= num:
                if meme >= 3:
                    print "Lower you idiot! That means DOWN."
                else:
                    print "Lower"
                meme += 1
    print "Good Job! The number was %d" % (num)