# queue program to take user input

list2=[]
def enque(z):
  list2.append(z)
  return list2
def deque():
  list2.remove(list2[0])
  return list2
f=int(input("enter no.of elements to be in queue:"))

for i in range(0,f):
  x=int(input("enter any choice:(1.push 2.pop 3.display)"))
  if(x==1):
    z=int(input("enter numnberyou wanted to add to the queue :"))
    print(enque(z))
  elif(x==2):
    print(deque())
  elif(x==3):
    print(list2)


