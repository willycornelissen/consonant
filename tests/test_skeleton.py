#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from consonant.skeleton import fib

__author__ = "Willy Garabini Cornelissen"
__copyright__ = "Willy Garabini Cornelissen"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
