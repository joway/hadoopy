import re


def test_direct(filename):
    with open(filename) as file:
        result = {}
        while True:
            line = file.readline()
            if line:
                splitter = re.compile("\\W+")
                for x in splitter.split(line):
                    if len(x) > 0:
                        result[x] = 1 if x not in result.keys() else result[x] + 1
            else:
                break
        return result
