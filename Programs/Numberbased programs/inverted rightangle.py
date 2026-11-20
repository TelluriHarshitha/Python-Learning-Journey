def invertedright(n):
  for i in range(n,0,-1):
    print('*'*i)
num=int(input("Enter number of rows:"))
invertedright(num)

#by using the while loop

rows=int(input("Enter number of rows"))
row_no=1
while row_no<=rows:
  print('*'*(rows-row_no+1))
  row_no=row_no+1
