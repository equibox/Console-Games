import random
import time

print("Welcome to the arena!\n")

player_hp = 100
enemy_hp = 100

FOOD_LIST = ("Apple", "Orange", "Pear", "Pineapple", "Watermelon", "Grapes", "Cherries", "Peach")
ENEMY_NAME_LIST = ("Billy the Building Basher", "Terry the Town Smasher", "Larry the Crayon Eater", "Pootis", "Samuel L. Jackson", "The Rock", "Sally the Seashell Seller", "Bob Ross")

PLAYER_ATTACK_LINES = ("slashed your sword", "shot your gun", "blew the enemy up", "stabbed the enemy", "slapped the enemy", "threw a brick", "smashed a plate over the enemy's head", "bit the enemy")
ENEMY_ATTACK_LINES = ("slashed its sword", "shot its gun", "blew you up", "stabbed you", "slapped you", "threw a brick", "smashed a plate over your head", "bit you")

game_over = False

def Attack():
    global enemy_hp
    global game_over
    print("\nYou chose to attack.\n")
    time.sleep(1.5)
    damage_done = random.randint(15,35)
    crit_number = random.randint(1,10)
    #print(str(crit_number))
    if crit_number == 5:
        damage_done *= 2
        print("Critical hit!\n")
        time.sleep(2.5)
    print(f"You {random.choice(PLAYER_ATTACK_LINES)} and dealt {damage_done} damage.\n")
    time.sleep(1.5)
    enemy_hp -= damage_done
    if enemy_hp > 0:
        print(f"The enemy has {enemy_hp} health.\n")
        time.sleep(1.5)
    elif enemy_hp <= 0:
        enemy_hp = 0
        print("You have defeated the enemy!\n")
        time.sleep(1.5)
        game_over = True
        

def Heal():
    global player_hp
    print("\nYou chose to heal.\n")
    time.sleep(1.5)
    health_healed = random.randint(19,43)
    print(f"You consumed {random.choice(FOOD_LIST)} and gained {health_healed} health!\n")
    time.sleep(1.5)
    player_hp += health_healed
    if player_hp > 100:
        player_hp = 100
    print(f"You have {player_hp} health.\n")
    time.sleep(1.5)

def PlayerTurn():
    print("It is now your turn.\n")
    time.sleep(0.5)
    while True:
        choice = input("{A}ttack or {H}eal? ")
        if choice.lower() == "a":
            Attack()
            break
        elif choice.lower() == "h":
            Heal()
            break
        elif choice.lower() != "a" or choice.lower() != "h":
            print("Not an option\n")
            continue

def EnemyAttack():
    global player_hp
    global game_over
    print("The enemy chose to attack.\n")
    time.sleep(1.5)
    damage_done = random.randint(15,35)
    crit_number = random.randint(1,10)
    #print(str(crit_number))
    if crit_number == 5:
        damage_done *= 2
        print("Critical hit!\n")
        time.sleep(2.5)
    print(f"The enemy {random.choice(ENEMY_ATTACK_LINES)} and dealt {damage_done} damage.\n")
    time.sleep(1.5)
    player_hp -= damage_done
    if player_hp > 0:
        print(f"You have {player_hp} health.\n")
        time.sleep(1.5)
    elif player_hp <= 0:
        player_hp = 0
        print("The enemy has defeated you!\n")
        time.sleep(1.5)
        game_over = True

def EnemyHeal():
    global enemy_hp
    print("The enemy chose to heal.\n")
    time.sleep(1.5)
    health_healed = random.randint(19,43)
    print(f"The enemy consumed {random.choice(FOOD_LIST)} and gained {health_healed} health!\n")
    time.sleep(1.5)
    enemy_hp += health_healed
    if enemy_hp > 100:
        enemy_hp = 100
    print(f"The enemy has {enemy_hp} health.\n")
    time.sleep(1.5)

def EnemyTurn():
    global enemy_hp
    print("It is now the enemy's turn.\n")
    time.sleep(1.5)
    choice = random.choice(("a", "h"))
    if enemy_hp != 100:
        if choice == "a":
            EnemyAttack()
        elif choice == "h":
            EnemyHeal()
    elif enemy_hp == 100:
        EnemyAttack()

def Main():
    time.sleep(1.5)
    print(f"Your opponent will be: {random.choice(ENEMY_NAME_LIST)}!\n")
    time.sleep(1.5)
    while True:
        PlayerTurn()
        if game_over == True:
            print("Game Over!")
            exit()
        EnemyTurn()
        if game_over == True:
            print("Game over!")
            exit()

Main()