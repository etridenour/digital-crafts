
import random

class Character:
    def __init__(self, power, health, name):
        self.power = power
        self.health = health
        self.name = name

    def attack(self, enemy):
        # if enemy_death_count == 0:
        #     enemy.name = 'Goblin'
        # elif enemy_death_count == 1:
        #     enemy.name = 'Shadow'
        # elif enemy_death_count == 2:
        #     enemy.name = 'Zombie'
        # elif enemy_death_count == 3:
        #     enemy.name = 'Sharknado'
        # elif enemy_death_count == 4:
        #     enemy.name = 'Angry Beaver'
        hero_damage_multiplier = 1
        enemy_damage_multiplier = 1
        rand_heal = random.randint(1,5)
        if enemy.name == 'Shadow':
            rand_evade = random.randint(1, 10)
            if rand_evade > 1:
                print("{} makes an evasive maneuver".format(enemy.name))
                hero_damage_multiplier = 0
                
            else:
                enemy.health -= self.power
        if enemy.name == 'Goblin':
            rand_block = random.randint(1, 3)
            if rand_block == 1:
                print('The {} blocked {}\'s attack.'.format(enemy.name, self.name))
                hero_damage_multiplier = 0
            else:
                enemy.health -= self.power

        if enemy.name == 'Sharknado':
            rand_sweep = random.randint(1,4)
            if rand_sweep == 1:
                print("The {} swept up {}.".format(enemy.name, self.name))
                enemy_damage_multiplier = 5
            else:
                enemy.health -= self.power


        if enemy.name == 'Zombie':
            enemy.health -= self.power
            


        if enemy.name == "Angry Beaver":
            rand_angry = random.randint(1,3)
            if rand_angry == 1:
                print('The {} is super angry!'.format(enemy.name))
                enemy_damage_multiplier = 2
            else:
                enemy.health -= self.power

        rand_attack = random.randint(1,5)
        if hero_damage_multiplier == 0:
            pass
        elif rand_attack == 1:
            hero_damage_multiplier = 2
            print('The {} hit with double power!'.format(self.name))
            enemy.health -= self.power * hero_damage_multiplier

        print("{} does {} damage to the {}.".format(self.name, self.power * hero_damage_multiplier, enemy.name))
        if enemy.health <= 0:
            if enemy.name == 'Goblin':
                print("The {} is dead.".format(enemy.name))
                print('It\'s body quickly decomposes into the ground, emitting a pungent odor.')
                self.coins += enemy.bounty
                print("{} is rewarded with a bounty of {} coins for slaying the evil {}.".format(self.name, enemy.bounty, enemy.name))
                print()
                print('Shadow quickly approches to battle!')
            if enemy.name == 'Shadow':
                print("The {} is dead.".format(enemy.name))
                print('It\'s body vaporizes into into thin air.')
                self.coins += enemy.bounty
                print("{} is rewarded with a bounty of {} coins for slaying the evil {}.".format(self.name, enemy.bounty, enemy.name))
                print()
                print('The zombie slowly stumbles up for an attack!')
            if enemy.name == 'Sharknado':
                print("{} is dead.".format(enemy.name))
                print('It dissipates high in the sky, launching sharks all over the place.')
                self.coins += enemy.bounty
                print("{} is rewarded with a bounty of {} coins for slaying the evil {}.".format(self.name, enemy.bounty, enemy.name))
                print()
                print('Emerging from a nearby dam comes an Angry Beaver, the final enemy!')
        elif enemy.name == 'Zombie':
            print("{} counters with {} damage to {}.".format(enemy.name, enemy_damage_multiplier * enemy.power, self.name))
            self.health -= enemy_damage_multiplier * enemy.power
            if enemy.health <= 0:
                print("You can't kill the {}!".format(enemy.name))

        else:
            print("{} counters with {} damage to {}.".format(enemy.name, enemy_damage_multiplier * enemy.power, self.name))
            self.health -= enemy_damage_multiplier * enemy.power

        if self.health <= 0:
            print("{} is dead.".format(self.name))
            print("GAME OVER")
        
        if rand_heal == 1:
            self.health += 2
            print('{} was healed +2 by the medic. What a nice medic.'.format(self.name))
            
            



    def alive(self):
        if self.name == "Zombie":
            return True
        elif self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))


class Hero(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name)
        self.coins = coins
        
    
class Tonic:
        cost = 5
        name = 'Tonic'
        def use(self, hero):
            hero.health = 10
            print('{} has been restored to full health.'.format(hero.name))
            
class Armor:
        cost = 5
        name = 'Armor'
        def use(self, hero):
            hero.armor = 2

class Evade:
    cost = 5
    name ='Evade'
    def use(self, hero):
        hero.evade = 2

def buy_stuff(self):
    while True:
        print('Welcome to the store.')
        print('You have {} coins.'.format(hero.coins))
        print()
        print('We have:')
        print('1. Tonic - bring health back to full strength.')
        print('2. Armor - increase ability to receive damage')
        print('3. Evade - increase ability to evade enemy attack')
        print('4. Energy Sword - increase attack strength')
        print('5. Bazooka - blow up your enemy')
        print()
        print('What would you like to purchase? (1-5)')
        choice = input('>')
            

    # def attack(self, enemy):
    #     rand_attack = random.randint(1,5)
    #     if rand_attack == 1:
    #         enemy.health -= self.double_power
    #         print("{} does double damage ({}) to the {}.".format(self.name, self.double_power, enemy.name))
    #         if enemy.health <= 0:
    #             print("The {} is dead.".format(enemy.name))
    #     else:    
    #         enemy.health -= self.power
    #         print("{} does {} damage to the {}.".format(self.name, self.power, enemy.name))
    #         if enemy.health <= 0:
    #             print("The {} is dead.".format(enemy.name))
        

class Goblin(Character):
    def __init__(self, power, health, name, bounty):
        super().__init__(power, health, name)
        self.bounty = 5


class Medic(Character):
    def __init__(self, power, health, name, heal):
        super().__init__(power, health, name)
   
        

class Shadow(Character):
    def __init__(self, power, health, name, bounty):
        super().__init__(power, health, name)
        self.bounty = 10


class Zombie(Character):
    def __init__(self, power, health, name):
        super().__init__(power, health, name)

class Sharknado(Character):
    def __init__(self, power, health, name, bounty):
        super().__init__(power, health, name)
        self.bounty = 15

class Angry_beaver(Character):
    def __init__(self, power, health, name, bounty):
        super().__init__(power, health, name)
        self.bounty = 7

# class Store:
#     def __init__(self, tonic, armor, evade, sword, bazooka):
#         self.tonic = tonic
#         self.armor = armor
#         self.evade = evade
#         self.sword = sword
#         self.bazooka = bazooka

#     def buy_stuff(self):
#             print('Welcome to the store.')
#             print()
#             print('We have:')
#             print('1. Tonic - bring health back to full strength.')
#             print('2. Armor - increase ability to receive damage')
#             print('3. Evade - increase ability to evade enemy attack')
#             print('4. Energy Sword - increase attack strength')
#             print('5. Bazooka - blow up your enemy')
#             print()
#             print('What would you like to purchase? (1-5)')
#             choice = input('>')


hero = Hero(5, 50, 'Galactar', 20, 0)
goblin = Goblin(2, 10, "Goblin", 5)
shadow = Shadow(3, 1, "Shadow", 7)
zombie = Zombie(2, 5, 'Zombie')
sharknado = Sharknado(5, 17, 'Sharknado', 12)
angry_beaver = Angry_beaver(3, 12, "Angry Beaver", 5)

print('********************************************************')
print("Galactar\'s Hardest Mission - Escape from Beaver Lodge")
print('********************************************************')
print()

def main(hero, enemy):
    while hero.alive():
        zombie_done = False
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. Fight {}".format(enemy.name))
        print("2. Do nothing")
        print("3. Flee")
        print("4. Go to store")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
            
        elif raw_input == "2":
            hero.health -= enemy.power
            print('{} attacked {}. Better do something!'.format(enemy.name, hero.name))
            
        elif raw_input == "3":
            if enemy == zombie:
                print('Good idea. You can\'t kill the Zombie!')
                print()
                print('{} walks into an open field. The air starts swirling violently.'.format(hero.name))
                print('Out of nowhere appears....Sharknado!')
                enemy = sharknado

            else:
                print("The {} runs away. Not much of a hero.".format(hero.name))
                print("GAME OVER")
                break
            
        elif raw_input == '4':
            hero.buy_stuff()
        else:
            print("Invalid input {}".format(raw_input))
        if enemy == sharknado:
            zombie_done = True
        elif enemy == angry_beaver:
            zombie_done = True
        else:
            zombie_done = False
        if goblin.health <= 0:
            enemy = shadow
        if shadow.health <= 0:
            enemy = zombie
        if zombie_done == True:
            enemy = sharknado
        if sharknado.health <= 0:
            enemy = angry_beaver
        if angry_beaver.health <= 0:
            print("{} deafeated the powerful Angry Beaver. You win!".format(hero.name))
            break
        

main(hero, goblin)



