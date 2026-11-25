'''
Pattern 03 – Decreasing Number Triangle.
12345
1234
123
12
1
'''
def decreasingnumber(n):
  for i in range(1,n+1):
    for j in range(1,n-i+1):
      print(j,end='')
    print()
num=int(input("Enter number of rows"))
decreasingnumber(num)
