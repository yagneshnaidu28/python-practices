#stack program from user input
list1=[]
def push(z):
  list1.append(z)
  return list1
f=int(input("enter no.of elements to be in stack:"))
for i in range(0,f):
  x=int(input("enter any choice:(1.push 2.pop 3.display)"))
  if(x==1):
    z=int(input("enter numnberyou wanted to add to the list :"))
    print(push(z))
  elif(x==2):
    if(len(list1)>1):
      list1.pop()
      print(list1)
    else:
      print("can't delete elements from empty list")
  elif(x==3):
    if (len(list1)==0):
      print("list is empty")
    else:
      print(list1)