import random
class Die:

    """Represent a 6-sided die."""

    def __init__(self):
        """Initialize die with random face value."""
        self.roll()

    def get_value(self):
        """Return the die's face value."""
        return self.__value

    def roll(self):
        """Roll the die and return its new face value."""
        self.__value = random.randint(1, 6)
        return self.__value

    def __str__(self):
        """Return a string representation of the die."""
        return str(self.__value)
