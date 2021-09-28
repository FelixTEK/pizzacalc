#PIZZACALCULATOR 1.1 BY FELIXTEK
refflour = 625
refsalt = 1
refsugar = 15
refyeast = 2
refwater = 300
refoil = 35

def calcpizzaingred():
    try:
        while True:
            flour = int(input("Insert desired flour use (in grams)\n > "))
            salt = refsalt * (flour / refflour)
            sugar = refsugar * (flour / refflour)
            yeast = refyeast * (flour / refflour)
            water = refwater * (flour / refflour)
            oil = refoil * (flour / refflour)
            print("You need:\n", salt, " tsp. of salt\n", sugar, "g. of sugar\n", yeast, "tbsp. of yeast\n", water,
              "cc. of water\n", oil, "g. of rice bran oil\n")
            break
        exitPrompt()
    except Exception as e:
        print("Error: "+str(e))
        pass

def exitPrompt():
    while True:
        endapp = input("Calculate another pizza recipe? (y/n)\n > ")
        #endapp = endapp[0]
        endapp = endapp.lower()
        if endapp == "y":
            calcpizzaingred()
        elif endapp == "n":
            print("Exiting program...")
            exit()
        else:
            print("Invalid selection")


if __name__ == "__main__":
    calcpizzaingred()
