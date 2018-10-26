direction=input("You awake in a room. To your left you see a static TV screen. To your right is a rotting sofa. Forward, you see a mouldy window with tattered curtains. Behind you is a locked door. Which direction to you go in?")
if direction == "left":
    print("The TV is old. You didn't know this place still had power. The static hypnotises you. You return to the centre of the room.")
elif direction == "right":
    print("The sofa was once white, probably. Now it's a mildewed grey. You think for a second you might take a seat. Then you think better of it. You return to the centre of the room.")
elif direction == "forward":
    print("The window is shattered in places. Probably not enough to climb through it. oh well. You return to the centre of the room.")
elif direction == "back":
    print("You've already tried the door. It's locked. But maybe if you try again it won't be... nope. Definitely locked. You return to the centre of the room.")
else:
    print("If you want to survive, you should start making more sense.")
