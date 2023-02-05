def shift_left(source, k):
  # TO DO
  # Hint, You can write a function for left shift once and then use it
  for i in range(len(source)):
    if i<k:
        source[i] = source[i+k]

    else:
        source[i] = 0

  return source
