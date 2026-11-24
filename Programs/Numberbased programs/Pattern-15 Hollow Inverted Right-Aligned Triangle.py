'''  Pattern-15 Hollow Inverted Right-Aligned Triangle.py
*****
 *  *
  * *
   **
    *
   '''

def invertedrighthollow(n):
  for i in range(1,n+1):
    if i==1:
      print('*'*n)
    elif i==n:
      print(' '*(n-i)+'*')
    else:
      print('' '*(i-1)+'*'+' '*(n-i-1)+'*')
num=int(input())
invertedrighthollow(num)
