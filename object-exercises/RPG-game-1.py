# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, power, health, name):
        self.power = power
        self.health = health
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)

class Goblin(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)


def main():
    hero = Hero(5, 10, 'Hero')
    goblin = Goblin(2, 6, 'Goblin')

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()

