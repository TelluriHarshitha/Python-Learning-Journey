''' Pattern 08 – Right-Aligned Inverted Triangle
*****
 ****
  ***
   **
    *
'''
#Time complexity for both code is o(n^2),space complexity is o(n)
def rightalignedinverted(n):
  for i in range(n):
    print(' '*i,'*'*(n-i))
num=int(input("Enter the number of rows:"))
rightalignedinverted(num)

#By using while loop
rows=int(input("Enter number of rows:"))
row_no=1
while row_no<=rows:
  print(' '*(row_no-1),'*'*(rows-row_no+1))
  row_no=row_no+1
#we can reducde the space complexity o(n) to o(1).
def rightalignedinverted(n):
  for i in range(n):
    for s in range(i):
      print(' ',end='')
    for  st in range(n-i):
      print('*',end='')
    print()
num=int(input("Enter number of rows"))
rightalignedinverted(num)
