#import random module
import random
#Create Subjects
Subjects = [
    "Shah Rukh khan",
    "Salman Khan",
    "Modi ji"
    "",
    "Ms Dhoni",
    "Jeffery Epstien",
    "Doland Trump"
]
#Create Actions
Actions = [
    "launches",
    "cancels",
    "eats",
    "Declared wars",
    "Blowed at",
    "celebrates",
    "orders"
]
#Create Objects
Objects = [
    "at red Fort",
    "at My house",
    "Through mirror",
    " modi ji"
    "",
    "in a jar ",
    "in dancing car",
    "in Pants"
]
#Start Loop
while True:
     sub = random.choice(Subjects)
     act = random.choice(Actions)
     obj = random.choice(Objects)

     headline = f"Breaking News :{sub} {act} {obj}."
     print(headline)

     user = input("Next Headline :").strip().lower()
     if user == "n":
         break
print("Thanks For the Reading Our news")
