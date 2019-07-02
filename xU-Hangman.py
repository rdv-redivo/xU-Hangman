# Hangman game

import random, string

def loadWords():
   
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')

    line = inFile.readline()

    wordlist = line.split()
    
    print("  ", len(wordlist), "words loaded.")
    
    return wordlist

def chooseWord(wordlist):
  
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    
    for letter in secretWord:
        
        if not (letter in lettersGuessed):
            
            return False
        
        return True


def getGuessedWord(secretWord, lettersGuessed):

    string = ''
    
    for letter in secretWord:
    
        if letter in lettersGuessed:
        
            string += letter
        
        else:
        
            string += '_'
            
    return string

def getAvailableLetters(lettersGuessed):

    string = ''
    
    for letter in string.ascii_lowercase:
        
        if not (letter in lettersGuessed):
            
            string += letter
            
    return string


def hangman(secretWord):
    
    availableLetters = string.ascii_lowercase
    
    lettersGuessed = ''
    
    numGuesses = 8
        
    endGame = False
    
    while not endGame:
    
        guess = input('Guess:').lower()
        
        if guess in lettersGuessed:
        
            print('Duplicated letter:')
            
        elif guess in availableLetters:
        
           #insere
           lettersGuessed += guess
           
           #atualiza
           getAvailableLetters(lettersGuessed)
           
           if guess in secretWord:
           
            endGame = isWordGuessed(secretWord, lettersGuessed)
                
           else:
           
            numGuesses -= 1
        
        else:
        
            print('Invalid letter:')

WORDLIST_FILENAME = "words.txt"

wordlist = loadWords()

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
