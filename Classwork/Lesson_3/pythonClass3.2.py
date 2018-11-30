##Not Functional

inventory = ["axe", "lockpick"]
game_on = True
list_yes = ["yeah", "y," "okay", "ok", "sure", "why not", "o.k.", "yes"]
while game_on:

    input = input("You are trapped in a room with a rotting wooden door. It's locked. Attempt to get through? ").lower()
    print(inventory)

    if input in list_yes:
        input = input("Which tool will you use? ".lower()
        if input == "axe":
            print("You break down the door, like an animal. You're an animal. Really now! That was hardly necessary.")
        elif input == "lockpick":
            print("You politely open the door, civilly, like a normal person.")
        elif input in inventory and input != "axe" and if input != "lockpick":
            print("Well, you can give it a go if you like, but there's no way that'll work. Actually, no. You can't try that. Idiot.")
        else:
            print("Really? What the Hell are you thinking?!")
