class Sort: 
    def __init__(self, array):
        self.array = array
    

    def insertionSort(self):
        for step in range(1, len(self.array)):
            key = self.array[step]
            j = step - 1
            
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j = j - 1
            
            self.array[j + 1] = key
        return self.array
    
    def _partition(self, low, high):
        i = (low-1)         # index of smaller element
        pivot = self.array[high]     # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if self.array[j] <= pivot:

                # increment index of smaller element
                i = i+1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        
        # swap arr[i+1] and arr[high] (or pivot)c
        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        return (i+1)

    def quickSort(self, low, high):
        if len(self.array) == 1:
            return self.array
        if low < high:

            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self._partition(low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(low, pi-1)
            self.quickSort(pi+1, high)
        return self.array 
    
    def mergeSort(self):
        self._mergeSort(self.array)
        return self.array


    # mergesort
    def _mergeSort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            L = array[:mid]
            R = array[mid:]

            self._mergeSort(L)
            self._mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1
        


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    s = Sort(arr)
    print(s.insertionSort())
    print(s.quickSort(0, len(arr) - 1))
    print(s.mergeSort(arr))