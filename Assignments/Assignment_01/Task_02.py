# Test 02: Rotate Left k cell
def rotate_left(source, k):
  # TO DO
  # Hint, You can write a function for left rotate once and then use it
  length = len(source)

  for j in range(k):   
    tmp = source[0]
    for i in range(len(source)-1):
        source[i] = source[i+1]

    source[len(source)-1] = tmp

  return source
