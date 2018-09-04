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


if __name__ == '__main__':
    unittest.main()
