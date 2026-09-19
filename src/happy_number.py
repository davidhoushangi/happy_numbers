# code here

def is_happy(n):
    """
    This function takes a number (an integer)

    Args:
        n (_int_): _description_

    Returns:
        _bool_: True fir happy numbers and False for NOT happy numbers    
    """
    seen_numbers = set()
    while (n != 1) and (n not in seen_numbers):
        seen_numbers.add(n)
        n = sum([(int(i)**2) for i in str(n)])

    return n == 1

if __name__ == "__main__":
    assert is_happy(7) is True
    assert is_happy(45) is False
