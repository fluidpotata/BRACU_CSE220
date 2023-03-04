# Test 01: Shift Left k cell
def shift_left(source, k):
  
  for i in range(len(source)):
    if i<k:
        source[i] = source[i+k]

    else:
        source[i] = 0

  return source



