# Copyright (C) 2013 Itzik Kotler
#
# This file is part of Hackersh.
#
# Hackersh is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# Hackersh is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hackersh; see the file COPYING.  If not,
# see <http://www.gnu.org/licenses/>.

# Local imports

import hackersh.components.external


# Metadata

__author__ = "Itzik Kotler <xorninja@gmail.com>"
__version__ = "0.1.1"


# Implementation

class Ping(hackersh.components.external.ExternalComponentReturnValueOutput):
    """Send ICMP ECHO_REQUEST to Network Hosts. Ping uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway."""

    def _processor(self, context, retval):

        _context = dict()

        if retval == 0:

            _context['PINGABLE'] = True

        return _context

    # Consts

    DEFAULT_FILENAME = "ping"

    DEFAULT_OUTPUT_OPTIONS = "-c 3"

    DEFAULT_QUERY = DEFAULT_FILTER = "IPV4_ADDRESS or HOSTNAME"
