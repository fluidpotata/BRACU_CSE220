import math

def mean_value(source):
  sum = 0
  for i in range(len(source)):
    sum+=source[i]
  avg = sum/len(source)

  return avg

def standard_deviation(source):
  sd_sum = 0
  mean = mean_value(source)
  for i in range(len(source)):
    sd_sum += (source[i] - mean)**2
  sd = math.sqrt(sd_sum/(len(source)-1))
  return float("{0:.2f}".format(sd))

def sd_mean_away(source):
  count = 0
  max = mean_value(source) + standard_deviation(source)*1.5
  min = mean_value(source) - standard_deviation(source)*1.5
  for i in range(len(source)):
    if source[i]>max or source[i]<min:
      count += 1
  j = 0
  newArray = [0]*count
  for i in range(len(source)):
    if source[i]>max or source[i]<min:
      newArray[j] = source[i]
      j += 1

  if len(newArray)!=0:
    return newArray
  return None

source = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
print(mean_value(source))
print(standard_deviation(source))
print(sd_mean_away(source))