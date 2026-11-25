'''
Pattern 02 – Repeated Number Triangle.
1
22
333
4444
55555
'''
def repeatednum(n):
  for i  in range(1,n+1):
    for j in range(1,i+1):
      print(i,end='')
    print()
num=int(input("Enter number of rows"))
repeatednum(num)
