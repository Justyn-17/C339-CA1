def calculate_parking_fee(minutes):
    """Calculate the charge for a stay measured in whole minutes."""
    if type(minutes) is not int:
        raise TypeError("invalid argument type")
    
    if minutes < 0:
        raise ValueError("argument outside permitted range")
    
    return (minutes // 60) * 200
