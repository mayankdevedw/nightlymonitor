class SharedObject(object):
    failCount = 0
    passCount = 0

    def __init__(self, total):
        self.total = total

    @staticmethod
    def increment_fail_count():
        SharedObject.failCount += 1

    @staticmethod
    def increment_pass_count():
        SharedObject.passCount += 1

    @staticmethod
    def decrement_fail_count():
        SharedObject.failCount -= 1

    @staticmethod
    def decrement_pass_count():
        SharedObject.passCount -= 1

    @staticmethod
    def fail_percent(self):
        return (SharedObject.failCount / self.total) * 100
