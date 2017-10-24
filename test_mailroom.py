"""Mailroom Madness Tests."""
import pytest


def test_get_name_true():
    """Gets the name of donor"""
    from mailroom import check_name
    assert check_name("Tony Stark") == True


def test_get_name_false():
    """Makes sures name is fake"""
    from mailroom import check_name
    assert check_name("Barry Allen") == False


def test_is_valid_donation_is_true():
    """Tests to make sure donation is true """
    from mailroom import check_donation
    assert check_donation("500") == True

def test_is_valid_donation_is_false():
    """Makes sure donation isnt false"""
    from mailroom import check_donation
    assert check_donation("xxx") == False


def test_create_email():
    """Verifyies email is correct"""
    from mailroom import create_email
    assert create_email("Tony Stark", 150) == "$150! Thanks for the Donation Tony!"


def test_get_average_donation():
    """Get's donar donation average"""
    from mailroom import get_average_donation
    assert get_average_donation([20, 500, 10]) == '176.67'
