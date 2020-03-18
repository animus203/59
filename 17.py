def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


# it = read_visits('E:\\Python\\pyer\\59\\data\\17.txt')
# percentage = normalize(it)                                  #再次迭代无法生成新数据
# print(percentage)


class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits('E:\\Python\\pyer\\59\\data\\17.txt')
percentages = normalize(visits)
print(percentages)



