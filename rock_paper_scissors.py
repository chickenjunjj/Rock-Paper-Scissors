import random
class RockPaperScissors:
    def __init__(self):
        self.start()

    def start(self):
        print("[p] play")
        print("[q] quit")
        command = input()
        print("")
        if command == 'p':
            self.play()
        elif command == 'q':
            pass
        else:
            print("Invalid command \n")
            self.start()

    def play(self):
        print("[r] rock")
        print("[p] paper")
        print("[s] scissors")
        choice = input()
        print("")
        your_choice = self.valid_command(choice)
        print(your_choice)
        if your_choice == "Invalid command \n":
            self.play()
            return
        AI_choice = self.my_choice()
        print("Computer: " + AI_choice + "\n")
        tie = self.winner(choice, AI_choice)
        if tie:
            self.play()
        else:
            self.start()

    def valid_command(self, choice):
        if choice == "r":
            return ("You:      rock")
        elif choice == "p":
            return ("You:      paper")
        elif choice == "s":
            return ("You:      scissors")
        else:
            return ("Invalid command \n")

        
    def my_choice(self):
        number = random.randrange(1, 4)
        if number == 1:
            return ("rock")
        elif number == 2:
            return ("paper")
        elif number == 3:
            return ("scissors")

    def winner(self, choice, AI_choice):
        if choice == "r":
            if AI_choice == "scissors":
                print("You win! \n")
            elif AI_choice == "rock":
                print("Tie!")
                print("Go again \n")
                return True
            elif AI_choice == "paper":
                print("You lose \n")
        elif choice == "p":
            if AI_choice == "rock":
                print("You win! \n")
            elif AI_choice == "paper":
                print("Tie!")
                print("Go again \n")
                return True
            elif AI_choice == "scissors":
                print("You lose \n")
        elif choice == "s":
            if AI_choice == "paper":
                print("You win! \n")
            elif AI_choice == "scissors":
                print("Tie!")
                print("Go again \n")
                return True
            elif AI_choice == "rock":
                print("You lose \n")
        return False

rock_paper_scissors = RockPaperScissors()
