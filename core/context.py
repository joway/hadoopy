class Context(object):
    def __init__(self):
        self.context = []

    def write(self, key, value):
        self.context.append((key, value))

    def data(self):
        return self.context
