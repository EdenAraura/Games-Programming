health = 10
class Enemy:
    kind = "fighter"
    weapon = {"sword": 4, "gun": 7}

    def __init__(self, name, faction, ability):
        self.name = name
        self.faction = faction
        self.ability = ability

sharky = Enemy("hektor", "jammie wammie", "cry")
boy = Enemy("rat king", "ratatouille", "cook :)")
