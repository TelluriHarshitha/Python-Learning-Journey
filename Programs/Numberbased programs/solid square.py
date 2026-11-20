def solidsquarepattern(n):
  for i in range(n):
    print('*'*n)
num=int(input("Enter a number of rows"))
solidsquarepattern(num)

#by using while loop
rows=int(input("Enter number of rows"))
row_no=1
while row_no<=rows:
  print('*''*rows)
  row_no=row_no+1
