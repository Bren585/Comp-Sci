# ciphers.py
''' ciphers.py provides a function for working with ciphers.
'''

def rotate(string,n):
    '''Returns the ciphertext of string after it has been shifted n letters.
    
    Works on both upper and lower case letters. Other characters are unchanged.
    '''    
    output=''
    for character in string:
        #if lower case letter
        if ord('a')<=ord(character)<=ord('z'): 
            new_ord = ord(character) + n # shift by n
            if new_ord>ord('z'): # wrap around the alphabet to the right
                new_ord -= 26
            if new_ord<ord('a'): #wrap around the alphabet to the left
                new_ord += 26 
            output += chr(new_ord)
        #if upper case letter
        elif ord('A')<=ord(character)<=ord('Z'): 
            new_ord = ord(character) + n # shift by n
            if new_ord>ord('Z'): # wrap around the alphabet to the right
                new_ord -= 26
            if new_ord<ord('A'): #wrap around the alphabet to the left
                new_ord += 26
            output += chr(new_ord)
        else: #not a letter
            output += character
    return output

def try_all_25(string):
    ''' Use brute force to crack a Caesar-like cipher,
        printing all 25 possible shifts
    '''
    for i in range(0,26):
        print rotate(string,i)