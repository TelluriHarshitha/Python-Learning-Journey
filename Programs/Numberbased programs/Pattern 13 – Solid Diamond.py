'''   Pattern 13 – Solid Diamond.py
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    '''

def solidalmond(n):
  middle=(n//2)+1
  if n%2==0:
    print("Not possible to form the diamond pattern")
  else:
    for i in range(1,n+1):
      if i<middle:
        print(' '*(middle-i)+'*'*(2*i-1))
      elif i>middle:
         print(' '* (i-middle)+'*'*(2*n-2*i+1))
      else:
        print('*'*n) 
num=int(input("Enter the number of rows"))
solidalmond(num)

  
