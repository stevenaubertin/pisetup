#!/bin/python

import sys

from uuid import getnode


def get_mac():
    chunk_size = 2

    def split(head, tail):
        if tail is '':
            return [head.upper()]
        return [head.upper()] + split(tail[:chunk_size], tail[chunk_size:])

    val = format(getnode(), '0x')
    return ':'.join(split(val[:chunk_size], val[chunk_size:]))


if __name__ == "__main__":
    print(get_mac())
    sys.exit(0)
