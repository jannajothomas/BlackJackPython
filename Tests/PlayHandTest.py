#!/usr/bin/python

# PlayHandTest.py

# Janna Thomas
# This program modules in the PlayHand file
# Type: python PlayHandTest.py

import unittest
import PlayHand


class PlayHandTest(unittest.TestCase):

    def test_get_Answer_To_Question(self):
        input_value = 'test1'
        prompt = 'Prompt'
        error_string = 'error'
        expected_output = ['Prompt']
        output = []

        def mock_input(s):
            output.append(s)
            return input_value

        PlayHand.input = mock_input
        PlayHand.print = lambda s: output.append(s)
        output_return = (PlayHand.getAnswerToQuestion(prompt, error_string))
        self.assertEqual(output, expected_output)
        self.assertEqual(output_return, input_value)

    def test_get_Answer_To_Question_No_Input(self):
        valid_input = 'valid input'
        input_values = ['', valid_input]
        prompt = 'Prompt'
        error_string = 'error'
        expected_output = [prompt, error_string]
        output = []

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        PlayHand.input = mock_input
        PlayHand.print = lambda s: output.append(s)
        output_return = (PlayHand.getAnswerToQuestion(prompt, error_string))
        self.assertEqual(output, expected_output)
        self.assertEqual(output_return, valid_input)

    def test_get_valid_input(self):
        input_values = ['s', '', 'b']
        expected_output = ["Input", "That is not a valid input.  Please try again.",
                           "Input", "That is not a valid input.  Please try again.",
                           "Input"]
        output = []
        my_list = ['b', "B", 'x', 'X']

        def mock_input(s):
            output.append(s)
            return input_values.pop(0)

        PlayHand.input = mock_input
        PlayHand.print = lambda s: output.append(s)
        PlayHand.get_valid_input('Input', my_list)
        self.assertEqual(output, expected_output)

    def test_Set_Bet(self):
        # initial balance is 8
        input_values = [8, 4, 2.3, 'a', -5, "seven"]
        expected_output = [8.0, 4.0, 2.3, 5, 5.0, 5.0]
        output_string = []
        output_returns = []

        def mock_input(s):
            output_string.append(s)
            return input_values.pop(0)

        PlayHand.input = mock_input
        PlayHand.print = lambda s: output_string.append(s)
        while len(input_values) > 0:
            output_returns.append(PlayHand.setBet(8))
        self.assertEqual(output_returns, expected_output)

    def test_Set_Bet_Larger_Than_Balance(self):
        # initial balance is 6
        input_values = [8, 6, 'a']
        expected_output = [6.0, 6.0, 5.0]
        output_string = []
        output_returns = []

        def mock_input(s):
            output_string.append(s)
            return input_values.pop(0)

        PlayHand.input = mock_input
        PlayHand.print = lambda s: output_string.append(s)
        while len(input_values) > 0:
            output_returns.append(PlayHand.setBet(6))
        self.assertEqual(output_returns, expected_output)


if __name__ == '__main__':
    unittest.main()
