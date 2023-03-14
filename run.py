import random

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