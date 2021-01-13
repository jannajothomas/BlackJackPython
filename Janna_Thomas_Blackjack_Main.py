#!/user/bin/python

# Janna_Thomas_Blackjack_Main.py
# Janna Thomas
# This program executes a command line blackjack game
# Requires files: PlayHand.py, CardGame.py, DatabaseConnection.py and Constants.py to run
# Type python Janna_Thomas_Blackjack_Main.py

import sys
from PlayHand import play_hand
from PlayHand import getAnswerToQuestion
from PlayHand import get_valid_input
from DatabaseConnection import DatabaseConnection

# This module's primary focus is managing the long term storage
# of the players data


def prepare_game_for_new_user():
    dbc.setupTable()
    requested_username = greet_and_get_username()
    return dbc.getUserData(requested_username)


def greet_and_get_username():
    print("Hello, welcome to Janna's blackjack game")
    get_name_string = "Enter your username to get started.  If you have never played enter a new username: "
    get_name_no_entry = ("You have to enter a user name to get started. "
                         " If you have not played before, enter the name you would like\n")
    return getAnswerToQuestion(get_name_string, get_name_no_entry)


def get_next_action():
    prompt = "Would you like to play[p], add money to your balance[b], or quit[q]"
    valid_inputs = ["p", "P", "b", "B", "q", "Q"]
    return get_valid_input(prompt, valid_inputs)


# Prompts user for amount to increase balance.  If input is not a positive number, nothing is added
def addMoneyToBalance(current_balance):
    balance_addition = input("How much would you like to add (max is 100).  "
                             "No entry or invalid entry will result in no balance added: ")
    try:
        balance_addition = float(balance_addition)
    except ValueError:
        balance_addition = 0
    if balance_addition < 0:    balance_addition = 0
    if balance_addition > 100:   balance_addition = 100
    print("Your new balance is {}".format(current_balance + balance_addition))
    return current_balance + balance_addition


def clean_and_quit():
    dbc.conn.close()
    print("Thanks for playing,", username, "your balance is ", balance,
          ".  Your record is", wins, "wins and", loses, "loses")
    print("Goodbye")
    sys.exit(0)


def save_info():
    dbc.updatePlayerStats(username, balance, wins, loses)
    dbc.conn.commit()


if __name__ == '__main__':
    # establish a database connection
    dbc = DatabaseConnection('blackJackUserData.db')

    # if database record exists, retrieve it.  Otherwise create a new record for the player
    name, username, balance, wins, loses = prepare_game_for_new_user()
    user_info = (name, username, balance, wins, loses)
    print("\nWelcome, {}.  Your username is {}.  Your balance is {}.  ".format(name, username, balance), end='')

    # continue game until player exits with the quit option
    while True:
        next_action = get_next_action()
        while next_action not in ["p", "P"]:
            if next_action in ["q", "Q"]:
                clean_and_quit()
            if next_action in ["b", "B"]:
                balance = addMoneyToBalance(balance)
                save_info()
            next_action = get_next_action()

        # game either returns results, or player is sent back to the menu to add balance
        try: username, balance, wins, loses = play_hand(username, balance, wins, loses)
        # this forces player to add more credits to play
        except TypeError: continue


        # update database
        save_info()
        print("Your balance is", balance, " ")
