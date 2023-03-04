# Test 03: Shift Right k cell
def shift_right(source, k):
 
  # Hint, You can write a function for right shift once and then use it
  j = len(source)-1
  while j>=0:
      if j>=k:
        source[j] = source[j-k]
      else:
        source[j] = 0
      j -= 1

  return source


