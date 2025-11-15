# This work is governed under the CC0 licence https://creativecommons.org/publicdomain/zero/1.0/

from collections.abc import Callable
from decimal import Decimal

class NextFunctions:
    @staticmethod
    def linear(increment: Decimal) -> Callable[[Decimal], Decimal]:
        """Creates a lambda incrementing input values by a given increment"""
        return lambda x: x + increment

    @staticmethod
    def geometric(multiplier: Decimal) -> Callable[[Decimal], Decimal]:
        """Creates a lambda multiplying input values by a given multiplier"""
        return lambda x: x * multiplier

class Sequence:
    def __init__(self: Sequence,
                 current_term: Decimal | float,
                 next_term_function: Callable[[Decimal], Decimal] = NextFunctions.linear(Decimal(1))
                 ) -> None:
        """Initialises a sequence object

        :param current_term: Decimal determines current term in the sequence
        :param next_term_function: Callable function to determine next term in sequence"""
        self._currentTerm: Decimal = Decimal(current_term)
        self._nextTermFunc: Callable[[Decimal], Decimal] = next_term_function

    def get_current_term(self: Sequence) -> Decimal:
        """Gets the current term of the object"""
        return self._currentTerm

    def next_term(self: Sequence) -> Sequence:
        """Creates a sequence object for the next term"""
        return Sequence(current_term = self._nextTermFunc(self._currentTerm),
                        next_term_function= self._nextTermFunc)

    def __repr__(self) -> str:
        """Creates a string representation of a sequence object"""
        return f"""sequence(currentTerm = {self._currentTerm},
                   nextTermFunc = {self._nextTermFunc.__name__})"""

    def __str__(self) -> str:
        """Creates an informal representation of a sequence object"""
        return repr(self)
