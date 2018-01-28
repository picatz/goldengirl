#!/usr/bin/env python

# Copyright (C) 2007 Giampaolo Rodola' <g.rodola@gmail.com>.
# Use of this source code is governed by MIT license that can be
# found in the LICENSE file.

"""
A FTP server which handles every connection in a separate thread.
Useful if your handler class contains blocking calls or your
filesystem is too slow.
"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
import os

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('root', 'picat', os.getcwd(), perm='elradfmwMT')
    authorizer.add_user('picat', 'picat', os.getcwd(), perm='elradfmwMT')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('', 21), handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
