# Constants.py
# Janna Thomas
# This contains formatting constants
# Requires files: Janna_Thomas_Blackjack_Main.py, CardGame.py, DatabaseConnection.py, and PlayHand.py to run
# This file has no main function and cannot be run on its own

MESSAGE_W = 21
PTS_W = 6
CARD_W = 9
GAP_W = 6
PRINT_W = 54

PUSH_W = PRINT_W * 2 + CARD_W + GAP_W
PTS_PLAYER_NL = MESSAGE_W + PTS_W
PTS_PLAYER_NNL = MESSAGE_W + PTS_W + 54
HEADING_PLAYER_NL = PRINT_W + MESSAGE_W + PTS_W + GAP_W

HINT_HOUSE_BASE = PRINT_W + PTS_W
PTS_HOUSE_NL = 96
HEADING_HOUSE_NL = 156
HEADING_HOUSE_NNL = PRINT_W + PTS_W + CARD_W
