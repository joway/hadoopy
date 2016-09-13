from tracker.task import Task


class JobTracker(object):
    def __init__(self):
        self.queue = []

    def submit(self, job):
        self.queue.append(job)

        # TODO
        self.dispatch()

    def dispatch(self):
        job = self.queue.pop()
        for split in job.input_splits:
            task = Task(input_split=split, mapper=job.mapper, reducer=job.reducer)
            task.start()
