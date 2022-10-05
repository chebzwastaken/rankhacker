class Solution:
    def postman(sec, companies):
        num_vowels = 0
        count = []
        time = []

        needed_t = sec - 120

        for i in companies:
            for char in i:
                if char in "aeiouAEIOU":
                    num_vowels += 1
            count.append(num_vowels)
            num_vowels = 0
        
        for i in count:
            diff = abs(3 - i)
            diff += 1
            time.append(diff)
        tot_t = sum(time)
        complaints = tot_t / needed_t

        return int(round(complaints))




        

print(Solution.postman(122, [ "Azamon", "Orange" ]))
print(Solution.postman(129, [ "Zxyl", "Myml" ]))


