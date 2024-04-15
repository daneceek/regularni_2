import re
def validate_email(email:str) -> bool:
    """
    This function checks if the given email address is valid or not.

    :param email: email address
    :type email: str
    :return: boolean value of valitation
    :rtype: bool
    """
    
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))