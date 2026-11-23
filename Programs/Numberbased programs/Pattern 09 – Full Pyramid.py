''' Pattern 09 – Full Pyramid
    *
   ***
  *****
 *******
*********
'''
#by building the code like this it takes space complexity -o(1),time complexity -o(n)
def fullpyramid(n):
  for i in range(1,n+1):
    for sp in range(n-i):
      print(' ',end='')
    for st in range(2*i-1):
      print('*',end='')
    print()
num=int(input("Enter number of rows"))
fullpyramid(num)

#by using while loop
rows=int(input("Enter the number of rows"))
row_no=1
while row_no<=rows:
  print(' '*(rows-row_no),'*'*(2*row_no-1))
  row_no=row_no+1
