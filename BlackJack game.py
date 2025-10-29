# -------------------------------
# SIMPLE BLACKJACK GAME IN PYTHON
# -------------------------------

import random

# Deal a random card from the deck
def deal_card():
    # 11 is Ace, 10 represents 10, Jack, Queen, and King
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Calculate the current score of a hand
def calculate_score(cards):
    # Check for Blackjack (Ace + 10 in the first two cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 will represent a Blackjack

    # If Ace (11) causes score to go over 21, convert it to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Return the total score
    return sum(cards)

# Compare user and computer scores to decide the winner
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😐"
    elif c_score == 0:
        return "You lose, opponent has Blackjack 😭"
    elif u_score == 0:
        return "You win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over 21. You lose 😭"
    elif c_score > 21:
        return "Opponent went over 21. You win 😁"
    elif u_score > c_score:
        return "You win 😁"
    else:
        return "You lose 😭"

# Main game function
def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two cards to each player at the start
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Keep playing until the game ends
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for win/loss/blackjack conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer keeps drawing cards until it reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final result
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main loop to restart the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)  # Clears the console by printing blank lines
    play_game()
