class Task(object):
    def __init__(self, input_split, mapper, reducer):
        self.input_split = input_split
        self.mapper = mapper
        self.reducer = reducer

    def start(self):
        with open(self.input_split['filename']) as file:
            file.seek(self.input_split['begin_at'])
            print(file.read(self.input_split['end_at'] - self.input_split['begin_at']))
