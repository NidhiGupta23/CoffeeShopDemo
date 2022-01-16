# File focus on customer database by using sqlite3
# A table is created which add, read, update
# and delete rows

import sqlite3


class dataBaseStructure:
    def __init__(self):
        self.connection = sqlite3.connect("Customer5.db")
        self.cursor = self.connection.cursor()

    # Creating databse that is a table with name 'CUSTOMER'
    def tableCreation(self):
        try:
            tablexistscmd = "SELECT COUNT(NAME) FROM SQLITE_MASTER WHERE TYPE='table' AND NAME='CUSTOMER'"
            self.cursor.execute(tablexistscmd)
            if self.cursor.fetchone()[0] != 1:
                table = """CREATE TABLE CUSTOMER (
                       FNAME CHAR(25) NOT NULL,
                       LNAME CHAR(25),
                       PWORD VARCHAR(9) NOT NULL,
                       EMAIL VARCHAR(255) NOT NULL,
                       CREDIT FLOAT                   
                )"""
                self.cursor.execute(table)
                self.connection.commit()
            return True
        except (RuntimeError, TypeError, NameError, BaseException) as e:
            print(e)
            return False

    # Insert customer details in the customer table
    def tableInsertion(self, fname, lname, pWord, eMail, credit):
        try:
            insertcmd = "INSERT INTO CUSTOMER (FNAME, LNAME, PWORD, EMAIL, CREDIT) VALUES "
            valuecmd = "(\"%s\", \"%s\", \"%s\", \"%s\", \"%f\")" % (fname, lname, pWord, eMail, credit)
            self.cursor.execute(insertcmd+valuecmd)
            self.connection.commit()
            print("Values are being added successfully")
            return 1
        except sqlite3.Error as e:
            print("Error faced : ", e)
            return 0

    # To update customer details using customer email id along with
    # column and updated value that needs to be included
    def tableUpdation(self, userEmail, newValue, column):
        try:
            target = column + "= (?)"
            updatecmd = f"UPDATE CUSTOMER SET {target} WHERE EMAIL=(?)"
            self.cursor.execute(updatecmd, (newValue, userEmail))
            self.connection.commit()
            return "Successful"
        except sqlite3.Error as e:
            print("Error faced : ", e)
            return 0

    # Read database and print them line wise
    def tableRead(self):
        self.cursor.execute("SELECT * FROM CUSTOMER")
        [print(row) for row in self.cursor.fetchall()]

    # Delete customer details or entire database can be removed
    # ToDo: Give right permission to the Admin
    def tableDelete(self, table, row):
        if table == 'yes':
            self.cursor.execute("DROP TABLE CUSTOMER")
        else:
            deletecmd = "DELETE FROM CUSTOMER WHERE " + row
            self.cursor.execute(deletecmd)
            self.connection.commit()

    # check from database if user exists or not by taking user email and password
    # PWORD: user password
    # EMAIL: user email address
    # return value 1 for validate user and 0 for not validate user
    def checkUserExistence(self, userEmail, userPass):
        try:
            existencecmd = "SELECT * FROM CUSTOMER WHERE EMAIL=(?) and PWORD=(?)"
            self.cursor.execute(existencecmd, (userEmail, userPass))
            self.connection.commit()
            cuDetail = self.cursor.fetchone()
            if cuDetail is not None:
                return cuDetail
            else:
                return 0
        except sqlite3.Error as e:
            print(e)
            return 0
