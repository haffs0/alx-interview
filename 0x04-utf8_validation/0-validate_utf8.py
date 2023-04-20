#!/usr/bin/python3
"""define validUTF8 function"""


def validUTF8(data):
    """return True if its a validUTF8 or False otherwise"""
    data_len = len(data)
    for i in range(data_len):
        curr = data[i]
        byte_type = get_type(curr)
        if byte_type == 0:
            continue
        elif byte_type > 1 and i + byte_type <= data_len:
            while byte_type > 1:
                if get_type(data[++i]) != 1:
                    return False
                byte_type -= 1
        else:
            return False
    return True


def get_type(num: int):
    """return type"""
    masks = [128, 64, 32, 16, 8]
    for i in range(5):
        if (masks[i] & num) == 0:
            return i
    return -1
