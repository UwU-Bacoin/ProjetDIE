a = "exercice de "
b = "concaténation "
c = "de chaînes"

print("concaténation par addition")
print(a + b + c)

print("\nconcaténation par f-string")
print(f"{a}{b}{c}")

print('\nconcaténation avec la méthode `join` de `str` et un tuple')
print(''.join((a, b, c)))

print("\nl'ancien style de concatenation")
print('%s%s%s' % (a, b, c))

print("\nméthode `format` de `str` et arguments")
print('{}{}{}'.format(a, b, c))

print("\nméthode `format` de `str` avec un tuple")
print('{1}{0}{2}'.format(b, a, c))

# Pour le fun :D
print("\nSans print")
license.__class__('Magique', type(__name__).__add__(a, b.__add__(c)))()
