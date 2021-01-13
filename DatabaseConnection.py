# DatabaseConnection.py
# Janna Thomas
# This manages a database connection for a blackjack game and contains class DatabaseConnection
# Requires files: Janna_Thomas_Blackjack_Main.py, PlayHand.py, CardGame.py, and Constants.py to run
# This file has no main function and cannot be run on its own

import sqlite3
from PlayHand import getAnswerToQuestion


class DatabaseConnection:
    def __init__(self, data_base_name):
        self.data_base_name = data_base_name
        self.conn = sqlite3.connect(data_base_name)
        self.c = self.conn.cursor()

    def setupTable(self):
        # create table if it doesn't exist
        self.c.execute('''create table if not exists userdata(name,username,balance,wins,loses)''')
        self.conn.commit()

    def getUserData(self, username):
        self.c.execute('SELECT * FROM userdata WHERE username=?', (username,))
        record = self.c.fetchone()
        if record is None:
            record = self.createNewUser(username)
        return record

    def createNewUser(self, username):
        string = "Please enter your first name: "
        error_string = "You have to enter a first name to continue. Please try again."
        firstname = getAnswerToQuestion(string, error_string)

        string = "Please enter your requested balance: "
        error_string = "You have to enter a balance to continue"
        requested_balance = getAnswerToQuestion(string, error_string)

        self.c.execute("INSERT INTO userdata VALUES(?,?,?,?,?)", (firstname, username, int(requested_balance), 0, 0))
        self.conn.commit()
        self.c.execute('SELECT * FROM userdata WHERE username=?', (username,))
        return self.c.fetchone()

    def updatePlayerStats(self, username, balance, wins, loses):
        self.c.execute('UPDATE userdata set balance =? where username =?', (balance, username))
        self.c.execute('UPDATE userdata set wins =? where username =?', (wins, username))
        self.c.execute('UPDATE userdata set loses =? where username =?', (loses, username))
