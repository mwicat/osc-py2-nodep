"""

Installation instructions:

1. Copy OSC.py and oscserver.py to Reaper scripts directory

Example for MacOS:

$ cp OSC.py oscserver.py "$HOME/Library/Application Support/REAPER/Scripts"

2. Open Actions -> ReaScript -> New... and insert contents of this file

3. Save and run!

"""

import logging
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


def run_reaper():
    server.process()
    RPR_defer('server.process()')


server = ExampleOSCServer(DEFAULT_SERVER_ADDRESS, DEFAULT_REMOTE_ADDRESS)
run_reaper()
