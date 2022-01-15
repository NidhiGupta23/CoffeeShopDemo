# File focus on customer database by using sqlite3
# A table is created which add, read, update
# and delete rows

import sqlite3


class dataBaseStructure:
    def __init__(self):
        self.connection = sqlite3.connect("Customer5.db")
        self.cursor = self.connection.cursor()

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

    def tableUpdation(self, oldvalue, newvalue):
        updatecmd = "UPDATE CUSTOMER SET " + newvalue + " WHERE " + oldvalue
        self.cursor.execute(updatecmd)
        self.connection.commit()

    def tableRead(self):
        self.cursor.execute("SELECT * FROM CUSTOMER")
        [print(row) for row in self.cursor.fetchall()]

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
            existencecmd = "SELECT FNAME FROM CUSTOMER WHERE EMAIL=(?) and PWORD=(?)"
            self.cursor.execute(existencecmd, (userEmail, userPass))
            self.connection.commit()
            firstname = self.cursor.fetchone()
            if firstname is not None:
                return firstname
            else:
                return 0
        except sqlite3.Error as e:
            print(e)
            return 0
