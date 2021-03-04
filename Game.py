from random import *
class Player():
    def __init__(self,name = None,level = 1, gold = 0, expirience = 0, skill_point = 0,
                 race = None, max_health = 0,health = 0, strenght = 0, agility = 0, intelligence = 0):
        self.level = level
        self.gold = gold
        self.expirience = expirience
        self.skill_point = skill_point
        self.name = name
        self.max_health = max_health
        self.health = health
        self.strenght = strenght
        self.agility = agility
        self.intelligence = intelligence
        self.race = race
def elf():
        Player.max_health+=8
        Player.strenght+=2
        Player.agility+=4
        Player.intelligence+=3
        Player.race = "Elf"

def human():
        Player.max_health+=10
        Player.strenght+=4
        Player.agility+=2
        Player.intelligence+=2
        Player.race = "Human"      

class Monster():
    def __init__(self,level, gold,health, strenght, agility, intelligence):
    self.level = level
    self.gold = gold
    self.health = health
    self.strenght = strenght
    self.agility = agility
    self.intelligence = intelligence



        
def game():
    print("What's you name:")
    Player.name = str(input())
    print("~~~~~~~~~~~~~~~")
    print("Hi {}!".format(Player.name))
    print("Chose you race:")
    print("Human : give you more helth and power")
    print("Elf : give you more agility and intelligence")
    print("write your anser(only one of race)")
    print("~~~~~~~~~~~~~~~")
    result = input(str()).lower
    if result == "human":
        human()
    elif result == "elf":
        elf()

palyer = Player()
monster = Monster()
game()

def fight(monster,player):
    

def leveling(player_expirience):
    exp_for_new_level = 100
    if player.expirience >= exp_for_new_level:
        print("You have new level")
        player.level+=1
        player.skill_point+=4
        exp_for_new_level = exp_for_new_level*2
     else:
         return
        
def uppgrade_stats(player_skill_point):
    print("please choose you skill's\nnow you skill_point = {} write 1 if you whant add 1sp at strenght \n write 2 if you whant add 1sp at intelligence\n"+
    +"write 3 if you whant add 1sp at agility \n ".format(player.skill_point))
    i = int(input())
    while player.skill_point>0:
        if i == 1:
            player.strenght+=1
            player.skill_point = player.skill_point-1
        elif i == 2:
            player.intelligence+=1
            player.skill_point = player.skill_point-1
        elif i == 3:
            player.agility+=1
            player.skill_point = player.skill_point-1
        else:
            brake
    
#def combatpower(strenght,intelligence,agility):
    #for i in player.strenght:
        #damage+=2
        #player.max_health+=2
    #for i in payer.intelligence:
        #crit_damage+=0.05
        #anti_crit_damage+=0.05
    #for i in player.agility:
        #dodge+=0.05
        #anti_dodge+=0.05
            
            #level = randit(1,player.level)
    #health = randit(player.health,player.max_health+10)
    #damage = randit((5+player.strenght*2),(10+player.strenght*2))
        
