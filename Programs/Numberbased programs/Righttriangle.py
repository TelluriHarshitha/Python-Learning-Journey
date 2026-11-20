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

#by using the while loop
rows=int(input("Enter number of rows"))
row_no=1
while row_no<=rows:
  print(''*(rows-row_no),'*'*row_no) 

  row_no=row_no+1

