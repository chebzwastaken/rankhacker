def sparseArrays(strings, queries):
    count_arr = [0] * len(queries)
    for i in range(len(queries)):
        if queries[i] in strings:
            count_arr[i] += strings.count(queries[i])
    return count_arr

def osparseArrays(strings, queries):
    return [strings.count(q) for q in queries]
strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']
print(osparseArrays(strings, queries))

sorted()