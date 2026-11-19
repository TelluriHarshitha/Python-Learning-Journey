"Nested loops
A  nested loop is a loop inside another loop.

it contains two components :
outer loop --it controls main iteration
inner loop ----executes completely for every iteration of outer loop
when to use:
nested loops are used when we have to process multipple levels inside a category.

example:
we have phones category
inside there are multiple phone model are listed to check we use outer loop after one phone models like iphone,or vivo ,realme 
inside we have multiple features like a same model with different properties in different of storage,camera,displaylike that..
to vist each same model of different mobile we use inner loop

nested for loops:
for i in range(start,stop,step):
   for j in range(start,stop,step):
        print(i,j)
        
nested while loops:(initialization,condition,increment,decrement)
i=1
while i<5:
  j=1
  while j<5:
   print(i,j)
   j=j+1
  i=i+1

  python allows diffferent types of loops to be nested inside each other,it depends on the choice.
  we can use for loop inside while loop
  or we can use while loop inside for loop it is acceptable
  
  for i in range(1,5):
    j=1
    while j<=5:
     print(i,j)
     j=j+1'''
