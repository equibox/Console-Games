print("Welcome to Sticks")
print("")

player1_left = 1
player1_right = 1
player2_left = 1
player2_right = 1

current_player = 1

while True:
    print(f"It is Player {current_player}'s Turn!")
    print("")
    print("Enemy's hand")
    if current_player == 1:
        print("Left: ", ("I" * player2_left))
        print("Right: ", ("I" * player2_right))
    elif current_player == 2:
        print("Left: ", ("I" * player1_left))
        print("Right: ", ("I" * player1_right))
    print("Your hand")
    if current_player == 1:
        print("Left: ", ("I" * player1_left))
        print("Right: ", ("I" * player1_right))
    elif current_player == 2:
        print("Left: ", ("I" * player2_left))
        print("Right: ", ("I" * player2_right))
    choice = input("Would you like to {Attack} or {Transfer}? ").lower()
    if choice == "attack" or choice == "a":
        handToAttack = input("What hand of the enemy would you like to attack? {Left} or {Right}? ").lower()
        handAttacking = input("With what hand would you like to attack? {Left} or {Right}? ").lower()
        if current_player == 1:
            if handToAttack == "left" or handToAttack == "l" and (handAttacking == "left" or handAttacking == "l"):
                if player2_left == 0 or player1_left == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player2_left += player1_left
            elif handToAttack == "left" or handToAttack == "l" and (handAttacking == "right" or handAttacking == "r"):
                if player2_left == 0 or player1_right == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player2_left += player1_right
            elif handToAttack == "right" or handToAttack == "r" and (handAttacking == "left" or handAttacking == "l"):
                if player2_right == 0 or player1_left == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player2_right += player1_left
            elif handToAttack == "right" or handToAttack == "r" and (handAttacking == "right" or handAttacking == "r"):
                if player2_right == 0 or player1_right == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player2_right += player1_right
            else:
                print("Invalid Syntax in choosing hands. Restarting Turn.")
                print("")
                continue
        elif current_player == 2:
            if handToAttack == "left" or handToAttack == "l" and (handAttacking == "left" or handAttacking == "l"):
                if player1_left == 0 or player2_left == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player1_left += player2_left
            elif handToAttack == "left" or handToAttack == "l" and (handAttacking == "right" or handAttacking == "r"):
                if player1_left == 0 or player2_right == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player1_left += player2_right
            elif handToAttack == "right" or handToAttack == "r" and (handAttacking == "left" or handAttacking == "l"):
                if player1_right == 0 or player2_left == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player1_right += player2_left
            elif handToAttack == "right" or handToAttack == "r" and (handAttacking == "right" or handAttacking == "r"):
                if player1_right == 0 or player2_right == 0:
                    print("Cannot attack with 0 or attack 0. Restarting turn")
                    continue
                else:
                    player1_right += player2_right
            else:
                print("Invalid Syntax in choosing hands. Restarting Turn.")
                print("")
                continue
    elif choice == "transfer" or choice == "t":
        handFrom = input("Which hand to transfer from? {Left} or {Right}? ")
        if current_player == 1:
            fingers = int(input("How many fingers to transfer? "))
            if handFrom == "left" or handFrom == "l":
                if fingers >= player1_left or fingers <= 0:
                    print("Invalid number of fingers. Restarting turn.")
                    print("")
                    continue
                else:
                    player1_right += fingers
                    player1_left -= fingers
            elif handFrom == "right" or handFrom == "r":
                if fingers >= player1_right or fingers <= 0:
                    print("Invalid number of fingers. Restarting turn.")
                    print("")
                    continue
                else:
                    player1_left += fingers
                    player1_right -= fingers
        elif current_player == 2:
            fingers = int(input("How many fingers to transfer? "))
            if handFrom == "left" or handFrom == "l":
                if fingers >= player2_left or fingers <= 0:
                    print("Invalid number of fingers. Restarting turn.")
                    print("")
                    continue
                else:
                    player2_right += fingers
                    player2_left -= fingers
            elif handFrom == "right" or handFrom == "r":
                if fingers >= player2_right or fingers <= 0:
                    print("Invalid number of fingers. Restarting turn.")
                    print("")
                    continue
                else:
                    player2_left += fingers
                    player2_right -= fingers
    else:
        print("Invalid Syntax. Restarting turn.")
        continue
    if player1_left >= 5:
        player1_left =0
        print("Player 1's left hand is out.")
        print("")
    elif player1_right >= 5:
        player1_right = 0
        print("Player 1's right hand is out.")
        print("")
    elif player2_left >= 5:
        player2_left = 0
        print("Player 2's left hand is out.")
        print("")
    elif player2_right >= 5:
        player2_right = 0
        print("Player 2's right hand is out.")
        print("")
    else:
        print("Turn successful.")
        print("")

    if player1_left == 0 and player1_right == 0:
        print("Player 2 has won the game!")
        exit()
    elif player2_left == 0 and player2_right == 0:
        print("Player 1 has won the game!")
        exit()
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1