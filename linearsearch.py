#this is program for linear search
stack1=[6,5,1,2]
x=2

def linearsearch(stack1,x):
  for i in stack1:
    if i==x:
      print(x,"is found at index",stack1[i])

linearsearch(stack1,x)