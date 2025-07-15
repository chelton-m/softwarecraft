string_as_input = input('Enter string: ')

def count_characters(string):
    dct = {}
    for char in string:
        dct[char] = dct.get(char, 0) + 1
    return dct

a = count_characters(string_as_input)
print(a)


'''
input = 'Hello Hehnry'
dct = {'h': 2, 'e': 2, 'l': 2, 'o':1, 'n':1, 'y':1, 'r':1}
'''