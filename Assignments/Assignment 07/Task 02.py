class hashTable:
    def __init__(self,arr):
        self.table = [0]*9
        for i in arr:
            j = self.hashFunction(i)
            if self.table[j] == 0:
                self.table[j] = i
            else:
                for q in range(9):
                    if self.table[(j+q)%9] == 0:
                        self.table[(j + q) % 9] = i
                        break

    def hashFunction(self,string):
        consonant = 0
        digits = 0
        for i in string:
            if i in "0123456789":
                digits += int(i)
            elif i.upper() not in "AEIOU":
                consonant += 1
        func = (consonant * 24 + digits) % 9
        return func

q = ["ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A31","ST1E89B8A31"]
q = hashTable(q)
print(q.table)
