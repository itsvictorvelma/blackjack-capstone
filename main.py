#BlackJack Capstone Project
import random
import sys
import art

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

# calculate the total of a hand taking aces into account
def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# check if total is exactly 21
def check_blackjack(total):
    return total == 21

# check if total is over 21
def check_bust(total):
    return total > 21

# draw a random card and add it to the hand
def draw_card(hand):
    hand.append(random.choice(cards))

# display the player's and computer's hand reveal_all decides if we show all of computer hand
def display_hands(player_hand, computer_hand, reveal_all=False):
    print(f"Your Cards: {player_hand} || Total: {calculate_total(player_hand)}")

    if reveal_all:
        print(f"Computer Cards: {computer_hand} || Computers Total: {calculate_total(computer_hand)}")
    else:
        print(f"Computers First Card: {computer_hand[0]}")

# main game function
def blackjack():

    # initial hands
    player_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)

    game_over = False

    player_total = calculate_total(player_cards)
    computer_total = calculate_total(computer_cards)

    # check for blackjack on first deal
    if check_blackjack(player_total):
        print("\nBLACKJACK - You Win\n")
        display_hands(player_cards, computer_cards, reveal_all=True)
        sys.exit()

    if check_blackjack(computer_total):
        print("\nComputer has BLACKJACK - You Lose\n")
        display_hands(player_cards, computer_cards, reveal_all=True)
        sys.exit()

    # check if anyone busts on first deal
    if check_bust(player_total):
        print("\nBUSTED - You Lose\n")
        display_hands(player_cards, computer_cards, reveal_all=True)
        sys.exit()

    if check_bust(computer_total):
        print("\nComputer went over 21 - YOU WIN\n")
        display_hands(player_cards, computer_cards, reveal_all=True)
        sys.exit()

    # game loop while player has not finished
    while not game_over:
        display_hands(player_cards, computer_cards, reveal_all = False)
        choice = input("\nHit or Stand?: ").lower()

        # if player hits draw a card and recalc total
        if choice == "hit":
            draw_card(player_cards)
            player_total = calculate_total(player_cards)

            # check if player busts
            if check_bust(player_total):
                print("\nBUSTED - You Lose\n")
                display_hands(player_cards, computer_cards, reveal_all=True)
                game_over = True

            # player reached 21 stop hitting
            elif player_total == 21:
                print("\nYou Reached 21 - YOU WIN!\n")
                display_hands(player_cards, computer_cards, reveal_all=True)
                break

            elif player_total < 21:
                continue

        # player stands computer turn
        elif choice == "stand":
            while computer_total < 16:
                draw_card(computer_cards)
                computer_total = calculate_total(computer_cards)

                # check if computer busts
                if check_bust(computer_total):
                    print("\nComputer went over 21 - YOU WIN\n")
                    display_hands(player_cards, computer_cards, reveal_all=True)
                    game_over = True

                elif computer_total == 21:
                    print("\nYou Lose - Computer reached 21\n")
                    display_hands(player_cards, computer_cards, reveal_all=True)
                    game_over = True
                    break

                # stop computer if total between 16 and 21
                if 16 < computer_total < 21:
                    break

        # final comparison if game not already over
        if not game_over:
            if computer_total > player_total:
                print("\nYou Lose...\n")
                print(f"Computers final hand: {computer_cards} || Total: {computer_total}")
                print(f"Your final hand: {player_cards} || Total: {player_total}")
                game_over = True

            elif player_total > computer_total:
                print("\nYOU WIN")
                print(f"Your final hand: {player_cards} || Total: {player_total}")
                print(f"Computers final hand: {computer_cards} || Total: {computer_total}")
                game_over = True

            else:
                print("\nDRAW\n")
                print(f"Your final hand: {player_cards} || Total: {player_total}")
                print(f"Computers final hand: {computer_cards} || Total: {computer_total}")
                break

# main loop to ask if player wants to play
while True:
    input1 = input("\nWould you like to play a game of blackjack? (y/n): ").lower()

    if input1 == "y":
        print("\nWelcome to my BlackJack game enjoy\n")
        print(art.logo)
        blackjack()

    elif input1 == "n":
        print("\nThank you for your time")
        sys.exit()

    else:
        print("\nPlease enter y or n")
