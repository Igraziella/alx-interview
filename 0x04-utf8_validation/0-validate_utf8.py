#!/usr/bin/python3
"""UTF-8 encoding method"""


def validUTF8(data):
    """Determines if a given set of data represents
    a valid UTF-8 encoding
    """
    num_bytes_to_follow = 0
    
    for num in data:
        if num_bytes_to_follow > 0:
            if (num >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1
        else:
            if (num >> 7) == 0b0:
                # Single-byte character (ASCII)
                continue
            elif (num >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (num >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (num >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
    
    return num_bytes_to_follow == 0
