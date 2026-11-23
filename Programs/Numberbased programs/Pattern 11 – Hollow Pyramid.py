''' Pattern 11 – Hollow Pyramid
    *
   * *
  *   *
 *     *
*********
'''
#time complexity -o(n^2),space complexity-o(n)[due to string multiplication]
def hollowpyramid(n):
  for i in range(1,n+1):
    if i ==1:
      print(' '*(n-i)+'*'*(i))
    elif i<n:
      print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
    else:
      print('*'*(2*n-i))
num=int(input("Enter the number of rows"))
hollowpyramid(num)
