import pytest

from src.parking_permit import is_permit_valid 

@pytest.mark.parametrize(
    "parked_minutes",
    [
        0,    # PKM-PMT-TC-001 BVA lower boundary ("including zero")
        60,   # PKM-PMT-TC-002 EP valid middle value
        119,  # PKM-PMT-TC-003 BVA just below limit
        120,  # PKM-PMT-TC-004 BVA exactly at limit ("at most 120")
    ],
)
def test_active_permit_within_limit_is_valid(parked_minutes):
    assert is_permit_valid(True, parked_minutes) is True

# It's true that have permit but is longer then 121 minutes --> so its false #PKM-PMT-TC-005
def test_active_permit_over_limit_is_not_valid():
    assert is_permit_valid(True, 121) is False

# Testing for when permit is false but still got park at least a duration
@pytest.mark.parametrize(
    "parked_minutes",
    [
        60,   # PKM-PMT-TC-006 EP inactive, within limit
        130,  # PKM-PMT-TC-007 EP inactive, over limit
    ],
)
def test_inactive_permit_is_not_valid(parked_minutes):
    assert is_permit_valid(False, parked_minutes) is False

# Test that permit is true but is -1 min so it's value error
def test_negative_minutes_raise_value_error():
    with pytest.raises(ValueError):
        is_permit_valid(True, -1)  # PKM-PMT-TC-008 BVA just below 0


# Testing for type error in permit even its valid minutes
@pytest.mark.parametrize(
    "permit_active",
    [
        1,       # PKM-PMT-TC-009 int instead of bool (only True/False accepted)
        "True",  # PKM-PMT-TC-010 string instead of bool
    ],
)
def test_invalid_permit_active_type_raises_type_error(permit_active):
    with pytest.raises(TypeError):
        is_permit_valid(permit_active, 60)

# Testing for type error in minutes parked even its valid permit 
@pytest.mark.parametrize(
    "parked_minutes",
    [
        True,   # PKM-PMT-TC-011 bool is not a valid int
        60.0,   # PKM-PMT-TC-012 float that looks like a whole number
        "60",   # PKM-PMT-TC-013 string
    ],
)
def test_invalid_parked_minutes_type_raises_type_error(parked_minutes):
    with pytest.raises(TypeError):
        is_permit_valid(True, parked_minutes)

# Concurrency test 1