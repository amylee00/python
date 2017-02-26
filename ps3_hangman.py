# Hangman game
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
    
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
      
    '''
    counter=0
    counter2=0
    result=0
    
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
                counter +=1
                result +=1
        else:
                counter +=1            

    if result==len(secretWord):
        return True
        counter2 +=1
    else:           
        return False
    
#secretWord='apple'
#lettersGuessed=['a','p','d','b','c','e']            
#print(isWordGuessed(secretWord, lettersGuessed))

def isLetterInSecretWord(letter,secretWord):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if a letter is in secretWord, False if not
      
    '''
 
    if letter in secretWord:
            return True
    else:    
            return False

#letter='a'
#secretWord='apple' 
#print(isLetterInSecretWord(letter,secretWord))

        

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    ans=''  #initialise answer list
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
                ans +=str(secretWord[i])
                i +=1

        else:
                ans +=(' _ ')
                i +=1
                
    return ans
                
#secretWord='apple'
#lettersGuessed=['a','p','d','b','c','e']            
#print(getGuessedWord(secretWord, lettersGuessed))
    
def getAlphabet():
    
    import string
    return string.ascii_lowercase
        
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
        
    alphabet=getAlphabet()
    #print(alphabet)    
    letters=''
    #lettersGuessed="".join(lettersGuessed)
    
    for i in range(len(alphabet)):
 
        if alphabet[i] in lettersGuessed:
            letters +=''
            i +=1
        else: 
            letters +=alphabet[i]
            i +=1
            
    return letters           
            
#lettersGuessed=['e','i','k','p','r','s']            
#print(getAvailableLetters(lettersGuessed))    
    
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print('Welcome to Hangman!')
    counter=0
    numberOfGuesses=8
    lettersGuessed=[]
    done=False
    
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print('--------------------------------------')
    
    while counter<numberOfGuesses and done==False:
    
        print('You have '+str(numberOfGuesses-counter)+' guesses left')
        print('Available letters: '+getAvailableLetters(lettersGuessed))
        letter=input('Please guess a letter:')
        letter=letter.lower()
        
        if letter in lettersGuessed:
                print("Oops! You've already guessed that letter:"+getGuessedWord(secretWord, lettersGuessed))
                counter +=0                             
                print('--------------------------------------')
                
        else:        
                lettersGuessed +=letter
                res=isWordGuessed(secretWord, lettersGuessed)
                ans=isLetterInSecretWord(letter,secretWord)
                

                if ans==True:
                        print('Good guess:'+getGuessedWord(secretWord, lettersGuessed))
                        counter +=0 
                        print('--------------------------------------')

                        if res==True:
                            print('Congratulations, you won!')
                            done=True                            
                        else:
                            done=False
                else:
                        print('Oops! That letter is not in my word:'+getGuessedWord(secretWord, lettersGuessed))
                        counter +=1
                        print('--------------------------------------')

    if done==True:
        return 
        
    else:                                   
        print('Sorry, you ran out of guesses. The word was: '+secretWord)                        
                            
#    isWordGuessed(secretWord, lettersGuessed)
#    getAvailableLetters(lettersGuessed)
   
    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
#secretWord='c'
hangman(secretWord)