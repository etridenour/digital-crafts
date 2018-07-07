
import random

class Character:
    def __init__(self, power, health, name):
        self.power = power
        self.health = health
        self.name = name

    def attack(self, enemy):
        hero_damage_multiplier = 1
        enemy_damage_multiplier = 1
        rand_heal = random.randint(1,5)
        armor_multiplier = 1
        if enemy.name == 'Shadow':
            rand_evade = random.randint(1, 10)
            if rand_evade > 1:
                print("{} makes an evasive maneuver".format(enemy.name))
                hero_damage_multiplier = 0
                
            else:
                pass
        elif enemy.name == 'Goblin':
            rand_block = random.randint(1, 3)
            if rand_block == 1:
                print('The {} blocked {}\'s attack.'.format(enemy.name, self.name))
                hero_damage_multiplier = 0
            else:
                pass

        elif enemy.name == 'Sharknado':
            rand_sweep = random.randint(1,4)
            if rand_sweep == 1:
                print("The {} swept up {}.".format(enemy.name, self.name))
                enemy_damage_multiplier = 5
            else:
                pass
            
        elif enemy.name == "Angry Beaver":
            rand_angry = random.randint(1,3)
            if rand_angry == 1:
                print('The {} is super angry!'.format(enemy.name))
                enemy_damage_multiplier = 2
            else:
                pass

        rand_attack = random.randint(1,5)
        if hero_damage_multiplier == 0:
            pass
        elif self.sword > 0:
            hero_damage_multiplier = 3
            print('{} attacked {} with the sword for triple power!'.format(self.name, enemy.name))
            self.sword -= 1
        elif self.bazooka > 0:
            hero_damage_multiplier = 25
            print('{} blew up {} with the bazooka!'.format(self.name, enemy.name))
            self.bazooka -= 1
        elif rand_attack == 1:
            hero_damage_multiplier = 2
            print('{} attacked {} with double power!'.format(self.name, enemy.name))
            
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
            elif enemy.name == 'Shadow':
                print("The {} is dead.".format(enemy.name))
                print('It\'s body vaporizes into into thin air.')
                self.coins += enemy.bounty
                print("{} is rewarded with a bounty of {} coins for slaying the evil {}.".format(self.name, enemy.bounty, enemy.name))
                print()
                print('The zombie slowly stumbles up for an attack!')
            elif enemy.name == 'Sharknado':
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
            if self.evade > 5:
                hero_evade_1 = random.randint(1, 10)
                if hero_evade_1 == 1:
                    print('{} makes an evasive maneuver!'.format(self.name))
                    enemy_damage_multiplier = 0
                else:
                    pass
            if self.evade > 3:
                hero_evade_2 = random.randint(1, 5)
                if hero_evade_2 == 1:
                    print('{} makes an evasive maneuver!'.format(self.name))
                    enemy_damage_multiplier = 0
            if self.evade > 1:
                hero_evade_3 = random.randint(1, 3)
                if hero_evade_3 == 1:
                    print('{} makes an evasive maneuver!'.format(self.name))
                    enemy_damage_multiplier = 0
                else:
                    pass
            else:
                pass

            if self.armor > 1:
                armor_multiplier = .90
            elif self.armor > 3:
                armor_multiplier = .80
            elif self.armor > 5:
                armor_multiplier = .70
            print("{} counters with {} damage to {}.".format(enemy.name, enemy_damage_multiplier * enemy.power * armor_multiplier, self.name))
            self.health -= (enemy_damage_multiplier * enemy.power * armor_multiplier)

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
    def __init__(self, power, health, name, coins, armor, evade, sword, bazooka):
        super().__init__(power, health, name)
        self.coins = coins
        self.armor = armor
        self.evade = evade
        self.sword = sword
        self.bazooka = bazooka
    
    
    def print_status(self):
        print("{} has {} health, {} power, {} armor, {} evade, {} sword, and {} bazooka.".format(self.name, self.health, self.power, self.armor, self.evade, self.sword, self.bazooka))

    def buy_stuff(self):
        print()
        print('Welcome to the store.')
        while self.coins > 0:
            print()
            print('You have {} coins.'.format(hero.coins))
            print()
            print('Items for sale:')
            print('1. Tonic (5 coins)- bring health back to full strength.')
            print('2. Armor (5 coins) - increase ability to receive damage')
            print('3. Evade (5 coins)- increase ability to evade enemy attack')
            print('4. Energy Sword (10 coins)- increase attack strength by 3 times (one time use)')
            print('5. Bazooka (15 coins) - blow up your enemy (one time use)')
            print('6. Exit')
            print()
            print('What would you like to purchase? (1-6)')
            choice = int(input('> '))
            print()
            if choice == 1:
                hero.use_tonic()
            elif choice == 2:
                hero.use_armor()
            elif choice == 3:
                hero.use_evade()
            elif choice == 4:
                hero.use_sword()
            elif choice == 5:
                hero.use_bazooka()
            elif choice == 6:
                break
        else:
            print('You have no coins.')
            print('Goodbye.')
            print()
        
    def use_tonic(self):
        if self.coins < 5:
            print('You don\'t have enough coins.')
        else:
            hero.health = 10
            self.coins -= 5
            print('{} has been restored to full health.'.format(hero.name))
            self.print_status()

    def use_armor(self):  
        if self.coins < 5:
            print('You don\'t have enough coins.')      
        else:
            self.coins -= 5
            self.armor += 2
            print('{} now has +2 armor.'.format(hero.name))
            self.print_status()

    def use_evade(self):
        if self.coins < 5:
            print('You don\'t have enough coins.') 
        else:
            self.coins -= 5
            self.evade += 2
            print('{} now has +2 evade.'.format(hero.name))
            self.print_status()

    def use_sword(self):
        if self.coins < 10:
            print('You don\'t have enough coins.') 
        else:
            self.coins -= 10
            self.sword += 1
            print('{} now has a sword.'.format(hero.name))
            self.print_status()

    def use_bazooka(self):
        if self.coins < 15:
            print('You don\'t have enough coins.') 
        else:
            self.coins -= 15
            self.bazooka += 1
            print('{} now has a bazooka.'.format(hero.name))
            self.print_status()
        

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


hero = Hero(5, 10, 'Galactar', 20, 0, 0, 0, 0)
goblin = Goblin(2, 10, "Goblin", 5)
shadow = Shadow(3, 1, "Shadow", 7)
zombie = Zombie(2, 6, 'Zombie')
sharknado = Sharknado(5, 15, 'Sharknado', 12)
angry_beaver = Angry_beaver(3, 20, "Angry Beaver", 5)

print()
print('******************************************************')
print("Fight Game - Galactar Fights A Bunch of Random Enemies")
print('******************************************************')
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
                print("{} runs away. Not much of a hero.".format(hero.name))
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
            print("{} deafeated the powerful Angry Beaver.".format(hero.name))
            print('YOU WIN!')
            break
        
main(hero, goblin)



