#!/usr/bin/env python2

import socket

import OSC


DEFAULT_SERVER_ADDRESS = '127.0.0.1', 9000


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = '/example/echo'
    msg = 'test', 123
    oscmsg = OSC.OSCMessage(address, msg)
    sock.sendto(oscmsg.getBinary(), DEFAULT_SERVER_ADDRESS)


if __name__ == '__main__':
    main()
