import re

from core.mapper import Mapper


class TestMapper(Mapper):
    def map(self, key, value, context):
        splitter = re.compile("\\W+")
        toks = [x for x in splitter.split(value) if len(x) > 0]
        for t in toks:
            context.write(t, 1)
