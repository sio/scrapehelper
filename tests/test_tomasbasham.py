'''
These unit tests were adapted from https://github.com/tomasbasham/ratelimit
'''

# The MIT License (MIT)
#
# Copyright (c) 2019 Tomas Basham
#                    and contributors to https://github.com/tomasbasham/ratelimit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from time import sleep
from unittest import TestCase
from concurrent.futures import ThreadPoolExecutor, as_completed
from scrapehelper.limit import RateLimiter, RateLimitReachedError


class Clock(object):
    def __init__(self):
        self.reset()

    def __call__(self):
        return self.now

    def __repr__(self):
        return '<Fake clock: {}>'.format(self.now)

    def reset(self):
        self.now = 0

    def increment(self, num=1):
        self.now += num


CLOCK_STEP = 5  # The longest test will take this much seconds
clock = Clock()


class limits(RateLimiter):
    '''RateLimiter with mocked clock'''
    clock = clock


class TestDecorator(TestCase):

    @limits(calls=1, interval=CLOCK_STEP, wait=False)
    def api_hit_nowait(self):
        '''
        Increment the counter at most once every CLOCK_STEP seconds.
        '''
        self.count += 1

    @limits(calls=1, interval=CLOCK_STEP)
    def api_hit_wait(self):
        '''
        Increment the counter at most once every CLOCK_STEP seconds, but w/o raising an
        exception when reaching limit.
        '''
        self.count += 1

    def setUp(self):
        self.count = 0
        clock.increment(CLOCK_STEP)

    def test_increment(self):
        self.api_hit_nowait()
        self.assertEqual(self.count, 1)

    def test_exception(self):
        self.api_hit_nowait()
        self.assertRaises(RateLimitReachedError, self.api_hit_nowait)

    def test_reset(self):
        self.api_hit_nowait()
        for _ in range(CLOCK_STEP):
            with self.subTest(_=_, clock=clock.now):
                self.assertRaises(RateLimitReachedError, self.api_hit_nowait)
            clock.increment()

        self.api_hit_nowait()
        self.assertEqual(self.count, 2)

    def test_no_exception(self):
        threads = ThreadPoolExecutor()
        futures = set()
        for _ in range(2):
            futures.add(threads.submit(self.api_hit_wait))

        def done_count():
            return len([f for f in futures if f.done()])

        for _ in range(CLOCK_STEP):
            with self.subTest(clock=clock.now, _=_):
                self.assertEqual(done_count(), 1)  # Second job is waiting for interval to pass
            clock.increment()
        for future in as_completed(futures):
            future.result()  # Wait for all threads and check that no exceptions are raised
        self.assertEqual(done_count(), 2)
