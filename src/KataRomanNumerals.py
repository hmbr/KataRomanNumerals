#!/usr/bin/env python

import collections

table = collections.OrderedDict(
    [
        (1000, 'M'),
        (500, 'D'),
        (100, 'C'),
        (50, 'L'),
        (10, 'X'),
        (5, 'V'),
        (1, 'I')
    ])


def convert_to_arabic(value):

    converted = ""
    temp = ""
    previous = ""

    for num in table.keys():

        while value >= num:
            temp = temp + table[num]
            value = value - num

        if len(temp) == 4:
            temp = table[num] + table[previous]

            if converted is not "" and converted[-1] == temp[-1]:
                converted = converted[:-1]
                temp = table[num] + table[2 * previous]

        converted = converted + temp
        temp = ""
        previous = num

    return converted
