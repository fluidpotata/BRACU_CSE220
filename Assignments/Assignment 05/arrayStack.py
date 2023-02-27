# Using Array
class ArrayStack:
  def __init__(self):
    self.size = 0
    self.arr = [None] * 100

  # Returns The number of items on the stack
  def stackSize(self):
    return self.size

  # Returns true if the stack is empty
  def isEmpty(self):
    if (self.size == 0):
      return True
    return False

  # Pushes the new item on the stack
  def push(self, e):
    if self.size<100:
      self.arr[self.size] = e
      self.size+=1
    else:
      print("Not enough space in array")

  # Pops the item on the top of the stack
  def pop(self):
    self.size -= 1
    self.arr[self.size] = None

  # Returns the item on the top of the stack
  def peek(self):
    return self.arr[self.size-1]

  # Print all items of the stack
  def stackPrint(self):
    for i in range(self.size):
      print(self.arr[i], end=" ")
    print()

