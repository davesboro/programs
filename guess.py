def main():
    print("Guess a number between 1 and 100")
    randomNumber = 35
    found = False

    while not found:
        userGuess = input("Your guess is: ")
        if userGuess == randomNumber:
            print("You got it!")
            found = True
        else:
            print("That's not it")



if __name__ == "__main__":
    main()

