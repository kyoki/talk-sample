"""

The Tracker class is used to allocate servers. You should be able to
allocate new servers and deallocate existing servers. When allocating
servers, it should return the next available lowest number that has
not yet been allocted, starting with 1:

example:
tracker = Tracker()
print tracker.allocate('apibox') => 'apibox1'
print tracker.allocate('apibox') => 'apibox2'

Each host type should start over from 1, regardless of what other
boxes have been allocated:

print tracker.allocate('sitebox') => 'sitebox1'
print tracker.allocate('apibox') => 'apibox3'

Deallocating a server should make that number available again:
tracker.deallocate('apibox2')
print tracker.allocate('apibox') => 'apibox2'
print tracker.allocate('apibox') => 'apibox4'

"""

from collections import defaultdict
import re
import unittest

class Tracker(object):

    def __init__(self):
        # maps host types to server numbers
        self.host_types = defaultdict(list)

    def allocate(self, host_type):
        next_number = self._next_server_number(self.host_types[host_type])
        self.host_types[host_type].append(next_number)
        return host_type+str(next_number)

    def deallocate(self, hostname):
        matched = re.search('([a-zA-Z]+)(\d+)', hostname)
        if not matched:
            return None
        host_type = matched.group(1)
        server_number = matched.group(2)
        server_numbers = self.host_types[host_type]
        if server_number in server_numbers:
            server_numbers.remove(server_number)
        return None

    def _next_server_number(self, server_number_list):
        server_number = 1
        while server_number in server_number_list:
            server_number += 1
        return server_number


class Tests(unittest.TestCase):

    def setUp(self):
        self.tracker = Tracker()

    def test_allocate(self):
        self.assertEqual(self.tracker.allocate('apibox'), 'apibox1')

if __name__ == '__main__':
    unittest.main()
