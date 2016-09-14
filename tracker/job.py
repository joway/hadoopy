from core.context import Context
from utils.radom import gen_random_id


class Job(object):
    def __init__(self, filenames, mapper, reducer, input_splits):
        self.id = gen_random_id()
        self.filenames = filenames
        self.context = Context()
        self.tasks = []
        self.mapper = mapper
        self.reducer = reducer
        self.input_splits = input_splits

    def finish(self):
        with open('output.txt', 'w') as file:
            for i in self.context.data():
                file.write(str(i[0]) + ' ' + str(i[1]) + '\n')
