'''
Pattern 14 – Hollow Diamond.py
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
    '''
def HollowDiamond(n):
  middle=(n//2)+1
  if n>3 and n%2 !=0:
    for i in range(1,n+1):
      if i<=middle:
        print(' '* +'*'+' '*()+'*')
      else:
        print(' '*()+)
    print()
        
      



num=int(input())
HollowDiamond(num)
