# class FrequencyList(list):
#     def __init__(self,members):
#         super().__init__(members)
#
#     def frequency(self):
#         counts = {}
#         for item in self:
#             counts.setdefault(item, 0)
#             counts[item] += 1
#         return counts
#
#
# foo = FrequencyList(['a', 'b', 'c', 'a', 'b', 'd'])
# print('len is ', len(foo))
# foo.pop()
# print('After pop ', repr(foo))
# print('Frequency: ', foo.frequency())


class BinaryNode(object):
    def __init__(self,value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


class IndexableNode(BinaryNode):
    def _search(self, count, index):
