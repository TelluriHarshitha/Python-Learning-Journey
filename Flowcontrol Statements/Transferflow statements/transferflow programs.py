def range_numbers(n):
  for i in range(0,n+1):
    if i==10:
      continue
    if i==15:
      break
  return i

num=int(input("enter a number"))
res=range_numbers(num)
print(res)
