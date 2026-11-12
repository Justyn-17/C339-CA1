import pytest

from src.parking_permit import is_permit_valid 

@pytest.mark.parametrize(
    "parked_minutes",
    [
        0,    # TC-P01 BVA lower boundary ("including zero")
        60,   # TC-P02 EP valid middle value
        119,  # TC-P03 BVA just below limit
        120,  # TC-P04 BVA exactly at limit ("at most 120")
    ],
)
def test_active_permit_within_limit_is_valid(parked_minutes):
    assert is_permit_valid(True, parked_minutes) is True

# It's true that have permit but is longer then 121 minutes --> so its false #TC-P05
def test_active_permit_over_limit_is_not_valid():
    assert is_permit_valid(True, 121) is False

# Testing for when permit is false but still got park at least a duration
@pytest.mark.parametrize(
    "parked_minutes",
    [
        60,   # TC-P06 EP inactive, within limit
        130,  # TC-P07 EP inactive, over limit
    ],
)
def test_inactive_permit_is_not_valid(parked_minutes):
    assert is_permit_valid(False, parked_minutes) is False

# Test that permit is true but is -1 min so it's value error
def test_negative_minutes_raise_value_error():
    with pytest.raises(ValueError):
        is_permit_valid(True, -1)  # TC-P08 BVA just below 0


# Testing for type error in permit even its valid minutes
@pytest.mark.parametrize(
    "permit_active",
    [
        1,       # TC-P09 int instead of bool (only True/False accepted)
        "True",  # TC-P10 string instead of bool
    ],
)
def test_invalid_permit_active_type_raises_type_error(permit_active):
    with pytest.raises(TypeError):
        is_permit_valid(permit_active, 60)

# Testing for type error in minutes parked even its valid permit 
@pytest.mark.parametrize(
    "parked_minutes",
    [
        True,   # TC-P11 bool is not a valid int
        60.0,   # TC-P12 float that looks like a whole number
        "60",   # TC-P13 string
    ],
)
def test_invalid_parked_minutes_type_raises_type_error(parked_minutes):
    with pytest.raises(TypeError):
        is_permit_valid(True, parked_minutes)

