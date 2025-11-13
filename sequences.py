# This work is governed under the CC0 licence https://creativecommons.org/publicdomain/zero/1.0/

from collections.abc import Callable
from decimal import Decimal

class nextFunctions:
    @staticmethod
    def linear(increment: Decimal) -> Callable[[sequence], sequence]:
        """Creates a lambda incrementing input values by a given increment"""
        raise NotImplementedError("nextFunctions.linear is not implemented")

    @staticmethod
    def geometric(multiplier: Decimal) -> Callable[[sequence], sequence]:
        """Creates a lambda multiplying input values by a given multiplier"""
        raise NotImplementedError("nextFunctions.geometric is not implemented")

class sequence:
    def __init__(self: sequence,
                 currentTerm: Decimal | float,
                 nextTermFunction: Callable[[sequence], sequence] = nextFunctions.linear(Decimal(1))
                 ) -> None:
        """Initialises a sequence object

        :param currentTerm: Decimal determines current term in the sequence
        :param nextTermFunction: Callable function to determine next term in sequence"""
        raise NotImplementedError("sequence.__init__ is not implemented")

    def getCurrentTerm(self: sequence) -> Decimal:
        """Gets the current term of the object"""
        raise NotImplementedError("sequence.getCurrentTerm is not implemented")

    def nextTerm(self: sequence) -> sequence:
        """Creates a sequence object for the next term"""
        raise NotImplementedError("sequence.nextTerm is not implemented")

    def __repr__(self) -> str:
        """Creates a string representation of a sequence object"""
        raise NotImplementedError("sequence.__repr__ is not implemented")

    def __str__(self) -> str:
        """Creates an informal representation of a sequence object"""
        raise NotImplementedError("sequence.__str__ is not implemented")
