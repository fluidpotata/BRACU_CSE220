# Test 04: Rotate Right k cell
def rotate_right(source, k):

  # Hint, You can write a function for right rotate once and then use it
  
  for i in range(k):
    j = len(source)-1
    tmp = source[j]
    while j>0:
      source[j] = source[j-1]
      j -= 1
    source[0] = tmp

  return source
