print('Counting with awaiting')
def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -= 1

for x in countdown(5):
    print(x)
print('\n')

print('Union lists')
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))
print('\n')

print('Each member length')
print('Len ', list(map(len, ['abc', 'de', 'fghi'])))
print('\n')

print('Sum the union of list(zip([1, 2, 3], [4, 5, 6]))', list(zip([1, 2, 3], [4, 5, 6])))
print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))
print('\n')
