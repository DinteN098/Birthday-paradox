import random

#this is the list of the months
months = ["Jan", "Feb", "Mar", "Apr", "May", "jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#this is where the created birthdays will be stored
birthdays = []

active = True

#amount of birthdays that the user wants
bday_amount = int(input("How many birthdays shall I generate? (Max 100)\n"))
if bday_amount > 100:
    active = False

#function that will create random birthdays
def get_random_bday():
    month = random.choice(months) 
    day = random.randint(1,31)
    birthday = f"{month} {day}"
    birthdays.append(birthday)

#this is where the amount of birthdays that are repeated will be stored
matching = []

#function to add number of matched birthdays to the list 'matching'
def matchedBdays(): 
    matched = 0
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:                
                matched = 1
                return matching.append(matched)

#function that finds repeated birthdays
def repeatedBday(): 
    for i in range(len(birthdays)):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:                
                return print(f"in the simulation, multiple people have a birthday on {birthdays[i]}")

#amount of simulations that the user wants
simulations = int(input("how many simulations do you want to run?"))

#loop to make the script run the code
for a in range(simulations):
  for b in range(bday_amount):
   get_random_bday()
  print(f"Here is {len(birthdays)} birthdays:\n{birthdays}")
  repeatedBday()
  matchedBdays()
  birthdays = []

#total amount of birthdays that matched
totalMatched = sum(matching)
#chances that people share the same birthday
probability = (totalMatched/simulations)*100

print(f"in {simulations} different cases there is a {round(probability, 2)}% chance that {bday_amount} people in a room have the same birthday")