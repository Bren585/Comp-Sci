def add_percent(total,percent):
    '''adds (percent) of (total) to (total)'''
    add = percent*.01*total
    print total + add
    
def hyp():
    '''Finds Hypotenuse (C) given sides (A) and (B)'''
    a = int(raw_input('A='))
    b = int(raw_input('B='))
    c = (a**2.+b**2)**.5
    print 'C='+str(c)
    
def cirArea():
    '''Finds area (A) of a circle given radius (R)'''
    r = int(raw_input('R='))
    a = 3.14*(r**2)
    print 'A='+str(a)
    
def cirCir():
    '''Finds circumfrence (C) given raidus (R)'''
    r = int(raw_input('R='))
    c = 6.28*r
    print 'C='+str(c)
    
def grade():
    '''Finds the Letter Grade given points out of points possible'''
    d = float(raw_input('Points Possible: '))
    n = float(raw_input('Points: '))
    g = n/d * 100
    if g < 60:
        l = 'F'
    else:
        if g < 70: 
            l = 'D'
        else:
            if g < 80:
                l = 'C'
            else:
                if g < 90:
                    l = 'B'
                else:
                    if g <100:
                        l = 'A'
                    else:
                        l= 'A+'
    print 'Grade: '+str(l)
    
def most(n):
    '''Finds the largest number in a group of numbers given the length of the list (n)'''
    x = 0
    s = []
    m = 0
    while n > x:
        x = x+1
        z = raw_input('Number '+str(x)+ ': ')
        s.append(z)
        if z > m:
            m = z
    print 'Given group '+ str(s) +', the largest number is ' +str(m)

import random
def ranl():
    '''Picks a random letter out of a name'''  
    name = raw_input('Name: ')
    l = name[random.randint(0, len(name)-1)]
    print "'" + l + "'"