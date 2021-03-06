import random
import numpy
class RockPaperScissors:
    '''
    Global variables of how many times each weapon is played and how many times the player won/lost
    '''
    def __init__(self):
        self.player_moves = ["r", "p", "s"]
        self.win_lose = []
        self.play()
    '''
    Gets the choice of the player and if they press q, it ends and prints all the stats
    '''
    def play(self):
        AI_choice = self.my_choice()
        print("[r] rock")
        print("[p] paper")
        print("[s] scissors")
        print("[q] quit")
        choice = input().lower()
        if choice == 'q':
            print("\nPlayed rock:    ", self.player_moves.count("r") - 1, "times")
            print("Played paper:   ", self.player_moves.count("p") - 1, "times")
            print("Played scissors:", self.player_moves.count("s") - 1, "times")
            print("You won:        ", self.win_lose.count("w"), "times")
            print("You lost:       ", self.win_lose.count("l"), "times")
            print("You tied:       ", self.win_lose.count("t"), "times\n")
            return
        print("")
        your_choice = self.valid_command(choice)
        print(your_choice)
        if your_choice == "Invalid command \n":
            self.play()
            return
        self.player_moves.append(choice)
        print("Computer: " + AI_choice + "\n")
        tie = self.winner(choice, AI_choice)
        self.play()
    '''
    Checks the choice of the player and prints it out, if it is invalid, it prints invalid command
    '''
    def valid_command(self, choice):
        if choice == "r":
            return ("You:      rock")
        elif choice == "p":
            return ("You:      paper")
        elif choice == "s":
            return ("You:      scissors")
        else:
            return ("Invalid command \n")

    '''
    Choice of the computer, probability based. If the user plays a lot of one weapon, it will have a higher chance to choose the weapon to counter it
    '''    
    def my_choice(self):
        number = numpy.random.choice(numpy.arange(0, 3), p = [self.player_moves.count("s")/len(self.player_moves), self.player_moves.count("r")/len(self.player_moves), self.player_moves.count("p")/len(self.player_moves)])
        if number == 0:
            return ("rock")
        elif number == 1:
            return ("paper")
        elif number == 2:
            return ("scissors")
    '''
    Checks if the player won, lost or tied
    '''
    def win_lose_tie(self, choice1, choice2, choice3, AI_choice):
        if AI_choice == choice1:
            print("You win! \n")
            self.win_lose.append("w")
        elif AI_choice == choice2:
            print("Tie!")
            print("Go again \n")
            self.win_lose.append("t")
            return True
        elif AI_choice == choice3:
            print("You lose \n")
            self.win_lose.append("l")
    '''
    Calls the previous function with different arguments
    '''
    def winner(self, choice, AI_choice):
        if choice == "r":
            self.win_lose_tie("scissors", "rock", "paper", AI_choice)
        elif choice == "p":
            self.win_lose_tie("rock", "paper", "scissors", AI_choice)
        elif choice == "s":
            self.win_lose_tie("paper", "scissors", "rock", AI_choice)
        return False

rock_paper_scissors = RockPaperScissors()
