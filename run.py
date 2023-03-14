import random  # imports random module from python eg randomise numbers.
import time  # import time module eg delay seconds before next line of code.

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
            user_input = input("Type Rock/Paper/Scissors or Q to quit:\n ").lower()  # takes an input from the user and coverts to lowercase. 
            if self.user_wins == 2:  # Creates a break after the user gets to 2 wins so it doesnt go on for too long and get boring.
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
                time.sleep(2)
                print("""                            ██████╗░░█████╗░░█████╗░██╗░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗██╗
                            ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ░██║░░██╗░░██║██║████╗░██║██╔════╝██║
                            ██████╔╝██║░░██║██║░░╚═╝█████═╝░  ░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░██║
                            ██╔══██╗██║░░██║██║░░██╗██╔═██╗░  ░░████╔═████║░██║██║╚████║░╚═══██╗╚═╝
                            ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝██╗
                            ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝""")
                print("You won this round!")
                self.user_wins += 1
                self.random_number = random.randint(0, 2)
                if self.user_wins == 2:
                    time.sleep(1)
                    print("""                            ░██╗░░░░░░░██╗███████╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
                            ░██║░░██╗░░██║██╔════╝  ██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
                            ░╚██╗████╗██╔╝█████╗░░  ███████║███████║╚██╗░██╔╝█████╗░░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║
                            ░░████╔═████║░██╔══╝░░  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║
                            ░░╚██╔╝░╚██╔╝░███████╗  ██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
                            ░░░╚═╝░░░╚═╝░░╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░

                            ░█████╗░██╗░░░██╗██████╗░  ░█████╗░██╗░░██╗░█████╗░███╗░░░███╗██████╗░██╗░█████╗░███╗░░██╗
                            ██╔══██╗██║░░░██║██╔══██╗  ██╔══██╗██║░░██║██╔══██╗████╗░████║██╔══██╗██║██╔══██╗████╗░██║
                            ██║░░██║██║░░░██║██████╔╝  ██║░░╚═╝███████║███████║██╔████╔██║██████╔╝██║██║░░██║██╔██╗██║
                            ██║░░██║██║░░░██║██╔══██╗  ██║░░██╗██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝░██║██║░░██║██║╚████║
                            ╚█████╔╝╚██████╔╝██║░░██║  ╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░░░░██║╚█████╔╝██║░╚███║""")
                    break
            elif user_input == "paper" and computer_pick == "rock":
                print("""                            ██████╗░░█████╗░██████╗░███████╗██████╗░  ██╗░░░██╗░██████╗  ██████╗░░█████╗░░█████╗░██╗░░██╗
                            ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██║░░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
                            ██████╔╝███████║██████╔╝█████╗░░██████╔╝  ╚██╗░██╔╝╚█████╗░  ██████╔╝██║░░██║██║░░╚═╝█████═╝░
                            ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗  ░╚████╔╝░░╚═══██╗  ██╔══██╗██║░░██║██║░░██╗██╔═██╗░
                            ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║  ░░╚██╔╝░░██████╔╝  ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
                            ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═════╝░  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝...\n\n\n""")
                time.sleep(2)
                print("""                            ██████╗░░█████╗░██████╗░███████╗██████╗░  ░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗██╗
                            ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ░██║░░██╗░░██║██║████╗░██║██╔════╝██║
                            ██████╔╝███████║██████╔╝█████╗░░██████╔╝  ░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░██║
                            ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗  ░░████╔═████║░██║██║╚████║░╚═══██╗╚═╝
                            ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝██╗
                            ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝""")
                print("You won this round!")
                self.user_wins += 1
                self.random_number = random.randint(0, 2)
                if self.user_wins == 2:
                    time.sleep(1)
                    print("""                            ░██╗░░░░░░░██╗███████╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
                            ░██║░░██╗░░██║██╔════╝  ██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
                            ░╚██╗████╗██╔╝█████╗░░  ███████║███████║╚██╗░██╔╝█████╗░░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║
                            ░░████╔═████║░██╔══╝░░  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║
                            ░░╚██╔╝░╚██╔╝░███████╗  ██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
                            ░░░╚═╝░░░╚═╝░░╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░

                            ░█████╗░██╗░░░██╗██████╗░  ░█████╗░██╗░░██╗░█████╗░███╗░░░███╗██████╗░██╗░█████╗░███╗░░██╗
                            ██╔══██╗██║░░░██║██╔══██╗  ██╔══██╗██║░░██║██╔══██╗████╗░████║██╔══██╗██║██╔══██╗████╗░██║
                            ██║░░██║██║░░░██║██████╔╝  ██║░░╚═╝███████║███████║██╔████╔██║██████╔╝██║██║░░██║██╔██╗██║
                            ██║░░██║██║░░░██║██╔══██╗  ██║░░██╗██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝░██║██║░░██║██║╚████║
                            ╚█████╔╝╚██████╔╝██║░░██║  ╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░░░░██║╚█████╔╝██║░╚███║""")
                    break
            elif user_input == "scissors" and computer_pick == "paper":
                print("""                            ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗  ██╗░░░██╗░██████╗
                            ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝  ██║░░░██║██╔════╝
                            ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░  ╚██╗░██╔╝╚█████╗░
                            ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗  ░╚████╔╝░░╚═══██╗
                            ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝  ░░╚██╔╝░░██████╔╝
                            ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═════╝░

                            ██████╗░░█████╗░██████╗░███████╗██████╗░
                            ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
                            ██████╔╝███████║██████╔╝█████╗░░██████╔╝
                            ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗
                            ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║...\n\n\n""")
                time.sleep(2)
                print("""                            ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗  ░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗██╗
                            ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝  ░██║░░██╗░░██║██║████╗░██║██╔════╝██║
                            ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░  ░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░██║
                            ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗  ░░████╔═████║░██║██║╚████║░╚═══██╗╚═╝
                            ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝██╗
                            ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝""")
                print("You won this round!")
                self.user_wins += 1
                self.random_number = random.randint(0, 2)
                if self.user_wins == 2:
                    time.sleep(1)
                    print("""                    ░██╗░░░░░░░██╗███████╗  ██╗░░██╗░█████╗░██╗░░░██╗███████╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
                            ░██║░░██╗░░██║██╔════╝  ██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
                            ░╚██╗████╗██╔╝█████╗░░  ███████║███████║╚██╗░██╔╝█████╗░░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║
                            ░░████╔═████║░██╔══╝░░  ██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║
                            ░░╚██╔╝░╚██╔╝░███████╗  ██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
                            ░░░╚═╝░░░╚═╝░░╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░

                            ░█████╗░██╗░░░██╗██████╗░  ░█████╗░██╗░░██╗░█████╗░███╗░░░███╗██████╗░██╗░█████╗░███╗░░██╗
                            ██╔══██╗██║░░░██║██╔══██╗  ██╔══██╗██║░░██║██╔══██╗████╗░████║██╔══██╗██║██╔══██╗████╗░██║
                            ██║░░██║██║░░░██║██████╔╝  ██║░░╚═╝███████║███████║██╔████╔██║██████╔╝██║██║░░██║██╔██╗██║
                            ██║░░██║██║░░░██║██╔══██╗  ██║░░██╗██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝░██║██║░░██║██║╚████║
                            ╚█████╔╝╚██████╔╝██║░░██║  ╚█████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║░░░░░██║╚█████╔╝██║░╚███║""")
                    break
            elif user_input == computer_pick:
                print("""                            ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
                            ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
                            ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
                            ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
                            ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
                            ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░""")
                self.random_number = random.randint(0, 2)
            else:
                print("""                            ░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░██╗████████╗███████╗██████╗░  ░░░░░░░░░███╗░░
                            ██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░██║╚══██╔══╝██╔════╝██╔══██╗  ░░██╗░░░████║░░
                            ██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░██║░░░██║░░░█████╗░░██████╔╝  ██████╗██╔██║░░
                            ██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗  ╚═██╔═╝╚═╝██║░░
                            ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░╚██████╔╝░░░██║░░░███████╗██║░░██║  ░░╚═╝░░███████╗
                            ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░░░░░╚══════╝...\n\n\n\n""")
                self.computer_wins += 1
                if self.computer_wins == 2:
                    time.sleep(1)
                    print("""                                ░█████╗░░██╗░░░░░░░██╗░██╗░░░░░░░██╗██╗  ██████╗░░█████╗░███╗░░██╗████████╗  ░█████╗░██████╗░██╗░░░██╗
                                ██╔══██╗░██║░░██╗░░██║░██║░░██╗░░██║██║  ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝  ██╔══██╗██╔══██╗╚██╗░██╔╝
                                ███████║░╚██╗████╗██╔╝░╚██╗████╗██╔╝██║  ██║░░██║██║░░██║██╔██╗██║░░░██║░░░  ██║░░╚═╝██████╔╝░╚████╔╝░
                                ██╔══██║░░████╔═████║░░░████╔═████║░╚═╝  ██║░░██║██║░░██║██║╚████║░░░██║░░░  ██║░░██╗██╔══██╗░░╚██╔╝░░
                                ██║░░██║░░╚██╔╝░╚██╔╝░░░╚██╔╝░╚██╔╝░██╗  ██████╔╝╚█████╔╝██║░╚███║░░░██║░░░  ╚█████╔╝██║░░██║░░░██║░░░
                                ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

                                ██╗░░░░░░█████╗░░██████╗███████╗██████╗░
                                ██║░░░░░██╔══██╗██╔════╝██╔════╝██╔══██╗
                                ██║░░░░░██║░░██║╚█████╗░█████╗░░██████╔╝
                                ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░██╔══██╗
                                ███████╗╚█████╔╝██████╔╝███████╗██║░░██║
                                ╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝""")
                    break
                self.random_number = random.randint(0, 2)

        print("\nYour score: ", self.user_wins)
        print("Computer's score: ", self.computer_wins)

game = RockPaperScissors()
game.play()