import asyncio

from tracker.task import MapTask, ReduceTask
from utils.radom import gen_random_id


class JobTracker(object):
    def __init__(self):
        self.jobs_queue = []
        self.loop = asyncio.get_event_loop()

    def submit(self, job):
        self.jobs_queue.append(job)

        self.dispatch()

    def dispatch(self):
        job = self.jobs_queue.pop()
        map_tasks = []
        for split in job.input_splits:
            map_task = MapTask(uuid=gen_random_id(), input_split=split,
                               mapper=job.mapper, context=job.context)

            map_tasks.append(map_task.exec_map())

        self.async_exec(tasks=map_tasks)

        shuffled = self.shuffle(job.context)

        reduce_tasks = []
        for key in shuffled:
            reduce_task = ReduceTask(uuid=gen_random_id(), key=key, values=shuffled[key], reducer=job.reducer,
                                     context=job.context)

            reduce_tasks.append(reduce_task.exec_reduce())

        self.async_exec(tasks=reduce_tasks)

        self.loop.close()

        job.finish()

    def shuffle(self, context):
        result = {}
        for k in context.data():
            result[k[0]] = result[k[0]] + (k[1],) if k[0] in result.keys() else (k[1],)
        return result

    def async_exec(self, tasks):
        self.loop.run_until_complete(asyncio.wait(tasks))
