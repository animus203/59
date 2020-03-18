names = ['alpha', 'bethfdaa', 'cidddfefasana']
letters = [len(n) for n in names]

longest = None
max_letter = 0

# for i, name in enumerate(names):
#     count = letters[i]
#     if count > max_letter:
#         longest = names[i]
#         max_letter = count
#
# print(longest)

for name, count in zip(names,letters):
    if count > max_letter:
        longest = name
        max_letter = count

print(longest)