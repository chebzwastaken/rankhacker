
class Solution: 
    def days_until_no_animal_dies(p):
        largest = 0
        counter = 0
        i = 1
        while i < len(p):
            print(p)
            for x in range(0, len(p)):
                if(p[x] > largest):
                    largest = p[x]

            if p[i] > p[i - 1]:
                print(f'{p[i]} > {p[i - 1]}, {counter}, {len(p)}, {largest}')
                if p[i] == largest:
                    counter += 1
                    largest = 0
                del(p[i])
                i -= 1
            else:
                i += 1
        print(counter)
        
        
            


        
            

Solution.days_until_no_animal_dies([ 6, 5, 8, 4, 7, 10, 9 ])
Solution.days_until_no_animal_dies([ 4, 3, 7, 5, 6, 4, 2 ])