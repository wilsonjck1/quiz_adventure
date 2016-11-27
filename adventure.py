# An adventure game
from random import randint

health = 100
gold = 0
if input == "balance".lower():
   print(gold)

def space():
   print(" ")
   print("Health: ", health, "Gold: ", gold)
   print(" ")


def startingroom():

    global health
    global gold
    print("In the distance you see a treasure chest that could contain some loot and you decide to open it")
    chest = randint(1, 2)

    if chest == 1:
        print("You have been rewarded with 10 gold, this could be useful later in your quest")
        gold = gold + 10
        room1()
    else:
        print("You found nothing")
        room1()

   
def room1():
    space()
    print("You have left the starting room and are faced with 2 doors")
    print("You can only choose one door")
    print("door A leads to a dungeon")
    print("door B leads to a tomb")
    print("Which door do you enter")

    door = input("Door: ")

    if door.lower() == "a":
       print("entering...")
       dungeon()

    elif door.lower() == "b":
         print("entering...")
         tomb()

def dungeon():
   space()
   print("This route is blocked off, im afraid you have to head back and enter the crypt")
   tomb()

    
def tomb():
   space()
   global health
   restless_skeleton_hp = 30
   restless_skeleton_damage = randint(10,20)
   damage = randint(10,30)
   hit_chance = randint(1,3)
   print("You have entered the tomb!!!")
   print("You hear a voice in the distance...")
   print("Restless skeleton: HOW DARE YOU ENTER MY TOMB!!!")
   print("Self conscience: oh no i need to find a weapon!")
   print("Ahead of you there is two weapons")
   print("A) a rusted sword")
   print("B) or a hunting bow")
   print("You can only choose one weapon to fight the Restless skeleton, choose wisely")

   weapon = input("Weapon: ")
   
   if weapon.lower() == "a":
      print("You have equiped the rusted sword")
      print("You walk towards the skeleton")



      print("The restless skeleton sudenly attacks")
      if restless_skeleton_damage == 0:
             print("You evaded his attack")
      else:
              print("You got hit")
              health = health - restless_skeleton_damage


      if 10<= damage <=15:
              print("You slice your sword into the skeletons chest, but dont kill it")
              print("it goes for another attack")
              print("your health is", health)
              restless_skeleton_hp = restless_skeleton_hp - damage

            
      if 15< damage <=20:
              print("You stab your sword into the skeletons chest, but dont kill it")
              print("it goes for another attack")
              print("your health is", health)
              restless_skeleton_hp = restless_skeleton_hp - damage

      else:
            print("You have slaughtered the skeleton and head towards the exit")
            print("your health is", health)
            print("exiting")
            merchant()
            

      if health <= 0:
             print("You died, try again")
             


   if weapon.lower() == "b":
      print("You have equiped the hunting bow")
      print("You walk  towards the skeleton")



      print("The restless skeleton sudenly attacks")
      if restless_skeleton_damage == 0:
             print("You evaded his attack")
      else:
              print("You got hit")
              health = health - restless_skeleton_damage


      if 10<= damage <=15:
              print("Your arrow scathes the skeletons arm, but dont kill it")
              print("it goes for another attack")
              print("your health is", health)
              restless_skeleton_hp = restless_skeleton_hp - damage

            
      if 15< damage <=20:
              print("Your arrow slices through the skeletons head, but somehow youdont kill it")
              print("it goes for another attack")
              print("your health is", health)
              restless_skeleton_hp = restless_skeleton_hp - damage

      else:
            print("You have slaughtered the skeleton and head towards the exit")
            print("your health is", health)
            print("exiting")
            merchant()

      if health <= 0:
             print("You died, try again")

def merchant():
   global health
   global gold
   space()
   print("〠hola my friend〠")
   print("Welcome to geralds gracious goods")
   print("Would you like to purchase a health potion my jolly good friend")
   print("A) Yes")
   print("B) No")

   answer = input("Answer: ")

   if answer.lower() == "a":
    print("Do you have the gold my friend?")
    print("...")

    if gold == 10:
      print("Ah yes you do, here you go, enjoy the potion!")
      print("... 10 Gold coins removed ...")
      bossroom()

    if gold == 0:
       print("Im afraid you havent got the gold my friend, potter along and earn money you peasant")

   if answer.lower() == ("b"):
       print("You're really missing out my friend!")
       print("Goodbye! Have great time and enjoy your inevitable death which could have been prevented had you bought one of gerald's gracious goods potions")
       bossroom()




def bossroom():
    global health
    global gold
    gold = gold - 10
    giant_hp = 100
    giant_damage = randint(10,30)
    damage = randint(10,30)
    hit_chance = randint(1,3)
    space()
    
     
    print("your health is only", health, "would you like to drink your potion now or save it until later?")
    print("A) Yes")
    print("B) No")

    answer = input("Answer: ")

    if answer.lower() == "a":
     health = health + 50
    print("Health regenerating... your health is now", health,)

    if answer.lower() == "b":
       print("Storing Health potion...")
 

    print(" ")
    print(" ")
    print("In the distance you hear a groan..")
    print("You head towards the peculiar noise to investigate")
    print("In the distance you see a Giant and decide to attack it")


    print("The Giant see's you and suddenly attacks")

    while giant_hp > 0 and health is 0:
       
     if giant_damage == 0:
       print("You evaded his attack")
     else:
       print("You got hit")
       health = health - giant_damage


     if 10<= damage <=15:
       print("You slice your sword into the skeletons chest, but dont kill it")
       print("it goes for another attack")
       print("your health is", health)
       giant_hp = giant_hp - damage

            
     if 15< damage <=20:
       print("You stab your sword into the skeletons chest, but dont kill it")
       print("it goes for another attack")
       print("your health is", health)
       giant_hp = giant_hp - damage

     if 20< damage <= 30:
       print("You landed a critical hit on the giant")

     else:
       print("You have slaughtered the skeleton and head towards the exit")
       print("your health is", health)
       print("exiting")
       quit()
            

     if health <= 0:
       print("You died, try again")

    
    

   
   


# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    startingroom()
    
