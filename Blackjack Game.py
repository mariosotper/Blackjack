import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = random.choice(cards)
    return drawn_card


def calculate_score(cards):
    # tambien podria usar if sum(cards) ==21 and len(cards) ==2:
    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        # return 0 podemos indicar que el ususario o computador tienen blackjack
        return sum(cards)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def clear():
    _ = os.system("cls")


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :)"

    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "win with a blackjack"
    elif user_score > 21:
        return "you went over, you lose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return " you lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"your final hand: {user_cards}, final score: {user_score}")
        print(
            f"computer's final hand:  {computer_cards}, final score: {computer_score}"
        )

        print(compare(user_score, computer_score))


while input("do you want to play a game of blackjack? type 'y' or 'n': ") == "y":

    clear()
    play_game()

