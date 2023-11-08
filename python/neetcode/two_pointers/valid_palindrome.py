def is_palindrome(s: str) -> bool:
    """Given a string s, return true if it is a palindrome, or false otherwise

    Args:
        s (str): string to test

    Returns:
        bool: true if it is a palindrome, or false otherwise
    """
    s = [char for char in s.lower() if char.isalnum()]
    return s == s[::-1]