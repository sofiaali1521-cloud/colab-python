print ("hello world")
print("something else")

a = 3;
print(a * 2)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
ans = a+b+c+d+e
print(ans)


a = input()
b = input()
ans = a + b
print(ans)


a = 3
b = 3
print(a+b+c)


a = 3
b = 2
print(a,b)
temp = a
a = b
b = temp
print(a,b)


for i in range(1,50):
    if(i % 2 == 0):
      print( "even is: ", i)
    else:
      print( "odd is: ", i)
      

a=0
if(a>0):
  print("positive")
elif(a<0):
  print("negative")
else:
  print("zero") 
  
  
  a = input()
if(a == "sun"):
  print("sunday")
elif(a == "mon"):
  print("monday")
elif(a == "tue"):
  print("tuesday")
elif(a == "wed"):
  print("wednesday")
elif(a == "thru"):
  print("thrusday")
elif(a == "fri"):
  print("friday")
elif(a == "sat"):
  print("saturday")
else:
  print("not a good day")
  
  
  
  n = 10
for i in range (0,n+1):
  if(i%2 == 0):
    print(i)
    
for i in range(1,11,2):
  print(i)
  
  
  
a=int(input())
while a < 10:
  print(a)
  a = a+1
  
  
  
n = input()
i = 0
j = len(n)-1
while(i < j):
  if(n[i] != n[j]):
    print("no")
    break
    i = i+1
    j = j-1
    
  else:
    print("yes")