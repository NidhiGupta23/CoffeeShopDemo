# This file contains the welcome message for the customers
# user input is taken wrt coffee chosen

import time
import coffeeReceipe as cReceipe
import coffeeOrder as cOrder


# Function prints logo a cup of coffee
def printWelcome_message():
    x = 10 * ' '
    print(8 * ' ', 'Welcome to Coffee Shop')
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
    time.sleep(1)


# Function that takes user input in form of string that is type of coffee
def welcomeMenu():
    print("Please choose which coffee you like !!!")
    print(" 1. Cappuccino \n 2. Latte \n 3. Mocha \n 4. Espresso")
    coffeeType = input('Coffee needed : ')
    print('Coffee choosed : ', coffeeType.upper())
    return coffeeType.upper()


# Function lists types of coffee available in the shop
def coffeeAvailable(coffeeType):
    coffeeList = ['CAPPUCCINO', 'LATTE', 'MOCHA', 'ESPRESSO']
    if coffeeType.upper() in coffeeList:
        procedureOrOrder(coffeeType)
    else:
        print("Choose valid option from the menu")
        print("Want to order again, write yes or no")
        orderAgain = input("Yes or No")
        if orderAgain.upper() == 'YES':
            welcomeMenu()
        else:
            print("Thank you for your valuable time !!!")
            exit(0)


# Function checks whether an order is placed or process to make coffee
def procedureOrOrder(coffeeType):
    print('  Want to know procedure or place order \n Type \n 1. Process \n 2. Order ')
    inputRec = input('Type 1 or 2 : ')
    if inputRec == '1':
        print("\n \n \t Below is the procedure to make your own delicious coffee")
        cReceipe.procedureToMakeCoffee(coffeeType)
    elif inputRec == '2':
        placeCoffee = cOrder.coffeeOrder()
        placeCoffee.checkUserAccount()
        #placeCoffee.coffeePlacement(coffeeType)
    else:
        print("Try again")


# Main code
if __name__ == '__main__':
    printWelcome_message()
    coffeeType = welcomeMenu()
    coffeeAvailable(coffeeType)
