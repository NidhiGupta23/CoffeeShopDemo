# Contains recipes of different types of coffee

def cappucinoReceipe():
    print("Step 1 : First, steam the milk. Heat 1 cup of milk in a 2-quart saucepan over medium heat. Let the milk simmer until bubbles form around the edges, but don’t boil the milk. Remove the pan from heat and set it on a flat surface.")
    print("Step 2 : Next, whip the milk with an electric mixer, increasing the speed as the milk begins to thicken. Continue mixing until you get the desired volume of froth.")
    print("Step 3 : Now, make the coffee. Measure 2 tablespoons of grounds for 5 to 6 ounces of water. Try using Folgers French Roast Coffee for a full-bodied taste, or make it with Folgers® Classic Decaf Coffee for less caffeine. You can brew the coffee in an automatic drip coffeemaker or a French press.")
    print("Step 4 : Now, make the cappuccino! A classic cappuccino calls for 1/3 espresso, 1/3 steamed milk, and 1/3 foam. You can mix it up by using 2 or 3 tablespoons of flavored syrups or even different kinds of milk, like chocolate or vanilla.")

def latteReceipe():
    print("Step 1 : Prepare the espresso")
    print("Step 2 : Pour milk to the pitcher. Make sure your stea wand cloth is moist. ")
    print("Step 3 : Purge the steam wand and pull it to far up and straight position. Place the pitcher so that the nozzle is aligned to the steam wand. Make sure the steam wand nozzle is in the middle of the pitcher and just below the milk surface. Tilt the pitcher a bit to optimize the whilrpool later on.")
    print("Step 4 : Swith on the steam wand. Start with the nozzle just below the surface but after a second or two rise the pitcher a bit so that the nozzle gets deeper into milk. Make sure the nozzle does not touch the bottom of the pitcher! ")
    print("Step 5 : Find a perfect position where the whilrpool of milk is created. Keep warming the milk until it reaches +55-62 c. ")
    print("Step 6 : Swirl the milk in the pitcher until it is smooth, silky and shiny.  ")
    print("Step 7 : Pour the caffe latte and enjoy! ")

def MochaReceipe():
    print("Step 1 : Collect below ingredients : \n  a. one cup hot brewed coffee  \n  b. one tablespoon unsweetened cocoa powder")
    print("  c. one tablespoon white sugar \n  d. two tablespoons milk ")
    print("Step 2 : Pour hot coffee into a mug. Stir in cocoa, sugar and milk.")

def expressoReceipe():
    print("Step 1 : CLEAN YOUR PORTAFILTER \n Step 2 : DOSE CORRECTLY \n Step 3 : DISTRIBUTE YOUR GROUNDS IN THE PORTAFILTER")
    print("Step 4 : TAMP EVENLY AND CONSISTENTLY \n Step 5 : RINSE YOUR GROUP HEAD \n Step 6 :  INSERT THE PORTAFILTER AND START BREWING IMMEDIATELY")
    print("Step 7 : INSERT THE PORTAFILTER AND START BREWING IMMEDIATELY \n  Step 8: SERVE WITH A SMILE")
    print("Step 9 : DISCARD THE PUCK, CLEAN THE BASKET AND RINSE THE GROUP HEAD")


def procedureToMakeCoffee(coffeeType):
    match coffeeType.upper() :
        case 'CAPPICINO' : cappucinoReceipe()
        case 'LATTE'     : latteReceipe()
        case 'MOCHA'     : MochaReceipe()
        case 'EXPRESSO'  : expressoReceipe()


