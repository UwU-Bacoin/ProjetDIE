EXT = ' extension de chaîne '
my_strings = [
    "je ne",
    "sais",
    "pas",
    "quoi",
    "mettre..."
]

for i in range(5):
    my_strings[i] += EXT

for i in range(5):
    print(my_strings[i])


# print('\n'.join(my_strings := [s + EXT for s in my_strings]))
