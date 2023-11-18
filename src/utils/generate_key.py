import secrets


def generate_api_key(length=32):
    """
    Generate a random API key.

    Args:
    - length (int): Length of the API key.

    Returns:
    - str: Generated API key.
    """
    return secrets.token_hex(length)


# Example usage
api_key = generate_api_key()
print(api_key)

if __name__ == "__main__":
    generate_api_key(100)
