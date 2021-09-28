#PIZZACALCULATOR 1.1 BY FELIXTEK
refflour = 625
refsalt = 1
refsugar = 15
refyeast = 2
refwater = 300
refoil = 35

def calcpizzaingred():
    try:
        flour = int(input("Insert desired flour use (in grams)\n > "))
        salt = refsalt * (flour / refflour)
        sugar = refsugar * (flour / refflour)
        yeast = refyeast * (flour / refflour)
        water = refwater * (flour / refflour)
        oil = refoil * (flour / refflour)
        print("You need:\n", salt, " tsp. of salt\n", sugar, "g. of sugar\n", yeast, "tbsp. of yeast\n", water,
              "cc. of water\n", oil, "g. of rice bran oil\n")
        exit()
    except: # catch *all* exceptions
        print("Value error")
        calcpizzaingred()

def exit():
    endapp = input("Calculate another pizza recipe? (y/n)")
    endapp = endapp[0]
    endapp = endapp.lower()
    if endapp == "y":
        calcpizzaingred()
    elif endapp == "n":
        print("Exiting program...")
    else:
        print("Invalid selection")
        exit()



calcpizzaingred()