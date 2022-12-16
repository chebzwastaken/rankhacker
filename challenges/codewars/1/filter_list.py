def filter_list(l):
    return [(l[x]) for x in range(len(l)) if not isinstance(l[x], str)]

print(filter_list([1, 2, 'a', 'b']))