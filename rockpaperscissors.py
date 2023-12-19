#ROCK_PAPER_SCISSORS

import random

while True:

    comp = ["rock", "paper", "scissors"]
    comp_choice = random.choice(comp)
    
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    print("You chose " + user_choice + " and Computer chose " + comp_choice)
    
    if comp_choice == user_choice:
        print("Both chose " + user_choice + "! It's a tie!")
    elif comp_choice == "rock":
        if user_choice == "paper":
            print("Paper covers Rock! You win!")
        elif user_choice == "scissors":
            print("Rock smashes Scissors! You lose!")
    elif comp_choice == "paper":
        if user_choice == "scissors":
            print("Scissors cut Paper! You win!")
        elif user_choice == "rock":
            print("Paper covers Rock! You lose!")
    elif comp_choice == "scissors":
        if user_choice == "rock":
            print("Rock smashes Scissors! You win!")
        elif user_choice == "paper":
            print("Scissors cut Paper! You lose!")
            
    again=input("Do you want to play again? (y/n): ")
    if again!= "y":
        break
