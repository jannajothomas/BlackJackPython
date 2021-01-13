# PlayHand.py
# Janna Thomas
# This manages the game play functions and rules for the blackjack game.
# Requires files: Janna_Thomas_Blackjack_Main.py, CardGame.py, DatabaseConnection.py, and Constants.py to run
# This file has no main function and cannot be run on its own

from CardGame import Player
from CardGame import Deck
import Constants

# point dictionary for cards
ptsDict = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


def getAnswerToQuestion(string, error_string):
    answer = input(string)
    while answer == '':
        answer = input(error_string)
    return answer


# loop getting an input until a valid input is selected
def get_valid_input(user_prompt, valid_list):
    while True:
        user_selection = input(user_prompt)
        if user_selection not in valid_list:
            print("That is not a valid input.  Please try again.")
            continue
        else:
            return user_selection


def print_headers():
    fstring = "{0:.^{1}}".format("Your Hand", Constants.PRINT_W)
    print("{0:>{1}}".format(fstring, Constants.HEADING_PLAYER_NL), end='')

    fstring = "{0:.^{1}}".format("The House", Constants.PRINT_W)
    print("{0:>{1}}".format(fstring, Constants.HEADING_HOUSE_NNL))


# Prompts user for amount to bet.  If input is not a positive number, the bet is set at 5
def setBet(user_balance):
    if user_balance < 5:
        print("You don't have enough credit to place a bet.  You need to add money to your balance.")
        return
    requested_bet = input("Enter your bet.  Default is 5: ")
    try:
        requested_bet = float(requested_bet)
    except ValueError:
        requested_bet = 5
    if requested_bet < 0:
        requested_bet = 5
    elif requested_bet > user_balance:
        print("That bet is higher than your balance.  Your bet will be {}".format(user_balance))
        requested_bet = user_balance
    return requested_bet


# prints points in hand or any notable outcomes
def summarizeHand(offset, points):
    print()
    if points > 21:
        fstring = "{0:X^{1}}".format(" BUST ", Constants.PRINT_W)
    elif points == 21:
        fstring = "{0:!^{1}}".format(" BLACKJACK ", Constants.PRINT_W)
    else:
        fstring = "{0:.^{1}}".format(" PTS = " + str(points), Constants.PRINT_W)
    print("{0:>{1}}".format(fstring, offset), end='')


# prints rows during player turn
def printPlayerHand(player, house):
    print("{:>{}}".format("Pts =", Constants.PTS_PLAYER_NL), "{:>2}".format(player.points), end='')
    player.showHand()

    value, suit = house.dealerHint()
    hint_string = ("{:>4} of {}".format(value, suit))
    local_offset = Constants.HINT_HOUSE_BASE - Constants.CARD_W * (len(player.hand) - 2)
    print("{0:>{1}}".format(hint_string, local_offset), end='')

# prints rows during house turn
def printHouseHand(house):
    print("{:>{}}".format("Pts =", Constants.PTS_HOUSE_NL), "{:>2}".format(house.points), end='')
    house.showHand()


def play_hand(local_username, local_balance, local_wins, local_loses):
    # setup bet for hand
    bet = setBet(local_balance)
    # if player doesn't have enough money they are sent back to the main menu
    if bet is None: return

    print("\nYour balance is {}.  Your bet is {}".format(local_balance, bet))

    # prepare the deck, create the players and deal the cards
    deck = Deck()
    deck.create_shuffled_deck()
    player = Player()
    house = Player()
    player.draw(deck, 2)
    house.draw(deck, 2)

    print_headers()

    # players Turn
    # deal with special issue of a blackjack
    if player.points == 21:
        printPlayerHand(player, house)
    while player.points < 21:
        printPlayerHand(player, house)
        # prompt for next action
        print("", end='\r')
        local_next_action = get_valid_input("Hit[h] or Stand[s]?", ["h", "H", "s", "S"])

        if local_next_action in ["s", "S"]: break
        else: player.draw(deck, 1)

        if player.points >= 21: printPlayerHand(player, house)

    summarizeHand(Constants.HEADING_PLAYER_NL, player.points)
    print()

    # let house know if player has busted
    player_points = player.points if player.points <= 21 else 0
    printHouseHand(house)
    while house.points <= 16 and player_points > house.points:
        house.draw(deck, 1)
        print()
        printHouseHand(house)
    summarizeHand(Constants.HEADING_HOUSE_NL, house.points)

    # announce results
    print()
    if (player.points == 21) & (len(player.hand) == 2):
        fstring = "{0:!^{1}}".format(" Natural! ", Constants.PRINT_W)
        local_balance += bet * 1.5
        local_wins += 1
        print("{0:>{1}}".format(fstring, Constants.HEADING_PLAYER_NL))
    elif house.points > 21 or (player.points > house.points and player.points <= 21):
        fstring = "{0:*^{1}}".format(" Player Wins ", Constants.PRINT_W)
        local_balance += bet
        local_wins += 1
        print("{0:>{1}}".format(fstring, Constants.HEADING_PLAYER_NL))
    elif player.points == house.points:
        fstring = "{0:-^{1}}".format(" Push ", Constants.PUSH_W)
        print("{0:>{1}}".format(fstring, Constants.HEADING_HOUSE_NL))
    else:
        fstring = "{0:*^{1}}".format(" House Wins ", Constants.PRINT_W)
        local_balance -= bet
        local_loses += 1
        print("{0:>{1}}".format(fstring, Constants.HEADING_HOUSE_NL))

    return local_username, local_balance, local_wins, local_loses
