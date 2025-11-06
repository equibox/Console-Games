import random
import time
print("Welcome to:")
print(r'''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/
                     ''')
print("-Made by: equibox")

CARD_CHOICES = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10 , 10, 10)
your_wins = 0
dealer_wins = 0
cash = 5000

while True:
    if cash <= 0:
        print("Sorry bud, we don't accept the poor. Try again when you get your money up, not your funny up.")
        exit()

    cards = [random.choice(CARD_CHOICES), random.choice(CARD_CHOICES)]
    player_total = sum(cards)
    aces = 0
    dealer_cards = [random.choice(CARD_CHOICES), random.choice(CARD_CHOICES)]
    dealer_total = sum(dealer_cards)
    dealer_aces = 0
    player_busts = False
    dealer_busts = False
    blackjack = False

    while True:
        print(f"\nYou have ${cash}.")
        try:
            bet = (input("How much do you want to bet? "))
            if 0 < int(bet) <= cash:
                print(f"\nYou bet ${int(bet)}. Good luck!")
                time.sleep(1)
                break
            elif int(bet) <= 0 or int(bet) > cash:
                print("\nYou can't bet that amount. Try again.")
            else:
                print("If you can't read instructions, I don't think you should be playing this game. But, I will let you try again.\n")
                continue
        except ValueError:
            print("Not an option.")
            continue

    print(f"\nYour first card is a {cards[0]}.")
    time.sleep(1)
    print(f"Your second card is a {cards[1]}.")
    print(f"For a total of {player_total}.\n")
    time.sleep(1)
    print(f"The dealer's first card is a {dealer_cards[0]}")
    time.sleep(1)
    print(f"The dealer's second card is a {dealer_cards[1]}")
    print(f"The dealer has a total of {dealer_total}.\n")

    while True:
        if cards[0] == 10 and cards[1] == 11 or cards[0] == 11 and cards[1] == 10:
            blackjack = True
            time.sleep(2)
            print("You got blackjack! Paying out now.\n")
            cash += (int(bet)*1.5)
            your_wins += 1
            break
        choice = input("Would you like to {H}it or {S}tand? ")
        if choice.lower() == "h":
            cardToAdd = random.choice(CARD_CHOICES)
            cards.append(cardToAdd)
            print(f"\nYour new card is a {cardToAdd}.")
            player_total = sum(cards)
            print(f"Your total is {player_total}.\n")
            if 11 in cards:
                aces += 1
            if player_total > 21 and aces == 0:
                print("You bust! House wins.\n")
                dealer_wins += 1
                cash -= int(bet)
                player_busts = True
                break
            elif player_total > 21 and aces >= 1:
                print("Turning ace elevens into ones.")
                time.sleep(2)
                for i in range(len(cards)):
                    if cards[i] == 11:
                        cards[i] = 1
                player_total = sum(cards)
                print(f"Your total is {player_total}.\n")
                time.sleep(1)
                aces -= aces
                continue
        elif choice.lower() == "s":
            print(f"You stand at a total of {player_total}.\n")
            player_total = sum(cards)
            break
        else:
            print("If you can't read instructions, I don't think you should be playing this game.")
            exit()
    if player_busts or blackjack:
        pass
    else:
        print("The dealer is playing.\n")
        time.sleep(1)
        print(f"The dealer's first card is a {dealer_cards[0]}")
        print(f"The dealer's second card is a {dealer_cards[1]}")
        print(f"The dealer has a total of {dealer_total}.")
        time.sleep(1)

        while True:
            dealer_total = sum(dealer_cards)
            if 11 in dealer_cards:
                dealer_aces += 1
            if dealer_total > 21 and dealer_aces == 0:
                print("Dealer busts! You win. \n")
                your_wins += 1
                cash += int(bet)
                dealer_busts = True
                break
            elif dealer_total > 21 and dealer_aces >= 1:
                print("Turning ace elevens into ones.")
                for i in range(len(dealer_cards)):
                    if dealer_cards[i] == 11:
                        dealer_cards[i] = 1
                dealer_total = sum(dealer_cards)
                print(f"Dealer total is {dealer_total}.")
                dealer_aces -= dealer_aces
                continue
            if dealer_total <= 16:
                cardToAdd = random.choice(CARD_CHOICES)
                dealer_cards.append(cardToAdd)
                print(f"\nNew card is a {cardToAdd}.")
                dealer_total = sum(dealer_cards)
                print(f"Dealer total is {dealer_total}.\n")
                time.sleep(3)
                continue
            if 17 <= dealer_total <= 21:
                print("Dealer stands.")
                dealer_total = sum(dealer_cards)
                break
        if player_total == dealer_total and dealer_busts == False:
            print("\nTotals were a tie. Result is a push.\n")
            time.sleep(1)
        elif player_total > dealer_total and dealer_busts == False:
            print("\nYou have a higher total than the dealer. You win!\n")
            your_wins += 1
            cash += int(bet)
            time.sleep(1)
        elif dealer_total > player_total and dealer_busts == False:
            print("\nDealer has a higher total than you. Dealer wins.\n")
            dealer_wins += 1
            cash -= int(bet)
            time.sleep(1)
    while True:
        time.sleep(1)
        print(f"Win/Loss: {your_wins}/{dealer_wins}")
        print(f"Cash: ${cash}")
        choice = input("Would you like to play again? {Y}es or {N}o. ")
        if choice == "y":
            break
        elif choice == "n":
            print("We hope to see you soon.")
            exit()
        else:
            print("If you can't read instructions, I don't think you should be playing this game. But, I will let you try again.\n")
            continue