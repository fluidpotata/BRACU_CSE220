# Test 07: Splitting an Array
def split_array(source):

    for i in range(1,len(source)):
        j = len(source)-1
        s1 = 0
        s2 = 0
        for k in range(i):
          s1+=source[k]
        for x in range(j,i-1,-1):
          s2+= source[x]
        if s1 == s2:
          return True
        s1,s2 = 0,0