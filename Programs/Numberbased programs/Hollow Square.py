''' program:n=4
****
*  *
*  *
**** '''
def hollowsquare(n):
  for r in range(n):
    for c in range(n):    
      if r==0 or r==(n-1):
        print('*'*n)
      elif c==0 or c==(n-1):
        print('*'*n)
      else:
        print(' ',end='')
      print()
num=int(input("Enter a number of rows"))
hollowsquare(num)
