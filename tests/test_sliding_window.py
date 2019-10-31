'''
Unit tests for sliding window algorithm

More information: https://github.com/tomasbasham/ratelimit/issues/31
'''


import random
from unittest import TestCase

from scrapehelper.limit import RateLimitReachedError
from tests.common import limits


CALLS = random.randint(2, 20)
INTERVAL = random.randint(21, 60)

clock = limits.clock


class TestSlidingWindow(TestCase):

    def setUp(self):
        self.hits = 0
        clock.increment(INTERVAL)

    @limits(calls=CALLS, interval=INTERVAL, wait=False)
    def api_hit(self):
        self.hits += 1

    def test_sliding_window(self):
        # First hit is separated from others
        self.api_hit()
        clock.increment(INTERVAL - 1)

        # Exhaust rate limit
        for _ in range(CALLS - 1):
            self.api_hit()

        # This one is outside of INTERVAL after first hit.
        # It is the last hit allowed by the sliding window.
        clock.increment()
        self.api_hit()

        # This one does not violate fixed time window based on the first hit, but
        # violates the sliding window calculated for the second hit
        self.assertRaises(RateLimitReachedError, self.api_hit)
