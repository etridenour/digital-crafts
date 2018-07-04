
import random

class Character:
    def __init__(self, power, health, name):
        self.power = power
        self.health = health
        self.name = name

    def attack(self, enemy):
        damage_multiplier = 1
        rand_heal = random.randint(1,5)
        if enemy.name == 'Shadow':
            rand_evade = random.randint(1, 10)
            if rand_evade > 1:
                print("{} does no damage to the {}".format(self.name, enemy.name))
                damage_multiplier = 0
            else:
                enemy.health -= self.power
        if enemy.name == 'Goblin':
            rand_block = random.randint(1, 5)
            if rand_block == 1:
                print('The {} blocked the {}\'s attack.'.format(enemy.name, self.name))
                damage_multiplier = 0
            else:
                enemy.health -= self.power

        if enemy.name == 'Sharknado':
            rand_sweep = random.randint(1,7)
            if rand_sweep == 1:
                print("The {} swept up the {}.".format(enemy.name, self.name))
                damage_mulitplier = 3
            else:
                enemy.health -= self.power

        if enemy.name == "Angry Beaver":
            rand_angry = random.randint(1,6)
            if rand_angry == 1:
                print('The {} is super angry!'.format(enemy.name))
                damage_mulitplier = 2
            else:
                enemy.health -= self.power

        if self.name == 'Hero':
            rand_attack = random.randint(1,5)
            if damage_mulitplier == 0:
                pass
            elif rand_attack == 1:
                damage_mulitplier = 2
                print('The {} hit with double power!'.format(self.name))
                enemy.health -= self.power * damage_mulitplier

        
        print("{} does {} damage to the {}.".format(self.name, self.power * damage_multiplier, enemy.name))
        if enemy.health <= 0:
            print("The {} is dead.".format(enemy.name))
        print("{} counters with {} damage to the {}.".format(enemy.name, enemy.power * damage_mulitplier, self.name))
        self.power -= enemy.power * damage_mulitplier

        if rand_heal == 1:
            self.health += 2
            print('{} was healed +2 by the medic. What a nice medic.'.format(self.name))
            print('{} now has {} power.'(self.name, self.power))

        if enemy.name == 'Zombie':
            


    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    def __init__(self, power, health, name, double_power):
        super().__init__(power, health, name)
        self.double_power = 10

    def attack(self, enemy):
        rand_attack = random.randint(1,5)
        if rand_attack == 1:
            enemy.health -= self.double_power
            print("{} does double damage ({}) to the {}.".format(self.name, self.double_power, enemy.name))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.name))
        else:    
            enemy.health -= self.power
            print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
            if enemy.health <= 0:
                print("The {} is dead.".format(enemy.name))
        

class Goblin(Character):
    def __init__(self, power, health, name, ):
        super().__init__(power, health, name)


class Medic(Character):
    def __init__(self, power, health, name, heal):
        super().__init__(power, health, name)
        self.heal = 2
    def heal_hero(self, hero):
        rand_heal = random.randint(1,5)
        if rand_heal == 1:
            hero.health += 2
            print("The {} has been healed +{} by the medic.")
        

class Shadow(Character):
    def __init__(self, power, health, name, evade):
        super().__init__(power, health, name)
        self.evade = evade
    def evasive_maneuver(self):
        rand_evade = random.randint(1, 10)
        if rand_evade == 1:
            print("{} has made an evasive maneuver! ")

class Zombie(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)

class Sharknado(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)

class Angry_beaver(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)

def main():
    hero = Hero()
    goblin = Goblin()

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

