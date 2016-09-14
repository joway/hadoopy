from abc import abstractmethod


class Mapper(object):
    @abstractmethod
    def map(self, key, value, context):
        pass
