# Hangman
import getpass
# Player 1 Function
def player1():
    typeword = getpass.getpass("Player 1 Type a word in: ")
    if typeword != "":
        split = list(typeword)
        return split
    else:
        print("Empty value, please try again!")


# Player 2 Function
def player2():
    life = 9
    word = player1()
    unknown_word = "-" * len(word)
    split_word = list(unknown_word)
    print(unknown_word + "\n")
    joined = "".join(word)
    guessed = []

    while life > 0:
        print("Lives: " + str(life) + "\n")
        guess = input("Player 2 Type a letter: ")

        if guess == joined:
            print("You win, The word was: " + joined)
            break

        elif guess in guessed:
            print("The letter is already guessed")
            print("".join(split_word))
            life -= 1

        elif guess in word:
           for i in range(len(word)):
                if any(guess in g for g in word[i]):
                    split_word[i] = word[i]
                else:
                    pass
           print("".join(split_word))
           guessed.append(guess)
        else:
            print("Its not the letter " + guess)
            print("".join(split_word))
            guessed.append(guess)
            life -= 1

        if split_word == word:
            print("You win, The word was: " + joined)
            break

    if life == 0:
        print("Game over! \n The answer was: " + joined)


player2()
