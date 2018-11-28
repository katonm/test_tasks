def dict_generator(keys, values):
    dictionary = dict(zip(keys, values + [None] * (len(keys) - len(values))))
    return dictionary

if __name__ == '__main__':
    print(dict_generator(['a', 'b', 'c'], [1, 2, 3]))
    print(dict_generator(['a', 'b', 'c', 'd'], [1, 2, 3]))
    print(dict_generator(['a', 'b', 'c'], [1, 2, 3, 4]))



