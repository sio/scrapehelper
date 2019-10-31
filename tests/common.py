'''
Common objects for unit tests
'''


from scrapehelper.limit import RateLimiter


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


class limits(RateLimiter):
    '''RateLimiter with mocked clock'''
    clock = Clock()
