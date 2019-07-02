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
    
  print('Welcome to the game, Hangman!')
  print('I am thinking of a word that is', len(secretWord) , 'letters long.')
    
  print('-----------')
    
  while not endGame:
    
    print('You have', numGuesses , 'guesses left.')
    print('Available letters:', availableLetters)
        
    guess = input('Please guess a letter:').lower()
        
    if guess in lettersGuessed:
        
    print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
    print('-----------')
            
    elif guess in availableLetters:
        
      #insere 
      lettersGuessed += guess

      #atualiza
      availableLetters = getAvailableLetters(lettersGuessed)
           
        if guess in secretWord:
            
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
            endGame = isWordGuessed(secretWord, lettersGuessed)
                
        else:
           
          print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
          print('-----------')
                numGuesses -= 1
                
                if numGuesses == 0:
                
                    endGame = True
        
        else:
    
            print('Invalid letter:')
            
    if numGuesses == 0:
        
        print('Sorry, you ran out of guesses. The word was', secretWord)
            
    else:

        print('Congratulations, you won!')
