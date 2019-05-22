#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the awesome module.
because it is good
"""
import pytest

from awesome import awesome


def test_something():
    assert True
	
def test_addingNumber():
	assert awesome.addNumbers(1,1) == 2, "adding 1+1=2"
	assert awesome.addNumbers(1,2) != 2, "not equal"

def something_else():
	assert FALSE
		
from unittest.mock import patch, Mock

@patch("requests.get")
def test_wordcount(mock):
	mock.return_value = Mock()
	mock.return_value.text = "text"
	
	bookurl="https://www.gutenberg.org/files/59560/59560-0.txt"
	wc = awesome.wordcount(bookurl)
	assert wc == 1

def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_awesome(an_object):
    assert an_object == {}
