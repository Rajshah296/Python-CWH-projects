# Create a program for number guessing game.
# Computer should take a random number as a number to be guessed and user will try to guess the number in a limited number of guesses. On each guess, Computer will provide user with the information whether the input given by user is  > or <  random number.If user guesses before he/she runs out of guesses, he/she wins.

import random
print("Welcome to the Guess the number game. This was developed by Raj Shah.\n\nYou will get only 5 chances to guess the number.")
while(1) : 
    random_num = random.randint(1,100)
    print(random_num)
    number_of_guesses = 0
    while(number_of_guesses < 5) : 
        guess = int(input("\nCome on human, take a guess : "))
        if random_num == guess : 
            print("Wow Human, you turned out to be smarter than I expected.\nYou took ",number_of_guesses + 1," guesses .")
            break
        else: 
            print("\nThe random number is bigger than input."if guess < random_num else "\nThe random number is smaller than input.")
            print(5 - (number_of_guesses+1)," guesses left")
        number_of_guesses+=1
    if number_of_guesses >= 5 : 
        print("Game over, Tumse na ho payega Manav.\nThe secret  number  was ",random_num)
    choice  = input("Press N for exit or any other key for continuing to play :  ")
    if choice == "N" : 
        print("Thanks for playing.")
        break