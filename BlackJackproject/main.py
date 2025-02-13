# BLACKJACK PROJECT
import random
from art import logo

# List of possible cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to get a random card
def deal_card():
    return random.choice(cards)

# Function to calculate the score and change the Ace (if necessary)
def calculate_score(card_list):
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0  # Blackjack
    if 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)  #  Change Ace from 11 to 1
    return sum(card_list)


#Main function that manages the full game
def play_game():
    print("\n"*10)
    print(logo)

    #  Draw 2 cards for the player and the computer
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Check if someone has Blackjack
    if user_score == 0:
        print("Blackjack! You win! 🎉")
    elif computer_score == 0:
        print("Computer has Blackjack! You lose. 😢")
    else:
        #  The player can decide to draw cards
        while user_score < 21:
            game = input("Type 'y' to get another card, type 'n' to pass: ")
            if game == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_score}")
            else:
                break

        # If the player exceeds 21, they lose immediately
        if user_score > 21:
            print("Busted! You lose. 😢")
        else:
            # The computer draws cards until it reaches at least 17
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)

            # Display final scores
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

            # Check who wins
            if computer_score > 21:
                print("Computer busted! You win! 🎉")
            elif user_score == computer_score:
                print("It's a draw! 😐")
            elif user_score > computer_score:
                print("You win! 🎉")
            else:
                print("Computer wins! 😢")

# Loop to ask if the user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
