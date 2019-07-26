import random

# This is RPS Project made for Udacity IPND course by HASSAN HAMZAH.

# Three different moves the player can make

moves = ['rock', 'paper', 'scissors']


# Function to decide who beats whom

def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# The Player class is the parent class for all of the Players in this game

class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Chooses its move at random and it returns 'rock','paper', or 'scissors'

class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


# What move the opponent played last round and plays it in the next round

class ReflectPlayer(Player):

    def __init__(self):
        # First round is a random choice
        self.previous_move2 = random.choice(moves)

    def move(self):
        return self.previous_move2

    def learn(self, my_move, their_move):
        self.previous_move2 = their_move


# Remembers what move it played last round and cycles through different moves

class CyclePlayer(Player):

    def __init__(self):
        self.previous_move1 = random.choice(moves)

    # Rotate moves until it restarts with rock again

    def move(self):
        moves_available = moves.index(self.previous_move1)
        if moves_available == 2:
            return moves[0]
        else:
            return moves[moves_available + 1]

    # Sets up the player to recall its own previous move

    def learn(self, my_move, their_move):
        self.previous_move1 = my_move


# Asks the player to choose the move

class Human(Player):
    def move(self):
        your_move = ""

        while True:
            your_move = input('Enter Your Move: '
                              '(1.Rock - 2.Paper - 3.Scissors)\n')
            if your_move.lower() == '1' or your_move.lower() == 'rock':
                your_move = 'rock'
                break
            elif your_move.lower() == '2' or your_move.lower() == 'paper':
                your_move = 'paper'
                break
            elif your_move.lower() == '3' or your_move.lower() == 'scissors':
                your_move = 'scissors'
                break
            else:
                print("Enter A Number As Shown On Left Of Choices, Try Again!")
        return your_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_one = 0
        self.player_two = 0
        self.tiegame = 0
        self.rounds_played = 0

    # Print the game header when the game starts

    def game_header(self):
        print(
            "\n"
            "WELCOME TO ROCK PAPER OR SCISSORS\n"
            "\n"
            "\n"
            "\n"
            "LETS BATTLE!!! ...\n")

    def select_mode(self):
        while True:
            rounds_num = input("Select Number Of Rounds (1-10):\n")

            # Checking for valid number 1-10. If not, loop back.
            if rounds_num.isnumeric():
                rounds_num = int(rounds_num)
                if rounds_num >= 0 and rounds_num <= 10:
                    print("You Choosed To Play {0} Rounds!".format(rounds_num))
                    print("")
                    self.rounds_played = rounds_num
                    break
                else:
                    print("That's Not A Number Between 1 to 10!, Try Again.")

    # Choose the opponent

    def opposite_player(self):
        print(
            "Select Your Opponent:\n"
            "\n1. Basic  - Opponent plays rock every round"
            "\n2. Random - Opponent plays random move"
            "\n3. Mimic  - Opponent mimics your move next round"
            "\n4. Cycle  - Remembers what was played and cycles through moves"
            "\n5. Exit   - Quits the game")
        while True:
            opponent = (input(""))
            if opponent.lower() == "1" or opponent.lower() == "Basic":
                self.p2 = Player()
                break
            elif opponent.lower() == "2" or opponent.lower() == "Random":
                self.p2 = RandomPlayer()
                break
            elif opponent.lower() == "3" or opponent.lower() == "Mimic":
                self.p2 = ReflectPlayer()
                break
            elif opponent.lower() == "4" or opponent.lower() == "Cycle":
                self.p2 = CyclePlayer()
                break
            elif opponent.lower() == "5" or opponent.lower() == "Exit":
                print("Alright, See You Later ...")
                self.rounds_played = 0
                break
            else:
                print("That's Not One Of The Options, Try Again.")

    def outcome(self, first_play, second_play):

        if beats(first_play, second_play):
            # Player one wins
            self.player_one += 1
            print("")
            print("You Won The Round!"
                  .format(first_play, second_play))
            print("")
            print("Your Score: {0}".format(self.player_one))
            print("Opponent Score: {0}".format(self.player_two))
            print("")

        elif beats(second_play, first_play):
            # Opponent wins
            self.player_two += 1
            print("")
            print("Opponent Player Won The Round!")
            print("")
            print("Your Score: {0}".format(self.player_one))
            print("Opponent Score: {0}".format(self.player_two))
            print("")

        else:
            # It's a tie
            self.tiegame += 1
            print("")
            print("It's A Tie")
            print("")
            print("Your Score: {0}".format(self.player_one))
            print("Opponent Score: {0}".format(self.player_two))
            print("")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You Choosed: {0}"
              " VS  Opponent Player Chooses: {1}".format(move1, move2))
        self.outcome(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def battle(self):
        if self.rounds_played >= 1:
            for round in range(0, self.rounds_played):
                print("Round " + str(round + 1) + ": ")
                self.play_round()

    def game_results(self):
        # Results of the game
        if self.rounds_played >= 1:
            print("END OF MATCH")
            print("")
            print("You Won: {0}".format(self.player_one))
            print("Opponent Player Won: {0}".format(self.player_two))
            print("Ties: {0}".format(self.tiegame))
            if self.player_one > self.player_two:
                print("")
                print("Congratulations YOU WIN The Match!!!")
            elif self.player_one < self.player_two:
                print("")
                print("Opponent Player Won The Match!!!")
            else:
                print("")
                print("It Is A Draw!")
            print("")
            print("Hope You Enjoyed :) ... Come Back For More.")

    def play_game(self):
        self.game_header()
        self.select_mode()
        self.opposite_player()
        self.battle()
        self.game_results()


if __name__ == '__main__':
    game = Game(Human(), RandomPlayer())
    game.play_game()
