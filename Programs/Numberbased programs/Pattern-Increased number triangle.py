'''
Pattern-Increased number triangle.py
1
12
123
1234
12345
'''
def increasedtriangle(n):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(j)
    print()
num=int(input("Enter the number of rows"))
increasedtriangle(num)
