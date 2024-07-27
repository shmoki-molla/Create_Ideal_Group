import random

class Warrior:
    def __init__(self, t, str, sta, ran, c):
        self.type = t
        self.strength = str
        self.stamina = sta
        self.range = ran
        self.cost = c


    def display(self):
        print("Type: {}, Strength: {}, Stamina: {}, Range: {}, Cost: {}".format(self.type, self.strength, self.stamina, self.range, self.cost))
class Mercenary:
    def __init__(self, wp=None, wt="None"):
        self.weapon = wp
        self.weaponType = wt

class Guild:
    def __init__(self):
        self.mercenaries = []


    def addMercenary(self, m):
        self.mercenaries.append(m)

    def displayMercenaries(self):
        for m in self.mercenaries:
            print("Mercenary with weapon type: {}".format(m.weaponType))
            if m.weapon:
                m.weapon.display()
def createRandomWarrior():
    types = [ "Swordsman", "Mage", "Archer" ]
    type = random.choice(types)
    strength = random.randint(2, 10)
    stamina = random.randint(2, 10)
    range = random.randint(2, 10)
    cost = random.randint(1, 100)


    if type == "Mage":
        strength += 2
        stamina -= 2
    elif type == "Archer":
        strength -= 2
        stamina += 2

    return Warrior(type, strength, stamina, range, cost)
def fillGuildWithRandomMercenaries(guild, count):
    for i in range(count):
        w = createRandomWarrior()
        m = Mercenary(w, w.type)
        guild.addMercenary(m)

def formIdealGroup(guild, maxCost):
    idealGroup = []
    totalStamina = 0
    totalCost = 0


    guild.mercenaries.sort(key=lambda x: x.weapon.strength, reverse=True)

    for m in guild.mercenaries:
        if len(idealGroup) >= 5 and totalStamina >= 50:
            break
        if totalCost + m.weapon.cost > maxCost:
            continue

        idealGroup.append(m)
        totalStamina += m.weapon.stamina
        totalCost += m.weapon.cost

    return idealGroup

random.seed()

guild = Guild()
fillGuildWithRandomMercenaries(guild, 20)

print("List of mercenaries in the guild:")
guild.displayMercenaries()

maxCost = 200
idealGroup = formIdealGroup(guild, maxCost)

print("\nIdeal Group (max cost {}):".format(maxCost))
for m in idealGroup:
    m.weapon.display()