#!/bin/python

import os
import subprocess
import logging

class Caller:
    def __init__(self, logger=None):
        self.logger = logger if logger else logging

    def __error(self, cmd, ex):
        self.logger.error('calling \"{}\" produced : \"{}\"'.format(cmd, ex))

    def os_call(self, *argv):
        try:
            self.logger.info(subprocess.check_output(argv))
        except Exception as ex:
            self.__error(' '.join([str(i) for i in argv]), ex)

    def call_sh(self, filename, *argv):
        self.os_call('sudo', 'chmod', '+x', filename)
        self.os_call(['su', '-', 'pi', '-c', filename]+[str(i) for i in argv])

    def call_python(self, filename, *argv):
        self.os_call(['su', '-', 'pi', '-c', '"python \"{}\""'.format(filename)]+[str(i) for i in argv])

    def call(self, filename, *argv):
        self.logger.info('calling \"{}\" with args {}'.format(filename, ' '.join([str(i) for i in argv])))

        name, ext = os.path.splitext(filename)

        if ext == '.py':
            self.call_python(filename, argv)
        if ext == '.sh':
            self.call_sh(filename, argv)
        
        raise 'Unable to call {}'.format(filename)