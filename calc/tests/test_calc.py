#!/usr/bin/env python

"""Tests for `calc` package."""

import pytest


from calc.calc import Calc

def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)
    assert res == 9
