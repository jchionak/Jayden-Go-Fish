"""
A simple go fish game loop.
"""

from Jayden-Go-Fish.player import *
from time import sleep
from random import randint

NAMES = ['Leb', 'Rafidain', 'Julian', 'Matthew', 'Lucas', 'Scott', 'Jamal', 'Theresa', 'Celeste', 'David', 'Gina', 'Ellen']


def main():

    print(f"Welcome to Jayden's Go Fish!")
    print(f"Now, you can finally play Go Fish without needing real cards or real friends!")

    sleep(3)

    print(f"This is a game of go fish between 2 players: you vs. the computer.")

    sleep(2)

    name = input(f"First, tell me your name (you can't change this, so make it good): ")

    if name.upper() != 'JAYDEN':
        print(f"Really? That's your name?")

        sleep(3)

        print(f"Ok then.")
    else:
        print(f"That's a great name, brother.")

    human = HumanPlayer(name)

    computer_name = NAMES[randint(0, len(NAMES) - 1)]

    sleep(2)

    print(f"Ok, you're good to go. Your opponent today will be {computer_name}. They may have a name, but they're really just a few lines of code, so feel free to rage and curse them if you lose.")

    computer_player = ComputerPlayer(computer_name)

    sleep(4)

    print(f"Let's get this game started!")

    sleep(2)

    while True:
        deck = Deck()

        deck.add_cards_no_jokers()

        deck.shuffle()

        human.draw(deck, 7)
        computer_player.draw(deck, 7)

        print(f"Each player begins the game with 7 cards. Here is your hand: ")

        sleep(3)

        print(f"{human.string_hand()}")

        sleep(4)

        print(f"If you have some matches, I'll go ahead and move them to your matches pile. If you don't, that sucks.")

        human.check_matches()
        computer_player.check_matches()

        sleep(3)

        print(f"Here are your matches: ")
        if human.matches == []:
            print(f"No matches LOL")
        else:
            print(f"{human.string_matches()}")

        print(f"You get to go first, because you're a real person and have human rights.")

        sleep(3)

        while True:
            if not human.hand:
                break
            if not computer_player.hand:
                break
            human.choose_action(deck, computer_player)
            sleep(3)
            if not human.hand:
                break
            if not computer_player.hand:
                break
            computer_player.choose_action(deck, human)
            sleep(3)

        if not human.hand:
            print(f"Congrats, {human.name}! You won!")
            sleep(3)
            print(f"To be fair, though, your opponent doesn't have a brain and literally chose cards at random.")
            sleep(2)
            print(f"Still, great job!")
        else:
            print(f"Damn, you lost. Good effort, though.")

        replay = input(f"Do you want to play again? 1 if yes, 2 if no.")

        while True:
            try:
                replay = int(replay)
            except ValueError:
                replay = input("Input a number, man.")
                continue
            else:
                break

        if replay <= 1:
            print(f"You really like Go Fish, huh? Ok, let's play again.")
            human.hand = []
            human.matches = []
            computer_player.hand = []
            computer_player.matches = []
            continue

        else:
            break

    print(f"Thanks for playing, {human.name}!")
    sleep(0.5)
    print(f"If {computer_player.name} had feelings, I'm sure they would've had fun.")


if __name__ == '__main__':
    main()
