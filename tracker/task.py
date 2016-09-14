import threading


class Task(object):
    def __init__(self, uuid, context):
        self.uuid = uuid
        self.context = context

    def async_exec(self, func, *args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
        t.start()


class MapTask(Task):
    def __init__(self, uuid, input_split, mapper, context):
        super().__init__(uuid=uuid, context=context)
        self.input_split = input_split
        self.mapper = mapper

    async def exec_map(self):
        with open(self.input_split['filename']) as file:
            file.seek(self.input_split['begin_at'])
            content = file.read(self.input_split['end_at'] - self.input_split['begin_at'])
            self.mapper.map(key=self.uuid,
                            value=content,
                            context=self.context)


class ReduceTask(Task):
    def __init__(self, uuid, key, values, reducer, context):
        super().__init__(uuid=uuid, context=context)
        self.reducer = reducer
        self.key = key
        self.values = values

    async def exec_reduce(self):
        self.reducer.reduce(key=self.key, values=self.values, context=self.context)
