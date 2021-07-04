"""Number of guesses =9,print number of guesses left,print number of guesses he/she took to finish game over"""
n = 20
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while number_of_guesses <= 9:
    guesses_number = int(input("Guess the number:\n"))
    if guesses_number < 20:
        print("your number is less number input greater number.\n")
    elif guesses_number > 20:
        print("your number is greater please input smaller number.\n")
    else:
        print("Congress!,You won")
        print(number_of_guesses, "number of guesses he/she took to Finish the game.")
        break
        print(9-number_of_gusses, "number of guesses left")
        number_of_guesses = number_of_guesses + 1
        if number_of_guesses > 9:
            print("Game Over")
