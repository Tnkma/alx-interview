#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Checks if a data set represents a valid UTF-8 encoding

    Args:
        data (list of int): The data set to validate
    """

    # Handle empty data list
    if not data:
        return True

    byte_number = 0
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    # Iterate over each number in the data list
    for num in data:
        # Ensure the number is within the valid byte range (0-255)
        if num < 0 or num > 255:
            return False

        # Work with the last 8 bits
        byte = num & 0xFF

        if byte_number == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                byte_number += 1
                mask >>= 1

            # If byte_number is 0, it's a single-byte character (0xxxxxxx)
            if byte_number == 0:
                continue

            # If byte_number is 1 or more than 4, it's invalid
            if byte_number == 1 or byte_number > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the byte_number
        byte_number -= 1
    # If byte_number is not 0, there are missing continuation bytes
    return byte_number == 0
