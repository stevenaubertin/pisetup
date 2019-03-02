#!/bin/python

import os
import sys

def call(filename, args):
    filename = filename if filename[:2] == './' else ''.join(['./', filename])
    args = ' '.join([str(i) for i in args[2:]])

    os.system(''.join(['sudo chmod +x ', filename]))
    os.system(''.join(['sudo ', filename, ' ', args]))
