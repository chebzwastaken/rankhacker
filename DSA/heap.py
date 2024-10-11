import heapq
class Heap:
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return (item for _, item in self._data)

    def __repr__(self):
        return "Heap({!r})".format(list(self))

    
# Path: DSA/heap.py

if __name__ == "__main__":
    h = Heap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0], key=lambda x: -x)
    print(h)
    h.push(10)

    while h:
        print(h.pop(), end=' ')