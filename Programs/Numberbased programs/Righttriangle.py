'''program:
n=4
   *
  **
 ***
****
'''
def rightpattern(n):
  for i in range(1,n+1):
    print(' '*n-i,'*'*i)
num=int(input("Enter number of rows"))
rightpattern(num)
