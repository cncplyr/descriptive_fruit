from random import choice

from descriptive_fruit.adjective import ADJECTIVES
from descriptive_fruit.fruit import FRUITS


def generate(separator=' '):
    return choice(ADJECTIVES) + separator + choice(FRUITS).replace(' ', separator)
