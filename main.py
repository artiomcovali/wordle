
import random
from words import words

wordleWords = []

aletter1 = ""
aletter2 = ""
aletter3 = ""
aletter4 = ""
aletter5 = ""

history = []


# picks a 5 letter word
for x in range(len(words)):
    if len(words[x]) == 5:
        wordleWords.append(words[x])

print("Welcome to Wordle!")

print("""
- - - - -
- - - - -
- - - - -
- - - - -
- - - - -
- - - - -
""")

def game():
    guesses = 6
    win = False
    word = random.choice(wordleWords)
    word = word.upper()
    userWord = ""

    while win == False and guesses > 0:   
        userWord = input("\033[1;39mGuess a word: ").upper()

        if len(userWord) < 5 or len(userWord) > 5:
            print("Please enter a 5 letter word.")
            userWord = input("\033[1;39mGuess a word: ").upper()

        print(" ")
        guesses = guesses - 1

        # checks if first letter is in the word
        if userWord[0] == word[0]:
            aletter1 = "\033[1;32m" + userWord[0]
        elif userWord[0] == word[1]:
            aletter1 = "\033[1;33m" + word[1]
        elif userWord[0] == word[2]:
            aletter1 = "\033[1;33m" + word[2]
        elif userWord[0] == word[3]:
            aletter1 = "\033[1;33m" + word[3]
        elif userWord[0] == word[4]:
            aletter1 = "\033[1;33m" + word[4]
        else:
            aletter1 = "\033[1;37m" + userWord[0]

        history.append(aletter1)


        # checks if second letter is in the word
        if userWord[1] == word[1]:
            aletter2 = "\033[1;32m" + word[1]
        elif userWord[1] == word[0]:
            aletter2 = "\033[1;33m" + word[0]
        elif userWord[1] == word[2]:
            aletter2 = "\033[1;33m" + word[2]
        elif userWord[1] == word[3]:
            aletter2 = "\033[1;33m" + word[3]
        elif userWord[1] == word[4]:
            aletter2 = "\033[1;33m" + word[4]
        else:
            aletter2 = "\033[1;37m" + userWord[1]

        history.append(aletter2)

        # checks if third letter is in the word
        if userWord[2] == word[2]:
            aletter3 = "\033[1;32m" + word[2]
        elif userWord[2] == word[0]:
            aletter3 = "\033[1;33m" + word[0]
        elif userWord[2] == word[1]:
            aletter3 = "\033[1;33m" + word[1]
        elif userWord[2] == word[3]:
            aletter3 = "\033[1;33m" + word[3]
        elif userWord[2] == word[4]:
            aletter3 = "\033[1;33m" + word[4]
        else:
            aletter3 = "\033[1;37m" + userWord[2]

        history.append(aletter3)

        # checks if fourth letter is in the word
        if userWord[3] == word[3]:
            aletter4 = "\033[1;32m" + word[3]
        elif userWord[3] == word[0]:
            aletter4 = "\033[1;33m" + word[0]
        elif userWord[3] == word[1]:
            aletter4 = "\033[1;33m" + word[1]
        elif userWord[3] == word[2]:
            aletter4 = "\033[1;33m" + word[2]
        elif userWord[3] == word[4]:
            aletter4 = "\033[1;33m" + word[4]
        else:
            aletter4 = "\033[1;37m" + userWord[3]

        history.append(aletter4)
        
        # checks if fifth letter is in the word
        if userWord[4] == word[4]:
            aletter5 = "\033[1;32m" + word[4]
        elif userWord[4] == word[0]:
            aletter5 = "\033[1;33m" + word[0]
        elif userWord[4] == word[1]:
            aletter5 = "\033[1;33m" + word[1]
        elif userWord[4] == word[2]:
            aletter5 = "\033[1;33m" + word[2]
        elif userWord[4] == word[3]:
            aletter5 = "\033[1;33m" + word[3]
        else:
            aletter5 = "\033[1;37m" + userWord[4]

        history.append(aletter5)


        if guesses == 5:
            print(history[0] + ' ' + history[1] + ' ' + history[2] + ' ' + history[3] + ' ' + history[4] + 
            "\033[1;39m" + "\n- - - - -\n- - - - -\n- - - - -\n- - - - -\n- - - - -\n")
        elif guesses == 4:
            print(history[0] + ' ' + history[1] + ' ' + history[2] + ' ' + history[3] + ' ' + history[4] + 
            "\n" + history[5] + ' ' + history[6] + ' ' + history[7] + ' ' + history[8] + ' ' + history[9] + 
            "\033[1;39m" + "\n- - - - -\n- - - - -\n- - - - -\n- - - - -\n")
        elif guesses == 3:
            print(history[0] + ' ' + history[1] + ' ' + history[2] + ' ' + history[3] + ' ' + history[4] + 
            "\n" + history[5] + ' ' + history[6] + ' ' + history[7] + ' ' + history[8] + ' ' + history[9] + 
            "\n" + history[10] + ' ' + history[11] + ' ' + history[12] + ' ' + history[13] + ' ' + history[14] + 
            "\033[1;39m" + "\n- - - - -\n- - - - -\n- - - - -\n")
        elif guesses == 2:
            print(history[0] + ' ' + history[1] + ' ' + history[2] + ' ' + history[3] + ' ' + history[4] + 
            "\n" + history[5] + ' ' + history[6] + ' ' + history[7] + ' ' + history[8] + ' ' + history[9] + 
            "\n" + history[10] + ' ' + history[11] + ' ' + history[12] + ' ' + history[13] + ' ' + history[14] + 
            "\n" + history[15] + ' ' + history[16] + ' ' + history[17] + ' ' + history[18] + ' ' + history[19] + 
            "\033[1;39m" + "\n- - - - -\n- - - - -\n")
        elif guesses == 1:
            print(history[0] + ' ' + history[1] + ' ' + history[2] + ' ' + history[3] + ' ' + history[4] + 
            "\n" + history[5] + ' ' + history[6] + ' ' + history[7] + ' ' + history[8] + ' ' + history[9] + 
            "\n" + history[10] + ' ' + history[11] + ' ' + history[12] + ' ' + history[13] + ' ' + history[14] + 
            "\n" + history[15] + ' ' + history[16] + ' ' + history[17] + ' ' + history[18] + ' ' + history[19] + 
            "\n" + history[20] + ' ' + history[21] + ' ' + history[22] + ' ' + history[23] + ' ' + history[24] + 
            "\033[1;39m" + "\n- - - - -\n")
        elif guesses == 0:
            print(history[0] + ' ' + history[1] + ' ' + history[2] + ' ' + history[3] + ' ' + history[4] + 
                "\n" + history[5] + ' ' + history[6] + ' ' + history[7] + ' ' + history[8] + ' ' + history[9] + 
                "\n" + history[10] + ' ' + history[11] + ' ' + history[12] + ' ' + history[13] + ' ' + history[14] + 
                "\n" + history[15] + ' ' + history[16] + ' ' + history[17] + ' ' + history[18] + ' ' + history[19] + 
                "\n" + history[20] + ' ' + history[21] + ' ' + history[22] + ' ' + history[23] + ' ' + history[24] + 
                "\n" + history[25] + ' ' + history[26] + ' ' + history[27] + ' ' + history[28] + ' ' + history[29])


            


        if userWord == word:
            win = True

    
    tries = 6 - guesses

    if userWord == word:
        print("\033[1;32m" + "Congrats you guessed the word in " + str(tries) + " tries!" + "\033[1;39m")
        quit

    if guesses == 0:
        print("\033[1;31m" + "\nSorry you ran out of guesses. The word was " + word + "\033[1;39m")
        quit

game()


