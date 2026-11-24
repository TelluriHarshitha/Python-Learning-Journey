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
  if n>3 and n%2 !=0:
     #upperpartofthepattern
     for i in range(1,n+1):
        if i==1:
           print(' '*(n-i) +'*')
        else:
           print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
     #lowerpart
     for i in range(1,n):
        if i==n-1:
           print(" "*(n-1)+"*")
        else:
           print(" "*i+"*"+" "*(2*n-2*i-3)+"*")
num=int(input())
HollowDiamond(num)
