from abc import abstractmethod


class Reducer(object):
    @abstractmethod
    def reduce(self, key, values):
        pass
