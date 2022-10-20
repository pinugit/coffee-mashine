def coinWnder(quarters, dimes, nickles, pennies, cost):
    #This function will handle all the coin transition
    totalQuarters = quarters * 0.25
    totalDimes = dimes * 0.10
    totalNickles = nickles * 0.05
    totalPennies = pennies * 0.01
    netTotal = totalDimes + totalNickles + totalQuarters +totalPennies
    change = 0
    canGetCoffee = True
    if netTotal < cost:
        canGetCoffee = False
        return canGetCoffee, change
    else :
        change = netTotal - cost
        return canGetCoffee, change
    

menu = {
    "espresso" :{
        "ingredients" :{
            "water" : 50,
            "coffee" :18,
        },
        "cost" : 1.5,
    },
    
    "latee" : {
        "ingredients" :{
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost" : 2.5,
    },
    
    "cappuccino" : {
        "ingredients" :{
            "water" : 250,
            "milk" : 100,
            "coffee" :24,
        },
        "cost" : 3.0,
    }
}

resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100
}


espresso = menu["espresso"]
espressoWater = espresso["ingredients"]["water"]
espressoCoffee = espresso["ingredients"]["coffee"]
espressoCost = espresso["cost"]
espressomilk = 0
    
latee = menu["latee"]
lateeWater = latee["ingredients"]["water"]
lateeCoffee = latee["ingredients"]["coffee"]
lateeCost = latee["cost"]
lateemilk = latee["ingredients"]["milk"]

cappuccino = menu["cappuccino"]
cappuccinoWater = cappuccino["ingredients"]["water"]
cappuccinoCoffee = cappuccino["ingredients"]["coffee"]
cappuccinoCost = cappuccino["cost"]
cappuccinomilk = cappuccino["ingredients"]["milk"]

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

mashineRunning = True

while mashineRunning :
    
    userChoice = str(input("What would you like? (espresso(E)($1.5)/latee(L)($2.5)/cappuccino(C)($3.0)): ")).upper()
    
    
    if userChoice == "ESPRESSO" or userChoice == "E":
        userQuarters = int(input("Enter the number of quarters : "))
        userDimes = int(input("Enter the number of dimes : "))
        userNickles = int(input("Enter the number of nickles : "))
        userPennies = int(input("Enter the number of pennies : "))
        
        canGetCoffee, change = coinWnder(userQuarters, userDimes, userNickles, userPennies, espressoCost)
        
        if canGetCoffee:
            
            print("Here is your change $" + str(change) )
            if espressoWater > water :
                print("Not enough Water, please contact a staff member so they can fill this upp.")
            
            elif espressomilk > milk:
                print("Not enough Milk, please contact a staff member so they can fill this upp.")
        
            elif espressoCoffee > coffee:
                print("Not enough Coffee, please contact a staff member so they can fill this upp.")
    
            else:
                water -= espressoWater
                milk -= espressomilk
                coffee -= espressoCoffee
                print("Enjoy your espresso")
                
        else :
            print("Please insert inough coins")
            
    elif userChoice == "LATEE" or userChoice == "L":
        
        userQuarters = int(input("Enter the number of quarters : "))
        userDimes = int(input("Enter the number of dimes : "))
        userNickles = int(input("Enter the number of nickles : "))
        userPennies = int(input("Enter the number of pennies : "))
        
        canGetCoffee, change = coinWnder(userQuarters, userDimes, userNickles, userPennies, lateeCost)
        
        if canGetCoffee:
            
            print("Here is your change $" + str(change) )
        
            if lateeWater > water :
                print("Not enough Water, please contact a staff member so they can fill this upp.")

            elif lateemilk > milk:
                print("Not enough Milk, please contact a staff member so they can fill this upp.")

            elif lateeCoffee > coffee:
                print("Not enough Coffee, please contact a staff member so they can fill this upp.")

            else:
                water -= lateeWater
                milk -= lateemilk
                coffee -= lateeCoffee
                print("Enjoy your Latee")
        
        else :
            print("Please insert inough coins")
            
    elif userChoice == "CAPPUCCINO" or userChoice == "C":
        
        userQuarters = int(input("Enter the number of quarters : "))
        userDimes = int(input("Enter the number of dimes : "))
        userNickles = int(input("Enter the number of nickles : "))
        userPennies = int(input("Enter the number of pennies : "))
        
        canGetCoffee, change = coinWnder(userQuarters, userDimes, userNickles, userPennies, cappuccinoCost)
        
        if canGetCoffee:
            
            print("Here is your change $" + str(change) )
        
            if cappuccinoWater > water :
                print("Not enough Water, please contact a staff member so they can fill this upp.")

            elif cappuccinomilk > milk:
                print("Not enough Milk, please contact a staff member so they can fill this upp.")

            elif cappuccinoCoffee > coffee:
                print("Not enough Coffee, please contact a staff member so they can fill this upp.")

            else:
                water -= cappuccinoWater
                milk -= cappuccinomilk
                coffee -= cappuccinoCoffee
                print("Enjoy your Cappuccino")
        else :
            print("Please insert inough coins")
            
    elif userChoice == "REPORT":
        
        print("Remaning resources are:")
        print("Water = " + str(water))
        print("Milk = " + str(milk))
        print("Coffee = " + str(coffee))
        
    elif userChoice == "OFF":
        
        print("mashine is turning off!")
        mashineRunning = False
        
    elif userChoice == "FILL":
        
        water = 500
        milk = 400
        coffee =200
        print("Wait for mashine to fill up.")
        print("DONE!")
         
    else:
        
        print("please enter a valid input.")
        
print("print program ended!")