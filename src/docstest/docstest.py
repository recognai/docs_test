"""This is a module doc string

This module is all about testing the docs.
"""
from typing import Optional


class DocsTest:
    """This is a class doc string"""
    def __init__(self, a: str, b: Optional[float] = None):
        self.a = a
        self.b = b
        self.d = None

    def method_a(self, aa: int) -> bool:
        """Some method doc string

        Parameters
        ----------
        aa : int
            Just a parameter

        Returns
        -------
        bool
        """
        print(self.a)
        return True
