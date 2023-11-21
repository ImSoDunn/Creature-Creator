import random                   #Import random module to choose bewteen characteristics
import time                     #Imports time module for sleep() method
import os                       #Imports os for terminal clear
from random import choice       #Specifically imports choice from the random module
from art import *               #Imports everything that is not a private variable from the art 5.5 ASCII Art Library 

#Clears terminal for a cleaner output
os.system('cls||clear')


#Define creature class
class Creature:
    #Initialize a Creature object with a name, weight, food, activity and color.
    def __init__(self, name, weight, food, activity, color):
        self.name = name
        self.weight = weight
        self.food = food
        self.color = color
        self.activity = activity

    #Displays info for chosen creature
    def printInfo(self):
        print(text2art("\nThis creature has a name of {}. Weighs {} pounds, eats {}, loves to {}, and is colored {}\n".format(self.name.title(), self.weight, self.food, self.activity, self.color), 'scammer'))

#Defining predetermined creatures
unicorn = Creature("Unicorn", 500, "stardust and rainbows", "run on rainbows and grant wishes",  "white or pink")
bat = Creature("Bat", 2, "blood", "fly around in the night", "black")
chimpanzee = Creature("Chimpanzee",150 , "meat or fruits", "climb trees and play", "black")
lion = Creature("Lion", 400, "other animals", "hunt gazelle and lead a pack", "golden yellow")
shark = Creature("Shark", 1500, "what ever it wants", "swim in the ocean", "blueish white")
greatWhiteShark = Creature("Great White Shark", 2400, "helpless divers", "swim in the ocean and appear briefly in 90s movies", "blue")
hummingBird = Creature("Humming Bird", 0.006, "sweet sweet flower nectar", "zip around and find nectar", "a brilliant display of reds, purples, greens and blues")
bear = Creature("Bear", 600 , "honey or hikers", "sleep in dens and eat honey", "brown")
horse = Creature("Horse", 660, "grass", "run on the plains and be free", "brown")
chicken = Creature("Chicken", 10, "seeds", "peck at the ground", "brown and white")
cat = Creature("Cat", 10 , "fish", "push cups off of counter tops", "black")
kraken = Creature("Kraken", 4000, "boats that have strayed too far from the well traveled path", "sit at the bottom of the ocean and lie in wait", "green")
griffin = Creature("Griffin", 500 , "goats and other unsuspecting animals", "fly around and yell", "yellowish brown")
golem = Creature("Golem", 700, "nothing", "protect their owner", "grey" )
cyclops = Creature("Cyclops", 1200, "goats and sheep", "live on an island and harrass greek travelers", "grey")
ogre = Creature("Ogre", 500 , "mostly onions but the occasional loud mouth donkey", "soak in mud and made candles out of earwax", "green")
leprechauns = Creature("Leprechaun", 30, "wildflowers or nuts and beer", "hide gold", "a wide variation of skin tones")
dragon = Creature("Dragon", 10000, "mostly goats and sheep but the occasional greedy dwarf", "hide in mountains, and sleep on massive piles of gold and precious stones", "any variation of red, green, gray, and brown")
mermaid = Creature("Mermaid", 170, "fish and sea plants", "either lure sailors to their death or play and have a joy filled life in the ocean, we aren't really sure", "a shimmering blue")
werewolf = Creature("Werewolf", 250, "any animal though mostly deer", "resist the blood lust that comes with each full moon", "black or brown")
fairy = Creature("Fairy", 1, "mushrooms and forest nuts", "fly around and cause mischief", "pink or gold")
centaur = Creature("Centaur",800 , "meats and plants", "hunt wild animals and ride the line between human and animal", "a wide variation of skin tones")
yeti = Creature("Yeti", 900, "local wildlife and plants", "get captured in grainy and quite frankly unrecognizable photos", "mostly white or brown fur")
ghoul = Creature("Ghoul", 200, "human flesh", "hang around graveyards on the prowl for their next meal", "a dead grey or red")
basilisk = Creature("Basilisk",5000 , "hunt animals and slink around", "stare into peoples eyes, possibly at accredited magic universities", "a deep greenish blue")

#Allows user to add custom creature to the list.
def addCreature():
    customAnswer = input(text2art("\nBefore we start would you like to make your own custom creature for combining? Enter 'Y' or 'y' for yes.", 'scammer')) #slammer, scammer
    #Allows the user to create as many custom creatures as they would like.
    while ((customAnswer == 'Y') or (customAnswer == 'y')):
        tempName = input(text2art("Enter the type of creature: ", 'scammer'))
        tempName = tempName.title()

        tempWeight = input(text2art("Enter your creatures weight: ", 'scammer'))
        tempFood = input(text2art("Enter your creatures food of choice: ", 'scammer'))
        tempActivity = input(text2art("Enter your creatures hobby: ", 'scammer'))
        tempColor = input(text2art("Enter your creatures color: ", 'scammer'))
        tempCreature = Creature(tempName, tempWeight, tempFood, tempActivity, tempColor)

        #Inserts creature at the front of the list. If a custom creature is created it will most likely be chosen. This cuts down on loop iteration later in the program.
        creatures.insert(0,tempCreature)
        creaturesNames.insert(0, tempCreature.name)
        customAnswer = input(text2art("Would you like to make another? 'Y' or 'y' for yes. Any other for no", 'scammer'))

#Defines a function to print avaiable creatures for choosing
def printCreatures():
        print((", ").join(creaturesNames))

#A working list of the current creatures to choose from
creatures = [unicorn, bat, chimpanzee, lion, shark, greatWhiteShark, hummingBird, bear, horse, chicken, cat, kraken, griffin,
            golem, cyclops, ogre, leprechauns, dragon, mermaid, centaur, werewolf, fairy, yeti, basilisk]
creaturesNames = []

#Appends the object creature names to a list specifically for the names
for el in creatures:
    creaturesNames.append(el.name)

#Displays creatures for use
print(text2art("These are the creatures you have to choose from: ", "scammer"), end='')
printCreatures()

#A call to custom object creation
addCreature()
#Slows the program down a bit to help with fluidity
time.sleep(1)


#Sets up the while loop to run as long as the user wishes
ch = 'y'
while ((ch == 'y') or (ch =='Y')):

    #Prints header
    print(text2art("\n\nWelcome to the Creature Creator\n", "slammer")) #epic, doom, slammer

    #prints available creatures to choose from
    print(text2art("Here are the creatures that can be used for your sick enjoyement: ", 'scammer'), end='')
    printCreatures()
    print()

    #Asks user for a creature selection and formats the input
    choice1 = input(text2art("\n---What is your first selection?---\n", 'slammer')) #ghoulish, doom , epic, fire_font-s
    choice1 = choice1.title()
    choice1 = choice1.strip()

    #Checks if first choice is a valid creature
    while (choice1 not in creaturesNames):
        choice1 = input(text2art("Thats is not a valid selection pick a creature from the list.", 'scammer'))
        choice1 = choice1.title()
        choice1 = choice1.strip()

    #Finds choice2 in creatures list and creates spliced name.
    for creature in creatures:
        if choice1.title() == creature.name:
            creature1 = creature
            name1 = choice1
            if (len(name1) > 3):
                name1Slice = name1[0:3]
            else:
                name1Slice = name1
            break

    #Asks user for a second creature selection and formats the input
    choice2 = input(text2art("\n---What is your second selection?---\n", 'slammer')) #contessa , double, drpepper, ghoulish
    choice2 = choice2.title()
    choice2 = choice2.strip()

    #Checks if valid creature is given
    while (choice2 not in creaturesNames):
        choice2 = input(text2art("That is not a valid creature. Enter a valid creature from the list.", 'scammer'))
        choice2 = choice2.title()
        choice2 = choice2.strip()

    #Finds choice2 in creatures list and creates spliced name.
    for creature in creatures:
        if choice2.title() == creature.name:
            creature2 = creature
            name2 = choice2
            if (len(name2) > 3):
                name2Slice = name2[3:]
            else:
                name2Slice = name2
            break

    #Art for before the combination of the two chosen creatures
    print(text2art("\n-----------Now Combining-----------", "slammer")) # doom, fire_font-s, #fantasy2 for loading icon
    
    #Simulate loading of the creature
    for num in range(1,7): 
        print(text2art("gfaspq", 'fantasy2'), end='', flush=True)
        time.sleep(random.uniform(0.1, 0.7))
    print("")
    os.system('cls||clear')


    # Prints chosen creatures
    print(text2art("\n\n" + name1.title() + "           +              " + name2.title(), 'scammer'))
    print(text2art(("\n             " + name1Slice + name2Slice).title(), 'scammer'))



    #Assigns attributes to the hybrid, randomized between both chosen creatures
    hybrid = Creature((name1Slice + name2Slice).title(), random.choice((creature1.weight, creature2.weight)), 
                    random.choice((creature1.food, creature2.food)), random.choice((creature1.activity, creature2.activity)),
                    random.choice((creature1.color, creature2.color)))
    #Prints hybrid info
    hybrid.printInfo()
    creatures.append(hybrid)
    creaturesNames.append(hybrid.name)

    #Determines whether loop repeats or not
    ch = input(text2art("Would you like to make another vile abombination? 'Y' or 'y' to continue. Any other character to quit.", 'scammer'))
    #Clears the terminal to make output more legible.
    #os.system('cls||clear')

#Prints when loop has terminated.
print(text2art("\nThank you for participating in this experiment.\n", 'slammer'))
quit()
