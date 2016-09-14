from core.reducer import Reducer


class TestReducer(Reducer):
    def reduce(self, key, values, context):
        SUM = 0
        for i in values:
            SUM += i
        context.write(key=key, value=SUM)
