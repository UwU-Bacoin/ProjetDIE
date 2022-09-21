# Forme Basique:

for i in range(3, 26):
    if i % 2:
        print(i, "impair")
    else:
        print(i, "pair")


# Forme Sans branches:

# for i in range(3, 26):
#     print(i, "im" * (i % 2) + "pair")


# Forme optimisé (un seul print + str.join):

# print('\n'.join(f"{i} {'im' * (i % 2)}pair" for i in range(3, 26)))
