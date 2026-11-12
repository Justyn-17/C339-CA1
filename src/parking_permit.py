def is_permit_valid(permit_active, parked_minutes):
    """Determine whether an active permit covers the parking stay."""
    if type(permit_active) is not bool or type(parked_minutes) is not int:
        raise TypeError("invalid argument type")
    
    if parked_minutes < 0:
        raise ValueError("argument outside permitted range")
    
    if permit_active and parked_minutes <= 120:
        return 1
    
    return False
