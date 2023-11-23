import random
import time
import sys

class Pig:
    def __init__(self) -> None:
        # initialise scores and players
        self.ai_score = 0
        self.player_score = 0
        self.current_go_score = 0

        self.player_name = ""
        self.ai_name = ""

        self.current_player = "" 
        self.required_score = 100


    def game_over(self) -> bool:
        # return true if the game is over and handle game end
        game_over = False

        if self.ai_score >= self.required_score:
            game_over = True
            print(f"You lost with a final score of {self.player_score}")
        elif self.player_score >= self.required_score:
            game_over = True
            point_difference = self.required_score - self.ai_score
            print(f"You won by {point_difference} points")

        return game_over


    def set_names(self) -> None:
        common_names = [
            "Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia",
            "Jackson", "Lucas", "Mia", "Ethan", "Alexander", "Aiden", "Chloe",
            "Elijah", "Abigail", "Mason", "Harper", "Evelyn", "Michael", 
            "Benjamin", "Emily", "Daniel", "Logan", "Avery", "Sebastian",
            "Carter", "James", "Aria", "Grayson", "Emma", "Liam", "Olivia",
            "Noah", "Ava"
        ]

        # sets player name
        self.player_name = input("Enter your player name: ")
        print(f"Welcome to pig, {self.player_name}!")
       
        #sets ai name
        while self.ai_name == self.player_name or self.ai_name ==  "":
            self.ai_name = random.choice(common_names)

        # randomly selects first player
        self.current_player = random.choice([self.player_name, self.ai_name])


    def roll_dice(self, current_player_name: str) -> None:
        if current_player_name == self.player_name:
            print(f"\n{self.player_name} it is your turn!")
            while True:
                player_input = input("Enter 1 to roll dice or 2 to stop: ")
                if player_input == "1":
                    print("\n\tRolling", end="")
                    sys.stdout.flush()
                    for _ in range(1, 4):
                        time.sleep(0.5)
                        print(".", end="")
                        # flushes because print statements seem to be buffered 
                        sys.stdout.flush()
                    print()
                    roll_value = random.randint(1, 6)
                    print(f"\t{self.player_name} rolled {roll_value}!\n")
                    if roll_value == 1:
                        self.current_go_score = 0
                        break

                    self.current_go_score += roll_value
                elif player_input == "2":
                    break
                else:
                    print("Invalid option please enter either 1 or 2")

            self.player_score += self.current_go_score
            self.current_go_score = 0


        elif current_player_name == self.ai_name:
            print(f"\n{self.ai_name}'s go!")
            amount_of_rolls = random.randint(1, 5)
            print(amount_of_rolls)
            for _ in range(0, amount_of_rolls):
                print("\n\tRolling", end="")
                sys.stdout.flush()
                for _ in range(1, 4):
                    time.sleep(0.5)
                    print(".", end="")
                    sys.stdout.flush()
                print()
                roll_value = random.randint(1, 6)
                print(f"\t{self.ai_name} rolled {roll_value}!")
                if roll_value == 1:
                    self.current_go_score = 0
                    break

                self.current_go_score += roll_value

                if self.ai_score + self.current_go_score > self.required_score:
                    break

            self.ai_score += self.current_go_score
            self.current_go_score = 0



    def play_game(self) -> None:
        self.set_names()

        # gameplay loop
        while True:
            if self.current_player == self.player_name and not self.game_over():
                self.roll_dice(self.player_name)
                self.current_player = self.ai_name
                print(f"\n{self.player_name}'s score: {self.player_score}")

            if self.current_player == self.ai_name and not self.game_over():
                self.roll_dice(self.ai_name)
                self.current_player = self.player_name
                print(f"\n{self.ai_name}'s score: {self.ai_score}")

            if self.game_over():
                break


if __name__ == "__main__":
    # create instance of the game
    pig = Pig()
    pig.play_game()
