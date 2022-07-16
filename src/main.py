# This file contains the welcome message for the customers
# user input is taken wrt coffee chosen

# %%

import time
import pandas as pd
from IPython import display
import coffeeReceipe as cReceipe
import coffeeOrder as cOrder

coffeeMenu = ['CAPPUCCINO', 'LATTE', 'MOCHA', 'ESPRESSO']
coffeePrice = [45, 50, 55, 25]

# Function prints logo a cup of coffee
def printWelcome_message():
    x = 10 * ' '
    print("********************************************************************************")
    print("******************************************************************************** \n")
    print(8 * ' ', 'Welcome to Coffee Shop \n')
    print("********************************************************************************")
    print("******************************************************************************** \n")
    print(x, '     //     //    ')
    print(x, '    //     //     ')
    print(x, '     //     //')
    print(x, ' ******************')
    print(x, '*                  *')
    print(x, ' ****************** ')
    print(x, '|                  |')
    print(x, '|                  |')
    print(x, '|                  |||||||')
    print(x, '|                  |    ||')
    print(x, '|                  |    ||')
    print(x, '|                  |||||||')
    print(x, '||||||||||||||||||||')
    print("--------------------------------------------------------------------------------")
    time.sleep(2)


# Function that takes user input in form of string that is type of coffee
def welcomeMenu(df):
    print("*******   GOOD IDEAS START WITH BRAINSTORMING. GREAT IDEAS START WITH COFFEE   *******")
    print("--------------------------------------------------------------------------------\n")
    print("Please choose which coffee you like !!! \n")
    df.index +=1
    display.display(df, display_id=True)
    print("\n--------------------------------------------------------------------------------")
    coffeeType = input('Type coffee name needed : ')
    print("\n--------------------------------------------------------------------------------")
    return coffeeType.upper()

# Function lists types of coffee available in the shop
def coffeeAvailable(coffeeType, df):
    if coffeeType.upper() in coffeeMenu:
        procedureOrOrder(coffeeType, df)
    else:
        print("Choose valid option from the menu")
        print("Want to order again, write yes or no")
        orderAgain = input("Yes or No")
        if orderAgain.upper() == 'YES':
            welcomeMenu(df)
        else:
            print("Thank you for your valuable time !!!")
            exit(0)


# Function checks whether an order is placed or process to make coffee
def procedureOrOrder(coffeeType, df):
    print('Want to know procedure or place order \n Type \n 1. Process \n 2. Order ')
    inputRec = input('Type 1 or 2 : ')
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    if inputRec == '1':
        print("\n \nBelow is the procedure to make your own delicious coffee")
        print("--------------------------------------------------------------------------------")
        cReceipe.procedureToMakeCoffee(coffeeType)
    elif inputRec == '2':
        placeCoffee = cOrder.coffeeOrder()
        display.clear_output()
        placeCoffee.checkUserAccount()
        cfePrice = df['Prices'][df['CoffeeList'] == coffeeType].values[0]
        placeCoffee.coffeePlacement(coffeeType, cfePrice)
    else:
        print("Try again")
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")

# Main code
if __name__ == '__main__':
    df = pd.DataFrame({'CoffeeList': coffeeMenu, 'Prices': coffeePrice})
    printWelcome_message()
    coffeeType = welcomeMenu(df)
    coffeeAvailable(coffeeType, df)

# %%
