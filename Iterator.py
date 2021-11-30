class Iterator:
    def __init__(self, obj):
        self.obj = obj
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= (len(self.obj)):
            self.counter += 1
            return self.obj[self.counter]

        else:
            raise StopIteration

# set_of_numbers = {1, 2, 3}
# list_of_numbers = [1, 2, 3]
#
# set_numbers_iterator = Iterator(set_of_numbers)
# # list_numbers_iterator = Iterator(list_of_numbers)
#
# print(next(set_numbers_iterator))
# print(next(set_numbers_iterator))
# print(next(set_numbers_iterator))
# #
# # print(next(list_numbers_iterator))
# # print(next(list_numbers_iterator))
# # print(next(list_numbers_iterator))