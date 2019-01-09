##Baisc fight funct
import random

health = 10

opponentHealth = 3

responseChoice = ["Aggressive", "Defensive", "Stealthy"]
positionChoice = ["Defensive", "Stealthy", "Aggressive"]

position = random.choice(positionChoice)
print(position)

p = positionChoice.index(position)

response = int(input("What is your response? (1: Aggressive, 2: Defensive, 3: Stealthy)")) -1
print(responseChoice[response])

if response == p:
    opponentHealth -= 1

else:
    health -= 1

if opponentHealth <= 0:
    print("You won the fight!")

elif health <= 0:
    print("You lost the fight!")

#- Continue "not properly in loop", fighting otherwise only lasts one round

print("Your health is: ", health)
print("Opponent's health is: ", opponentHealth)
