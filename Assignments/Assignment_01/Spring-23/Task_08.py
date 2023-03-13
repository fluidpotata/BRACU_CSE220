# Test 08: Max Bunch Count
def max_bunch(a):

  prev = a[0]
  max = 0
  current = 1
  for i in range(1,len(a)):
    if prev == a[i]:
      current += 1
      if max<current:
        max = current
    else:
      current = 1;
    prev = a[i]
  return max