import pytest
from src.parking_fee import calculate_parking_fee

#Testing the minutes that cost the expected price 
@pytest.mark.parametrize(
    "minutes, expected",
    [
        (0, 0),        # PKM-FEE-TC-001 0 min costs 0
        (1, 200),      # PKM-FEE-TC-002 1 min costs 200
        (30, 200),     # PKM-FEE-TC-003 30 mins costs 200
        (59, 200),     # PKM-FEE-TC-004 59 mins costs 200
        (60, 200),     # PKM-FEE-TC-005 1 hr costs 200
        (61, 400),     # PKM-FEE-TC-006 1 hr 1 min costs 400
        (119, 400),    # PKM-FEE-TC-007 1 hr 59 mins costs 400
        (120, 400),    # PKM-FEE-TC-008 2 hrs costs 400
        (121, 600),    # PKM-FEE-TC-009 2 hrs 1 min costs 600
        (1440, 4800),  # PKM-FEE-TC-010 24 hrs costs 4800
    ],
)
def test_valid_minutes_return_correct_charge(minutes, expected):
    assert calculate_parking_fee(minutes) == expected


# PKM-FEE-TC-011: charge must be returned as an int (cents)
def test_return_type_is_int():
    assert type(calculate_parking_fee(61)) is int


# PKM-FEE-TC-012: negative minutes raise ValueError
def test_negative_minutes_raise_value_error():
    with pytest.raises(ValueError):
        calculate_parking_fee(-1)


# PKM-FEE-TC-013 to 015: wrong data type raises TypeError
@pytest.mark.parametrize(
    "minutes",
    [
        True,    # PKM-FEE-TC-013 bool is not a valid int (General Req 2)
        False,   # PKM-FEE-TC-013
        60.0,    # PKM-FEE-TC-014 float that looks like a whole number
        "60",    # PKM-FEE-TC-015 string
    ],
)
def test_invalid_type_raises_type_error(minutes):
    with pytest.raises(TypeError):
        calculate_parking_fee(minutes)