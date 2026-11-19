'''for loop is a flowcontrol statement used to iterate over a sequence and execute a block  of code
for mainly used when the number of iterations is known

mainly for loop is used in sequence data structures.
syntax:
for i in range(stop)
for i in range(start,stop) ---here step is 1 by default
for i in range(start,end,step)
for i in range(start,stop,step) --step cann be negative
'''


print("Numbers from 1 to 10")
for i in range(1,11):
  print(i)


print("Numbers from 1 to 10 even numbers")
for i in range(2,11,2):
  print(i)

print("even Numbers from 10 to 1") 
for i in range(10,0,-1):
  print(i)
