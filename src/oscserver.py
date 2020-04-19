import logging
import errno
import socket

import OSC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


RECV_BUF_SZ = 65536


class OSCServer(object):

    def __init__(
            self, server_address, remote_address, prefix=''):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.setblocking(0)

        self.server_address = server_address
        self.remote_address = remote_address

        self._socket.bind(self.server_address)

        self.prefix = prefix
        self._callback_manager = OSC.CallbackManager()
        self.add_callback('/set_peer', self._set_peer)

    def _prefixed(self, address):
        return '%s%s' % (self.prefix, address)

    def add_callback(self, address, callback):
        self._callback_manager.add(self._prefixed(address), callback)

    def _handle(self, data, addr):
        try:
            self._callback_manager.handle(data, addr)
        except OSC.NoSuchCallback:
            logger.warn('No such callback. data=%s' % repr(data))

    def send(self, address, msg):
        oscmsg = OSC.OSCMessage(address, msg)
        self._socket.sendto(oscmsg.getBinary(), self.remote_address)

    def send_message(self, message):
        self._socket.sendto(message.getBinary(), self.remote_address)

    def _set_peer(self, msg, source):
        host = msg[2]
        if host == '':
            host = source[0]
        port = msg[3]
        self.remote_address = host, port

    def process(self):
        while True:
            try:
                data, addr = self._socket.recvfrom(RECV_BUF_SZ)
            except socket.error, e:
                try:
                    e_errno = e.errno
                except AttributeError:
                    e_errno = e[0]
                if e_errno == errno.EAGAIN:
                    return
                raise
            else:
                self._handle(data, addr)
