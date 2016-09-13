from utils.radom import gen_random_id


class Job(object):
    def __init__(self, filenames, mapper, reducer, input_splits):
        self.id = gen_random_id()
        self.filenames = filenames
        self.mapper = mapper
        self.reducer = reducer
        self.input_splits = input_splits

