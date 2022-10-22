from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


mashine_running = True
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_mashine = MoneyMachine()


while mashine_running :
    
    user_choice = input("enter your choice latte/espresso/cappuccino :").upper()
    
    if user_choice == "L" :
        
        my_order = my_menu.find_drink("latte")
        
        if my_coffee_maker.is_resource_sufficient(my_order):
            my_coffee_maker.make_coffee(my_order)
        
    elif user_choice == "E":
        
        my_order = my_menu.find_drink("espresso")
        
        if my_coffee_maker.is_resource_sufficient(my_order):
            
            my_coffee_maker.make_coffee(my_order)
            
    elif user_choice == "C":
        
        my_order = my_menu.find_drink("cappuccino")
        
        if my_coffee_maker.is_resource_sufficient(my_order):
            my_coffee_maker.make_coffee(my_order)
        
    elif user_choice == "REPORT":
        
        print("Here are the reports : ")
        my_coffee_maker.report()

    elif user_choice == "OFF":
        
        print("The mashine is turning off!!")
        mashine_running = False
      
    elif user_choice == "MR":
        
        print("here is the total profit \n" + my_money_mashine.report())
      
    else :
        
        print("Please make use of your brain and feed some valid input!!")

print("Program Ends!")