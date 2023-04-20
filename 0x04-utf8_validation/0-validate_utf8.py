#!/usr/bin/python3
"""define validUTF8 function"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """return True if its a validUTF8 or False otherwise"""
    data_len = len(data)
    count = 0
    for i in range(data_len):
        if count == 0:
            if (data[i] >> 5) == 0b110:
                count = 1
            elif (data[i] >> 4) == 0b1110:
                count = 2
            elif (data[i] >> 3) == 0b11110:
                count = 3
            elif (data[i] >> 7) == 1:
                return False
        else:
            if (data[i] >> 6) != 2:
                return False
            count -= 1
    return count == 0
