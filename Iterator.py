class Iterator:
    def __init__(self, obj):
        self.obj = obj
        self.index = -1

    # def __iter__(self):
    #     return self

    def __next__(self):
        try:
            self.index = self.index + 1
            return self.obj[self.index]
        except IndexError:
            raise StopIteration
