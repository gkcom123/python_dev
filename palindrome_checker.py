def is_palindrome(text: str) -> bool:
    """
    Check if a given string is a palindrome.
    
    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.
    
    Args:
        text: The string to check
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def is_strict_palindrome(text: str) -> bool:
    """
    Check if a string is a strict palindrome (case-sensitive, includes all characters).
    
    Args:
        text: The string to check
        
    Returns:
        True if the string is a strict palindrome, False otherwise
    """
    return text == text[::-1]


if __name__ == "__main__":
    test_strings = [
        "radar",
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "Madam",
        "12321",
        "",
    ]
    
    print("Palindrome Checker Results")
    print("=" * 50)
    
    for s in test_strings:
        result = is_palindrome(s)
        status = "✓ Palindrome" if result else "✗ Not a palindrome"
        print(f'"{s}" -> {status}')
