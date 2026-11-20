def rightangledec(n):
  for i in range(0,n):
    print(' '*i,'*'*(n-i))
num=int(input("enter number of rows"))
rightangledec(num)

#by using while loop
rows=int(input("Enter number of rows"))
row_no=1
while row_no<=rows:
  spaces=' '*(row_no-1)
  stars='*'*(rows-row_no+1)
  print(spaces+stars)
  row_no=row_no+1
