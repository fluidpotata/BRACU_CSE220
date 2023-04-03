class KeyIndex:
    def __init__(self,a):
        max = a[0]
        min = a[0]
        for i in a:
            if i>max:
                max = i
            if i<min:
                min = i
        if min<0:
            self.add = -1*min
        else:
            self.add = 0
        self.k = [0]*(self.add+max+1)
        for i in a:
            self.k[i+self.add] += 1

    def search(self,val):
        if len(self.k)+1<val or val<(-1*self.add) or self.k[val+self.add]==0 :
            return False
        return True

    def sort(self):
        leng = 0
        for i in self.k:
            if i!=0:
                for m in range(i):
                    leng+=1
        z = [0]*(leng)
        j = 0
        for i in range(len(self.k)):
            if self.k[i]!=0:
                for l in range(self.k[i]):
                    z[j]=i-self.add
                    j+=1
        return z



a=[9,5,3,-3,-2,-3,0,9]
p = KeyIndex(a)
print(p.search(-3))
print(p.search(9))
print(p.search(-99))
print(p.sort())
