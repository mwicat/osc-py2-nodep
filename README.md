# osc-py2-nodep

This repository serves as a packaging for OSC.py module together with some sample
code for server and client.

OSC.py is a simple module implementing OSC protocol encoding that does not
depend on external packages. It runs on Python 2.x only and is simple enough
to wrap it around simple non-blocking UDP socket implementation. These
features are especially useful for embedded environments and scripting
in applications. For example, in audio software like Ableton Live and Reaper
it's not only discouraged to depend on multithreading in your scripts,
but doing so can lead to bugs and crashes.

Here you can find OSC.py module from 2002 by Daniel Holth and Clinton McChesney.
I also included example_client.py and example_server.py showing
how you can implement server and client communication in practice. Server code
is inspired by [LiveOSC control surface](https://github.com/stufisher/LiveOSC2). 
Examples are tested against Python 2.5, 2.6 and 2.7.