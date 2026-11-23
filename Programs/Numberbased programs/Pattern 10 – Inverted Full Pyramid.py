'''
Pattern 13 – Inverted Full Pyramid
*********
 *******
  *****
   ***
    *
'''

def invertedfullpyramid(n):
  for i in range(1,n+1):
    for sp in range(i-1):
      print(' ',end='')
    for st in range(2*n-2*i+1):
      print('*',end='')
    print()
num=int(input("Enter the number of rows"))
invertedfullpyramid(num)

#by using thw while loop
rows=int(input("Enter number of rows"))
row_no=1
while row_no<=rows:
  stars=2*rows-2*row_no+1
  spaces=row_no-1
  print(' '*spaces+'*'*stars)
  row_no=row_no+1
  
