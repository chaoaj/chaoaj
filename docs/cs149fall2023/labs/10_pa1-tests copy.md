#Lab12 - PA1 Unit Tests

Here is a starting point for Part A of the project. Two example assert statements are provided for each test function. You should add at least three more to each function, so that every requirement of the project is tested.

Note: Docstrings are generally not required for test functions. But you should still have a module docstring with your name and date.

test_dice.py

<pre>
"""Test the dice module.

Name: YOUR NAME
Date: THE DATE
"""

from dice import roll_dice
from dice import are_valid
from dice import add_values
from dice import num_faces


def test_roll_dice():
    assert roll_dice(5) == ['Q', 'Q', '9', 'J', 'K']
    assert roll_dice(0, 1) == ['9']


def test_are_valid():
    assert are_valid(['A', 'K'])
    assert not are_valid(['1', '2', '3'])


def test_add_values():
    assert add_values(['10', '10', '10', '10']) == 40
    assert add_values([]) == -1


def test_num_faces():
    assert num_faces(['Q', '9', 'Q', '9'], 'Q') == 2
    assert num_faces(None) == -1

</pre>
On Part B, you will need to define a test function for each of the nine categories. Each test function should have at least five assert statements. (The autograder has over ten assert statements in each category!) Don't just add assert statements for the sake of having five or more. Make sure you test each situation required by the project.

Note: The following code abbreviates score_dice as sd, rather than import every constant.

test_score_dice.py
<pre>
"""Test the score_dice module.

Name: YOUR NAME
Date: THE DATE
"""

import score_dice as sd


def test_one_pair():
    assert sd.calculate_score(['9', '9', '10', 'J', 'K'], sd.PAIR) == 18
    assert sd.calculate_score(['9', '10', 'J', 'Q', 'K'], sd.PAIR) == 0
</pre>