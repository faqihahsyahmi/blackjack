import art
import random

#step 4 - function draw card
def deal_card():
    """Returns a random card from the list of deck card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#step 6 - takes cards as input for the func and in the body will calc the total of the card in the list
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    #step 7
    if 11 in cards and 10 in cards and len(cards) == 2: #alternative way if sum(cards) == 21 and len(cards) == 2:
        return 0 #blackjack treated as `0`

    #step 8 - logic to handle ACE
    if 11 in cards and sum(cards) > 21:
        #remove 11 and replace it with 1
        cards.remove(11)
        cards.append(1)

    return sum(cards) #return the sum of deck card

#step 13 - compare score func: takes player_score and computer_score as inputs
def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Wow Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif player_score == 0:
        return "Blackjack! You win!!"
    elif player_score > 21:
        return "You went over. You lose.."
    elif computer_score > 21:
        return "Opponent went over. You win..."
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose...LOL"

def play_game():
    #logo goes here
    print(art.logo)
    #step 5
    #deck of cards
    player_card = []
    computer_card = []
    player_score = -1
    computer_score = -1
    game_over = False

    for _ in range(2): #loop runs twice by calling deal_card()
        # add new card to player cards
        player_card.append(deal_card())
        computer_card.append(deal_card())


    #step 11 - while loop
    while not game_over:
        #step 9
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {player_card}, current score: {player_score} ")
        print(f"Computer's first cards: {computer_card[0]}")

        #step 10
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input("Another card? 'y' or 'n': ").lower()
            #if player wants more card then add card, else, game over.
            if another_card == "y":
                player_card.append(deal_card())
            else:
                game_over = True

    #step 12 - for computer to keep drawing cards if below criterias are met
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        #re-calc computer score
        computer_score = calculate_score(computer_card)

    #step 13

    print(f"\nPlayer final card: {player_card}, current score: {player_score}")
    print(f"Computer cards: {computer_card}, computer score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Play Blackjack? 'y' or 'no': "):
    print("\n"*20)
    play_game()