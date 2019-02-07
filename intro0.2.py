class Collectible:
    def __init__(self, amount):
        self.type = type
        self.amount = amount
        
class Potion(Collectible):
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

banana = Potion("banana", 5)
coin = Trinket("coin", 10)
rainbow = Potion("rainbow", 15)

class Trinket(Collectible):
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

score = 0
inpt = input("?")
if inpt == "banana":
    print(banana.name)
    score += banana.amount
elif inpt == "coin":
    print(coin.name)
    score += coin.amount
elif inpt == "rainbow":
    print(rainbow.name)
    score += rainbow.amount

print(score)
