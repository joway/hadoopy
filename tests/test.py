from tests.test_mapper import TestMapper
from tests.test_reducer import TestReducer
from tracker.job import Job
from tracker.jobtracker import JobTracker
from utils.hdfs import split_with_line

FILENAME = 'words.list'
with open(FILENAME, 'r') as file:
    words_list = file.read()

job_tracker = JobTracker()
job = Job([FILENAME], mapper=TestMapper, reducer=TestReducer, input_splits=split_with_line([FILENAME]))
job_tracker.submit(job)
