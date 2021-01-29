import random

# abstraction = extracting something from a totality of which it is an integral part -- simplifying something for a purpose
# an object is an instance of a class
# objects contain variables and functions


class Enemy:
    # Class variables/attributes/fields
    __weapons = {"sword": 10, "axe": 15, "hammer": 20}  # The __ makes it a private variable.
    __names = ["Wraith", "Ghoul", "Ghost", "Phantom", "Beast"]
    __clans = ["Blood", "Evil", "Spooky"]
    __abilities = ["self heal", "poison", "invisibility"]

    # Class methods
    def __init__(self):  # Nothing is assigned manually, so no values after "self".
        self.name = random.choice(Enemy.__names)  # Values are assigned randomly.
        self.clan = random.choice(Enemy.__clans) + " Clan"
        self.ability = random.choice(Enemy.__abilities)
        self.weapon = random.choice(list(Enemy.__weapons))
        self.damage = Enemy.__weapons[self.weapon]  # Assigned automatically using dictionary key.
        self.description = "This " + self.name + " is part of the " + self.clan + ". It has the " + \
                           self.ability + " ability, and is using a " + self.weapon + " that does " + \
                           str(self.damage) + " damage."

    def get_description(self):  # For if you want to edit the description later.
        return self.description


# Instantiating 5 enemies.
enemies = []
numberOfEnemies = 0

while numberOfEnemies < 5:
    enemies.append(Enemy())
    numberOfEnemies += 1

# Printing the enemies' descriptions.
for enemy in enemies:
    print(enemy.description)


class Collectibles:
    __items = ["Potion", "Coin"]

    def __init__(self):
        self.item = random.choice(list(Collectibles.__items))


class Potions(Collectibles):
    __coloursAndPoints = {"purple": 10, "green": -100, "orange": 30, "yellow": 25, "red": 50}

    def __init__(self):
        Collectibles.__init__(self)
        self.colour = random.choice(list(Potions.__coloursAndPoints))
        self.points = Potions.__coloursAndPoints[self.colour]


class Coins(Collectibles):
    __typesAndPoints = {"gold coin": 100, "silver coin": 10, "copper coin": 1}

    def __init__(self):
        Collectibles.__init__(self)
        self.type = random.choice(list(Coins.__typesAndPoints))
        self.points = Coins.__typesAndPoints[self.type]


# Here is the game:
playerPoints = 0

while playerPoints < 600:
    choice = input("Pick a number between 1 and 6: \n")
    if int(choice) <= 3:
        coin = Coins()
        print("You found a " + coin.type + " and gained " + str(coin.points) + " points!")
        playerPoints += coin.points
    elif int(choice) <= 6:
        potion = Potions()
        if potion.colour != "green":
            print("You found a " + potion.colour + " potion and gained " + str(potion.points) + " points!")
        else:
            print("Oh no! You found a green potion and lost 100 points!")
        playerPoints += potion.points
    else:
        continue
    if playerPoints < 0:
        playerPoints = 0
    print("Total points: " + str(playerPoints) + "\n")

print("Congratulations, you levelled up!")
