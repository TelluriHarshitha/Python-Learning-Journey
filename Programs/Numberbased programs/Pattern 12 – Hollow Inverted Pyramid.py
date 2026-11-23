'''Pattern 12 – Hollow Inverted Pyramid.
*********
 *     *
  *   *
   * *
    *
    '''
def invertedhollow(n):
  for i in range(1,n+1):
    if i==1:
      print('*'*(2*n-i))
    elif i<n:
      print(' '*(i-1)+'*'+' '*(2*n-2*i-1)+'*')
    else:
      print(' '*(i-1)+'*')
num=int(input("Enter the number of rows"))
invertedhollow(num)
