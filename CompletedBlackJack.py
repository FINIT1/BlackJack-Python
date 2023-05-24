import random # import random to shuffle cards types and amounts. 
cards = [] # card list
types = ["Hearts", "Diamonds",  "Spades", "Clubs" ] # card types
points_total = "" # Player's points declared as a string which is later to become an integer
dealer_points_total = "" # dealer's points declared as a string which is later to become an integer
amounts = [
        {"card" : "Ace", "amount" : 11}, {"card" :"2",  "amount" : 2}, #amounts list indicates the values of the cards
        {"card" : "3", "amount" : 3}, {"card" :"4", "amount" : 4},
        {"card" : "5", "amount" : 5}, {"card" :"6", "amount" : 6},
        {"card" : "7", "amount" : 7}, {"card" :"8", "amount" : 8},
        {"card" : "9", "amount" : 9}, {"card" :"10", "amount" : 10},
        {"card" : "Jack", "amount" : 10}, {"card" : "Queen", "amount" : 10},
        {"card" : "King", "amount" : 10},
    ]
for card_type in types: # for loop that initializes both amounts and types of cards into list
    for card_amount in amounts:
        cards.append([card_amount, card_type])

def shuffle_cards(cards): # function that shuffles cards
    random.shuffle(cards)

def dealing_cards(number_of_cards): # Function that deals cards to player and dealer that is automatically shuffled each time the function is called.
    random.shuffle(cards)
    cards_being_dealt = []
    for i in range(number_of_cards):
        card = cards.pop()
        cards_being_dealt.append(card)
    return cards_being_dealt

player_cards = [] # declaring player cards as a list
dealer_cards = [] # declaring dealer cards as a list

dealer_cards = dealing_cards(2) # dealer recieving two random cards
player_cards = dealing_cards(2) # player recieving two random cards

def card_add(player_cards): # function that adds another card for the player
    points_total = player_cards[0] + player_cards[1]
    print(points_total)

print("You have:")
print(f"-{player_cards[0][0]['card']} of {player_cards[0][1]}") # players first card
print(f"-{player_cards[1][0]['card']} of {player_cards[1][1]}") # players second card

print("\nThe dealer has") # program showing dealers cards
print("-One face down card")
print(f"-{dealer_cards[1][0]['card']} of {dealer_cards[1][1]}") # program showing dealers second card and hiding the first one.

player_input = "" # Declaring player_input as a string

print("\nDo you wish to draw another card? (y/n)") # program asks user if they want to add another card.
player_input = input()

card_increase = 0 # integer, used for incrementing to add another card into the list.

while (player_input == "y" or player_input == "Y") : #if player inputs Yes to hit
    card_increase += 1 #increment

    dealt_card = dealing_cards(1)[0] #add one more card

    player_cards.append(dealt_card) #add extra card into the list

    print("Current cards are:") #print current cards in list

    for i in range(0, len(player_cards)): # for loop which prints the players cards
        print(f"-{player_cards[i][0]['card']} of {player_cards[i][1]}")

    print("\nDo you wish to draw another card? (y/n)") # user input if player would like to draw another card
    player_input = input()

if (player_input == "n" or player_input == "N") : # if player inputs N to stand
    player_converted_point_total = 0 # Created int to change str value in player_card list to integer and store inside of here
    dealer_converted_point_total = 0 # Created int to change str value in dealers_card list to integer and store inside of here
    for i in range(0, len(player_cards)): #for loop to calculate and go through player cards list string and store them inside of the integer player points
        points_total = f"{player_cards[i][0]['amount']}"
        player_converted_point_total += int(points_total)
    print("You have : ", player_converted_point_total, " points") # print player points
    print("Dealer has the cards : \n", f"-{dealer_cards[1][0]['card']} of {dealer_cards[1][1]}", "\n ", f"-{dealer_cards[0][0]['card']} of {dealer_cards[0][1]}" ) #print dealers cards
    for i in range(0, len(dealer_cards)):#for loop to calculate and go through dealers cards list string and store them inside of the integer dealers points
        dealer_points_total = f"{dealer_cards[i][0]['amount']}"
        dealer_converted_point_total += int(dealer_points_total)
    print("Dealer has : ", dealer_converted_point_total, " points") # print player points
    if (player_converted_point_total > 21): # if statement for if player has over 21 points
        print("You bust! You have over 21 points, Dealer wins!")
    elif (dealer_converted_point_total > 21):# if statement for if dealer has over 21 points
        print("Dealer bust! Dealer has over 21 points, You win!")
    elif(player_converted_point_total == 21 and dealer_converted_point_total == 21):# if statement for if player has 21 points
        print("Game is a tie! both dealer and player have 21 points!")
    elif (player_converted_point_total > dealer_converted_point_total):# if statement for if player has more points than dealer
        difference = player_converted_point_total - dealer_converted_point_total
        print("You Win!, you had ", difference, " more points!")
    elif (dealer_converted_point_total > player_converted_point_total):# if statement for if dealer has more points than player
        difference = dealer_converted_point_total - player_converted_point_total
        print("You lose!, Dealer had ", difference, " more points than you!")



