# File work on CRUD operation where customer
# data can be added, read, modified and delete.
# File is connected to customer database via
# databaseStructure.py file

import sqlite3
import databaseStructure as dbS


class customersData:
    def __init__(self):
        self.dbFlag = 0
        self.data1 = dbS.dataBaseStructure()

    # Check if customer database exists or not
    def checkDataBase(self):
        if self.data1.tableCreation():
            self.dbFlag = 1
            #self.data1.tableRead()

    # Get user information and return the details to method createAccount
    def getUserDetails(self):
        fname = input("Enter First Name and press enter : ")
        lname = input("Enter Last Name and press enter : ")
        pWord = input("Enter 8 digit Password and press enter : ")
        eMail = input("Enter EMail and press enter : ")
        credit = int(input("Enter Credit and press enter : "))
        return fname, lname, pWord, eMail, credit

    # Add customer into database for successful creation of user account
    def addCustomer(self, fname, lname, pWord, eMail, credit):
        dataAdded = 0
        self.checkDataBase()
        print("Value of dbFlag : ", self.dbFlag)
        try:
            if self.dbFlag == 1:
                print("Adding data :  ", fname, lname, pWord, eMail, credit)
                dataAdded = self.data1.tableInsertion(fname, lname, pWord, eMail, credit)
            else:
                print("somehow \'if\' condition doesn't work")
        except sqlite3.Error as e:
            print(e)
        finally:
            return dataAdded

    # Validates whether user is authentic via user email id and user password
    # uemail: user email address
    # upass: user password
    # uAuth : return value 1 for validate user and 0 for not validate user
    def validate(self, uemail, upass):
        uAuth = self.data1.checkUserExistence(uemail, upass)
        return uAuth

    def placeOrder(self, totalAmount):
        # data = pd.read_sql_query("SELECT * FROM CUSTOMER")
        # print(data)
        pass

    def upgradeData(self):
        pass

    def deleteCustomerData(self):
        pass

    def __del__(self):
        del self.data1

