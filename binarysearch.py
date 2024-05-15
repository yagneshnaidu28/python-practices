#binary search program
stack5=[4,5,6,1,2]
stack5.sort()  #[1,2,4,5,6]
high=len(stack5)-1
low=0
x=4

def binarysearch(stack5,high,low,x):
  mid=(high+low)//2
  if stack5[mid]==x:
    return mid
  elif(stack5[mid]>x):
    return binarysearch(stack5,low,mid-1,x)
  elif(stack5[mid]<x):
    return binarysearch(stack5,mid+1,high,x)

r=binarysearch(stack5,high,low,x)
print("element is found at:",str(r))