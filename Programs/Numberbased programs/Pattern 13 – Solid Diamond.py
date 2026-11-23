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
        print(' '*


      elif i>middle:
        

      else:
        print('*'*n) 
num=int(input("Enter the number of rows"))
res=solidalmond(num)
print(res)
  
