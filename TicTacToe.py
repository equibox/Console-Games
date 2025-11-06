print("Welcome to Tic Tac Toe\n") 
print("Slots to choose from:") 
print("1, 2, 3") 
print("4, 5, 6") 
print("7, 8, 9\n") 
print("You may begin.") 
  
slots = ["placeholder", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "] 
win_conditions = [(1,2,3), (4,5,6), (7,8,9), 
(1,4,7), (2,5,8), (3,6,9), 
(1,5,9), (3,5,7)] 
  
player = " X " 
  
def print_game(): 
    print(f"\n{slots[1]}|{slots[2]}|{slots[3]}") 
    print("-----------") 
    print(f"{slots[4]}|{slots[5]}|{slots[6]}") 
    print("-----------") 
    print(f"{slots[7]}|{slots[8]}|{slots[9]}") 
  
while True: 
    print_game() 
    print(f"\nIt is Player {player}'s turn.") 
    try: 
        choice = int(input("\nSelect a slot to put a marker: ")) 
    except ValueError: 
        print("\nNot an option.") 
        continue 
    if 0 < choice <= 9: 
        if player == " X " and slots[choice] == "   ": 
            slots[choice] = player 
        elif player == " O " and slots[choice] == "   ": 
            slots[choice] = player 
        else:  
            print("Space is already used.") 
            continue 
    else: 
        print("\nNot an option.") 
        continue 
     
    for cond in win_conditions: 
        if slots[cond[0]] == slots[cond[1]] == slots[cond[2]] == player: 
            print_game() 
            print(f"\nPlayer {player} has won!") 
            exit() 
    if player == " X ": 
        player = " O " 
    else: 
        player = " X " 
