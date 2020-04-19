#!/usr/bin/env python2

import logging
from time import sleep

from oscserver import OSCServer


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DEFAULT_SERVER_ADDRESS = '127.0.0.1', 9000
DEFAULT_REMOTE_ADDRESS = '127.0.0.1', 9001


class ExampleOSCServer(OSCServer):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('prefix', '/example')
        super(ExampleOSCServer, self).__init__(*args, **kwargs)
        self.add_callback('/echo', self._handle_echo)

    def _handle_echo(self, msg, source):
        args = msg[2:]
        logger.info('Echo message from %s: %s' % (source, msg))
        self.send('/echo', args)


def main():
    server = ExampleOSCServer(DEFAULT_SERVER_ADDRESS, DEFAULT_REMOTE_ADDRESS)
    while True:
        server.process()
        sleep(0.1)


if __name__ == '__main__':
    main()
