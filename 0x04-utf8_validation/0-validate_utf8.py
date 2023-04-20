#!/usr/bin/python3
"""define validUTF8 function"""


def validUTF8(data):
    """return True if its a validUTF8 or False otherwise"""
    data_len = len(data)
    count = 0
    for i in range(data_len):
        x = data[i]
        if not count:
            if (x >> 5) == 0b110:
                count = 1
            elif (x >> 4) == 0b1110:
                count = 2
            elif (x >> 3) == 0b11110:
                count = 3
            elif (x >> 7) != 0:
                return False
        else:
            if (x >> 6) != 0b10:
                return False
            count -= 1
    return count == 0
