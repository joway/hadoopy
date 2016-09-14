import datetime

from tests.test_direct import test_direct
from tests.test_mapper import TestMapper
from tests.test_reducer import TestReducer
from tracker.job import Job
from tracker.jobtracker import JobTracker
from utils.hdfs import split_with_line

BEGIN = datetime.datetime.now()
FILENAME = 'words.list'
# FILENAME = 'words.txt'
with open(FILENAME, 'r') as file:
    words_list = file.read()

job_tracker = JobTracker()
job = Job([FILENAME], mapper=TestMapper(), reducer=TestReducer(), input_splits=split_with_line([FILENAME]))
job_tracker.submit(job)

END = datetime.datetime.now()

print((END - BEGIN).total_seconds())

BEGIN = datetime.datetime.now()
result = test_direct(filename=FILENAME)
print(result)
END = datetime.datetime.now()
print((END - BEGIN).total_seconds())
