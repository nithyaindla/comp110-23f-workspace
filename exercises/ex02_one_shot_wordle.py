"""EX02 - One Shot Wordle: Almost the OG Wordle."""

__author__ = "730653507"

#Pre-establishing some variables for later.'''
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
occurance = False
output: str = ""
secret_word = "python"
guess = input("What is your 6-letter guess? ")
i = 0
#Make sure that the guess is 6 letters. Otherwise, make user keep trying.
while len(guess)!= 6:
    guess = input("That was not 6 letters! Try again: ")
#Check each character in guess and compare to the secret word.
while i < 6:
    occurance = False
    #If the guess character matches the secret word character.
    if guess[i] == secret_word[i]:
        output = output + GREEN_BOX
        occurance = True
    else:
        #If the guess character does not match secret word character, but matches a secret word character at a different index.
        x = 0
        while x < 6:
            if guess[i] == secret_word[x]:
                output = output + YELLOW_BOX
                occurance = True    
            x = x + 1
    #If the guess character is just not in the secret word at all.
    if occurance == False:
       output = output + WHITE_BOX        
    #Move to the next character in the guess word and repeat.
    i = i + 1
#Prints final pattern of red/white/yellow boxes.
print(output)
#Prints if user gets the word correct.
if guess == secret_word:
    print("Woo! You got it!")
#Prints if user gets word wrong.
else:
    print("Not quite. Play again soon!")