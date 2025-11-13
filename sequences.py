# This work is governed under the CC0 licence https://creativecommons.org/publicdomain/zero/1.0/

from collections.abc import Callable
from decimal import Decimal

class nextFunctions:
    @staticmethod
    def linear(increment: Decimal) -> Callable[[Decimal], Decimal]:
        """Creates a lambda incrementing input values by a given increment"""
        raise NotImplementedError("nextFunctions.linear is not implemented")

    @staticmethod
    def geometric(multiplier: Decimal) -> Callable[[Decimal], Decimal]:
        """Creates a lambda multiplying input values by a given multiplier"""
        raise NotImplementedError("nextFunctions.geometric is not implemented")

class sequence:
    def __init__(self: sequence,
                 currentTerm: Decimal | float,
                 nextTermFunction: Callable[[Decimal], Decimal] = nextFunctions.linear(Decimal(1))
                 ) -> None:
        """Initialises a sequence object

        :param currentTerm: Decimal determines current term in the sequence
        :param nextTermFunction: Callable function to determine next term in sequence"""
        self._currentTerm: Decimal = Decimal(currentTerm)
        self._nextTermFunc: Callable[[Decimal], Decimal] = nextTermFunction

    def getCurrentTerm(self: sequence) -> Decimal:
        """Gets the current term of the object"""
        return self._currentTerm

    def nextTerm(self: sequence) -> sequence:
        """Creates a sequence object for the next term"""
        raise NotImplementedError("sequence.nextTerm is not implemented")

    def __repr__(self) -> str:
        """Creates a string representation of a sequence object"""
        raise NotImplementedError("sequence.__repr__ is not implemented")

    def __str__(self) -> str:
        """Creates an informal representation of a sequence object"""
        raise NotImplementedError("sequence.__str__ is not implemented")
