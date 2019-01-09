##Basic fight funct
fight = True

health = 10
opponentHealth = 3

while fight == True:

    import random

    print("Your health is: ", health)
    print("Opponent's health is: ", opponentHealth)

    responseChoice = ["Aggressive", "Defensive", "Stealthy"]
    positionChoice = ["Defensive", "Stealthy", "Aggressive"]
    position = random.choice(positionChoice)
    print(position)
    p = positionChoice.index(position)

    response = int(input("What is your response? (1: Aggressive, 2: Defensive, 3: Stealthy)")) -1
    print(responseChoice[response])

    if response == p:
        opponentHealth -= 1
        print("It worked!")
        if opponentHealth <= 0:
            print("You won the fight!")
            break
        elif health <=0:
            print("You lost the fight!")
            break
        else:
            continue

    else:
        health -= 1
        print("That didn't work...")
        if opponentHealth <= 0:
            print("You won the fight!")
            break
        elif health <=0:
            print("You lost the fight!")
            break
        else:
            continue
