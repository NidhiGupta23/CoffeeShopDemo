# File focuses on creating, logging user account
# once account is created it works on placing
# coffee order and deduct amount from credit and
# display remaining credit

import customersData as cuData

class coffeeOrder:
    def __init__(self):
        self.customer1 = cuData.customersData()

    # Create user account by adding details into customer table
    def createAccount(self):
        print("\n \nPLEASE CREATE AN ACCOUNT")
        fname, lname, pWord, eMail, credit = self.customer1.getUserDetails()
        if len(pWord) != 8:
            print("Enter password that is 8 digit long... TRY AGAIN")
            pWord = input("Enter 8 digit Password and press enter : ")
        valueAdded = self.customer1.addCustomer(fname, lname, pWord, eMail, credit)
        if valueAdded == 1:
            print("Account created successfully")
            print("********************************************************************************")
            print("********************************************************************************")
            print("Kindly login with your registered email and password")
            self.login()
        else:
            print("Could not create Account..Try again ")

    # TODO: Check the password length is 8 digit long
    def checkPwd(self, pWord, eMail):
        pass

    # Authentic the email and password of user
    # userEmail- Takes user email address
    # userPassword- Takes user password
    def login(self):
        userEmail = input("Enter your email : ")
        userPassword = input("Enter your 8 word password : ")
        userAuthenticate = self.customer1.validate(userEmail, userPassword)
        if userAuthenticate is not None:
            print("********************************************************************************")
            print("********************************************************************************")
            print("Welcome to our caffe again ", userAuthenticate)
            print("********************************************************************************")
            print("********************************************************************************")
        else:
            print("Please enter your email Id and password correctly")

    # check if user account exists or user needs to create a new account
    # accountPresent- checks whether user account exists or not
    def checkUserAccount(self):
        accountPresent = input("Press 1 if account exists else press any key ")
        if accountPresent == '1':
            self.login()
        else:
            self.createAccount()

    # Place coffee order and update the remaining amount
    def coffeePlacement(self, coffeeType, coffeePrice):
        remainCredit = self.customer1.placeOrder(coffeePrice)
        if remainCredit == 1:
            print("ORDER ACCEPTED. COLLECT ",coffeeType, " COFFEE FROM COUNTER 4")
        elif remainCredit == 0:
            print("Server cannot connect to your database... Retry after few minutes")
        else:
            print("Not enough credit. Add money to your wallet")


    def printRemainingCredit(self, remainCredit):
        print("remaining credit in your account: ", remainCredit)
        self.customer1.upgradeData(0, remainCredit, "credit")


    def __del__(self):
        del self.customer1
