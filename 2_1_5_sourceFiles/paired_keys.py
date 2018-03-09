import random
""" paired_keys.py defines 13 functions for understanding RSA encryption.
numerize() and denumerize(),
make_keys() and use_key() are intended to be called in a 
functional programming paradigm. The other functions are helpers.

version 12/3/2013
Unpublished work (c) 2013 Project Lead The Way, Inc.
"""

#####
# Functions for prime numbers
#####

def calculate_primes(minimum, maximum):
    """Return a list of all primes between minimum and maximum
    """
    primes = [2,3,5,7] #initialize the list with the first few primes
    for new_number in range(11,maximum+1,2):
        is_prime=True
        for test_prime in primes:
            if new_number % test_prime == 0:
                is_prime=False
        if is_prime:
            primes.append(new_number)
    min_index = 0
    while primes[min_index]<minimum:
        min_index += 1
    return primes[min_index:]

def factor(a):
    """ Returns a list of factors of a other than 1 and a
    """  
    factors = []
    # Test all numbers from 2 up to square root of a
    for i in range(2, int(a**.5)): 
        if a % i == 0:
            factors.append(i)
            factors.append(a/i) # the other factor in the pair is > a**.5
    # Include the square root if a is a perfect square
    if a % int(a**.5) == 0: 
        factors.append(int(a**.5)) 
    return  sorted(factors)        

def prime_factors(a):
    """ Returns a list of prime factors of a
    """
    prime_factor_list=[]
    #remove the factors of 2
    while a%2==0:
        a=a/2
        prime_factor_list.append(2)
    prime = False
    while prime == False:
        prime=True
        for test in range(3,int(a**.5)+1,2):
            if a%test==0:
                prime_factor_list.append(test)
                a /= test
                prime=False
                break
    prime_factor_list.append(a)
    return prime_factor_list
                
def get_primes(minimum=100, maximum=300):
    """ returns two distinct prime numbers between minimum and maximum
    """
    primes = calculate_primes(minimum, maximum)
    # Pick any two distinct prime numbers
    p = random.choice(primes)
    q = random.choice(primes)
    #keep picking second prime until we have two distinct primes
    while q == p:
        q = random.choice(primes)
    return p, q
    
#####
# Functions for RSA encryption
####

def make_keys_from_primes(p, q):
    """ p and q are distinct prime numbers
    make_keys_from_primes() finds two integers d, e such that (d,pq) and (e,pq) 
    are paired RSA keysreturns two 2-tuples
    """
    # Find n and phi
    # n is part of public and private keys
    # phi is used to find the other part of each key
    n = p * q # n is the modulus; its length is the key length
    eulers_phi = (p-1)*(q-1) # number of positive integers 1 to n-1 relatively prime to n
    
    ####
    # Find d and e, the other parts of the public and private keys  
    # d*e = 1 (mod n)
    # so find a pair of factors d*e = n+1 or 2n+1 or 3n+1 or ...
    ####
    
    product = eulers_phi+1
    d, e = 1, 1
    while d*e == 1:
        factors = factor(product)
        if len(factors)>1: # if there is a pair of factors
            # Remove the squareroot if its among the factors
            # since we need 2 distinct factors
            if int(product**.5)**2 == product: 
                factors.remove(product**.5)
            # Pick one key
            d = random.choice(factors)
            # Get the other key
            e = product/d
        product += eulers_phi # Prepare for next iteration in case this one didn't factor  
    return [(n, d), (n, e)]        
    
def make_keys():
    """Returns a pair of of keys for RSA encryption. 
    Each key is a 2-tuple of (modulus, factor)
    """
    p, q = get_primes()
    d, e = make_keys_from_primes(p, q)
    return d, e

def crypt_number((n, d_or_e), number_message):
    """ crypt_number() transforms a numeric message with the (n, d_or_e) key. 
    This is the inverse operation of using crypt_number() with the other key 
    from the same pair. 
    """
    # Return message ** d mod n
    # To reduce calculate time, compute message ** d one multiplication
    # at a time, taking modulus n each step'
    new_number_message = 1
    for i in range(d_or_e): # exponent d_or_e is counting the number of multiplications.
        new_number_message = (new_number_message * number_message) % n
    return new_number_message 

def use_key((n, d_or_e), number_message, chunk_size=4):
    """ use_key() transforms a message with the (n, d_or_e) key. 
    This is the inverse operation of using use_key() with the other key 
    from the same pair. 
    The message should be a string of digits in groups separated by "-"
    """ 
    output = []
    numbers = number_message.split("-")
    for number in numbers:
        crypted = crypt_number((n, d_or_e), int(number))
        crypted = str(crypted)
        short = chunk_size - len(crypted)
        crypted = "0"*short + crypted
        output.append(crypted)
    return "-".join(output)
    
#####
# Functions for turning a message into numbers and back to letters
#####

def letter_to_number(letter):
    """ Turn one character into a number 01-99
    """
    return ord(letter)-26 # so that all keyboard symbols are 0-99

def letters_to_numberstring(string):
    """ Returns a string of digits from a string of letters,
    two digits per letter
    """
    number=0
    for character in string:
        number *= 100 # Shift the number over two decimal places
        number += letter_to_number(character)
    numberstring = str(number)
    if len(numberstring)%2 == 1: # Odd length indcates single digit at front
        numberstring = "0" + numberstring # Include leading 0 if needed
    return numberstring # Return a string
                           
def numerize(string, chunk_size=2):
    """Turns a string of characters into a string of digits
    Each two decimal digits represents one character
    The string is split into groups of letters, separarated by "-". 
    chunk_size says how many letters are in each group.
    """
    numerized = ""
    # Make the string be a multiple of chunk_size
    extras = len(string) % chunk_size
    if extras != 0:
        string = " "*(chunk_size - extras) + string        
    # Change to numbers one chunk at a time
    while len(string)>0:
        if len(numerized)>0:
            numerized += "-"
        chunk = string[:chunk_size]
        string = string[chunk_size:]
        numerized += letters_to_numberstring(chunk)
    return numerized

def number_to_letter(number):
    """ Turn one number 01-99 into one character
    """
    return chr(number+26)

def denumerize(numberstring):
    """Reverses the effect of numerize(), turning a sequence of two-digit
    numbers into characters, dropping the hyphens between digits.
    """
    string=""
    while len(numberstring)>0:
        if numberstring[0]=="-":
            numberstring = numberstring[1:]
        else:
            try:
                string += number_to_letter(int(numberstring[:2]))
                numberstring = numberstring[2:]
            except:
                print("Oops! Could not parse string. Please check your decryption step.")
                return numberstring
    return string                