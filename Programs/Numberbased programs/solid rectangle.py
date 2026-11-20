'''Program
******
******
******
******'''
def solid_rectangle(rows,col):
  for r in range(rows):
    for c in range(col):
      print('*',end='')
    print()
rows=int(input("Enter number of rows"))
col=int(input("Enter number of col"))
solid_rectangle(rows,col)
