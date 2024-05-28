#Lab12 - PA1 Unit Tests

Videos for explanation of Cant Stop:

1) [https://www.youtube.com/watch?v=sI3HLZ36VPM](https://www.youtube.com/watch?v=sI3HLZ36VPM)

2) Our version: [https://youtu.be/g1DFGT_1tJQ](https://youtu.be/g1DFGT_1tJQ)

Here is a starting point for Part A of the project. Two example assert statements are provided for each test function. You should add at least three more to each function, so that every requirement of the project is tested.

Note: Docstrings are generally not required for test functions. But you should still have a module docstring with your name and date.

test_dice.py

<pre>
"""Test_dice.py - test the dice module.

@author: Alvin Chao
@version: 3-21-24
I got help from TA Madison on the valid tests.
"""
import unittest
import dice


class TestDice(unittest.TestCase):


    def test_roll_dice_valid(self):
        expected = [4]
        actual = dice.roll_dice(1,0)
        self.assertEqual(expected, actual, "1-0")


    def test_roll_dice_invalid(self):
        pass

    def test_are_valid_valid(self):
        pass

    def test_are_valid_invalid(self):
        pass


if __name__ == '__main__':
   unittest.main()
</pre>

Also here are some stubs for the dice module:
<pre>
""" PA1- dice.py.

@author: Alvin Chao
@version: 3-21-24
I got help from TA Marshall on the invalid tests.
"""

def roll_dice(num, seed):
    my_dice = []
    my_dice.append[6]
    return my_dice

def are_valid(dice):
    return True
</pre>
