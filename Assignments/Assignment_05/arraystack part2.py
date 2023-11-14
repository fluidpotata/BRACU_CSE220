from arrayStack import ArrayStack

s1="{(()}]"
#complete your task here
def parenthesischecker(s):
  a = ArrayStack()
  for i in range(len(s)):
    if s[i] in "(){}[]":
      if s[i]==")":
        if a.peek()!="(":
          return (f"Error at character {i+1}, '(' not opened")
        else:
          a.pop()
      elif s[i]=="}":
        if a.peek()=="{":
          a.pop()
        else:
          return ("Error at character "+str(i + 1)+", '{' not opened")
      elif s[i]=="]":
        if a.peek()!="[":
          return (f"Error at character {i + 1}, '[' not opened")
        else:
          a.pop()
      elif s[i]=="{":
        if a.peek()=="(":
          return (f"Error at character {i+1}, '(' not closed")
        else:
          a.push(s[i])
      elif s[i]=="[":
        if a.peek() == "(":
          return (f"Error at character {i + 1}, '(' not closed")
        elif a.peek()=="{":
          return ("Error at character "+str(i + 1)+", '{' not closed")
        else:
          a.push(s[i])
      else:
        a.push(s[i])
  if a.isEmpty():
    return f"This expression is correct."
  else:
    return f"Error, '{a.peek()}' wasn't closed"


print(parenthesischecker(s1))
