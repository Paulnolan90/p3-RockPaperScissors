import random
import time

class RockPaperScissors:
    def __init__(self):
        self.user_wins = 0  # counts the wins from the user
        self.computer_wins = 0  # counts the wins from the computer
        self.random_number = random.randint(0, 2)  # randomly generates number.
        self.options = ["rock", "paper", "scissors"]  # creates a variable

    def play(self):
        print("""            ░█████╗░░█████╗░███╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ██████╗░███████╗░█████╗░████████╗
            ██╔══██╗██╔══██╗████╗░██║  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
            ██║░░╚═╝███████║██╔██╗██║  ░╚████╔╝░██║░░██║██║░░░██║  ██████╦╝█████╗░░███████║░░░██║░░░
            ██║░░██╗██╔══██║██║╚████║  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══██╗██╔══╝░░██╔══██║░░░██║░░░
            ╚█████╔╝██║░░██║██║░╚███║  ░░░██║░░░╚█████╔╝╚██████╔╝  ██████╦╝███████╗██║░░██║░░░██║░░░
            ░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░

            ░█████╗░██╗░░░██╗██████╗░  ░██████╗██╗░░░██╗██████╗░███████╗██████╗░  ░██████╗███╗░░░███╗░█████╗░██████╗░████████╗
            ██╔══██╗██║░░░██║██╔══██╗  ██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗  ██╔════╝████╗░████║██╔══██╗██╔══██╗╚══██╔══╝
            ██║░░██║██║░░░██║██████╔╝  ╚█████╗░██║░░░██║██████╔╝█████╗░░██████╔╝  ╚█████╗░██╔████╔██║███████║██████╔╝░░░██║░░░
            ██║░░██║██║░░░██║██╔══██╗  ░╚═══██╗██║░░░██║██╔═══╝░██╔══╝░░██╔══██╗  ░╚═══██╗██║╚██╔╝██║██╔══██║██╔══██╗░░░██║░░░
            ╚█████╔╝╚██████╔╝██║░░██║  ██████╔╝╚██████╔╝██║░░░░░███████╗██║░░██║  ██████╔╝██║░╚═╝░██║██║░░██║██║░░██║░░░██║░░░
            ░╚════╝░░╚═════╝░╚═╝░░╚═╝  ╚═════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

            ░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░██╗████████╗███████╗██████╗░░█████╗░
            ██╔═ ██╗██╔══██╗████╗░████║██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
            ██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝╚═╝███╔╝
            ██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗░░░╚══╝░
            ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░╚██████╔╝░░░██║░░░███████╗██║░░██║░░░██╗░░
            ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░.\n\n""")
        while True:
            user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()   
            if self.user_wins == 2:
                break
            if self.computer_wins == 2:  # Creates a break after the computer gets to 2 wins so it doesnt go on for too long and get boring.
                break
            if user_input == "q":  # checks the user input to see if its q and then breaks the while loop.
                break
            if user_input not in self.options:  # if the user enters anything that isnt rock/paper/scissors then it repeats the question.
                continue
            computer_pick = self.options[self.random_number]
            print("Computer picked", computer_pick + ".")
            if user_input == "rock" and computer_pick == "scissors":
                print("""
                        ██████╗░░█████╗░░█████╗░██╗░░██╗  ██╗░░░██╗░██████╗
                        ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██║░░░██║██╔════╝
                        ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ╚██╗░██╔╝╚█████╗░
                        ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ░╚████╔╝░░╚═══██╗
                        ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ░░╚██╔╝░░██████╔╝
                        ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═════╝░

                        ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
                        ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
                        ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
                        ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
                        ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
                        ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░...\n\n\n""")