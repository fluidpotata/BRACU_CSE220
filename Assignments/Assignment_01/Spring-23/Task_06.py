# Test 06: Remove all occurrences of a particular element from an array
from Task_05 import remove

def remove_all(source, element):

  i = 0

  while(i<len(source)):
    if source[i] == element:
      remove(source,i)
    else:
      i += 1


  return source