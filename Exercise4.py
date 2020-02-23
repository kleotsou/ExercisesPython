#create a function
def Function_ASCII(s):
  y = [ord(c) for c in s]
  print(y)
  j = len(y)
  sum1 = 0
  for i in range(j):
    sum1+=y[i]
  sum2 = 0
  for i in range(sum1):
    h = sum1 % (i+1)
    if (h == 0):
      sum2+=1
  if (sum1/1==sum1) and (sum1/sum1==1) and (sum2==2):
    return ("The number", s, "is first!!!")
  else:
    return("The number", s, "is not first!!!")

#main program
print("Give a string in ascii code:")
s = input()
while (s == " "):
  print("Give a string in ascii code:")
  s = input()
Sum = Function_ASCII(s)
print(Sum)


