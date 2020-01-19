#!/bin/python

import os
import sys
import subprocess
import logging

class Caller:
    def __init__(self, logger=None):
        self.logger = logger if logger else logging

    def __error(self, cmd, ex):
        self.logger.error('calling \"{}\" produced : \"{}\"'.format(cmd, ex))

    def __os_call(self, *argv):
        try:
            self.logger.info(subprocess.check_output(argv))
        except Exception as ex:
            self.__error(' '.join([str(i) for i in argv]), ex)

    def call_sh(self, filename, *argv):
        self.__os_call('sudo', 'chmod', '+x', filename)
        self.__os_call('su', '-', 'pi', '-c', filename)

    def call_python(self, filename, *argv):
        self.__os_call(['su', '-', 'pi', '-c', '"python \"{}\""'.format(filename)]+argv)

    def call(self, filename, *argv):
        self.logger.info('calling \"{}\" with args {}'.format(filename, ' '.join([str(i) for i in argv])))

        filename = filename if filename[:2] == './' else ''.join(['./', filename])
        argv = ' '.join([str(i) for i in argv])

        if filename[-3:] == '.py':
            self.call_python(filename, argv)
        else:
            self.call_sh(filename, argv)
