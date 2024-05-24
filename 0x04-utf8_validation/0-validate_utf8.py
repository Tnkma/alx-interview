#!/usr/bin/env python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Checks if a data set represents a valid UTF-8 encoding

    Args:
        data (int, optional): _description_ The data set to validate
    """
    # set he byte to o first
    byte_number = 0
    # get the mask of the most significant bit
    mask1 = 1 << 7
    mask2 = 1 << 6

    # iterate over the data
    for num in data:
        # Ensure were only counting the last 8 bits
        byte = num & 0xFF
        # if byte number is 0
        if byte_number == 0:
            # count the number of bits in the byte
            while byte & (mask1 << byte_number):
                # increment the byte number
                byte_number += 1
            # if the byte is 0, it is a single byte character
            if byte_number == 0:
                return True
            # if the byte is more than 4 bytes long, it is invalid
            if byte_number == 1 or byte_number > 4:
                return False
        else:
            # if the byte is not a continuation byte, it is invalid
            if not (byte & mask1 and not (byte & mask2)):
                return False
        # decrement the byte number
        byte_number -= 1
        return byte_number == 0
