def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'for you and for me i'
result = index_words(address)
print(result)


def index_words_iter(text):
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1
it = index_words_iter(address)
print(list(it))
print(list(it))
