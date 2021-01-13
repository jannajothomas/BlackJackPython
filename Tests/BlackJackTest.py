#!/usr/bin/python

# BlackJackTest.py

# Janna Thomas
# This program tests my blackjack project
# Type: python BlackJackTest.py


import unittest
import Janna_Thomas_Blackjack_Main


class BlackJackTest(unittest.TestCase):

    def test_Add_Money_To_Balance(self):
        input_values = [20, 0, 'a', 100, 'hello', -5]
        expected_output = [35.0, 15.0, 15.0, 115.0, 15.0, 15.0]
        output_string = []
        output_returns = []

        def mock_input(s):
            output_string.append(s)
            return input_values.pop(0)

        Janna_Thomas_Blackjack_Main.input = mock_input
        Janna_Thomas_Blackjack_Main.print = lambda s: output_string.append(s)
        while len(input_values) > 0:
            output_returns.append(Janna_Thomas_Blackjack_Main.addMoneyToBalance(15))
        print("test 1 output", output_returns)
        self.assertEqual(output_returns, expected_output)


if __name__ == '__main__':
    unittest.main()
