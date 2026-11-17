'''if-elif statement in python is used to make  a decision whhen we have the multiple condition to check.

syntax:
if condition1 :
    execute the if block if cond1 is true
elif cond2 is true:
    execute this elif block when the cond2 is true
elif cond3 is true:
    execute this elif block when the cond3 is true
else:
   execute this else block when none of above block execute/cond fails 

imagine an shopping application that gives the discount based on the order amount.'''


amount=int(input("Enter the amount:"))
discount=0
if amount>=5000:
  discount=amount*0.2
  amount=amount-discount
  print("The final amount to pay is",amount)
  print("you got",discount,"discount")
elif amount>=3000:
  discount=amount*0.1
  amount=amount-discount
  print("The final amount to pay is",amount)
  print("You got",discount,"discount")
elif amount>=1000:
  discount=amount*0.05
  amount=amount-discount
  print("The final amount to pay is",amount)
  print("You got",discount,"discount")
else:
  print("No discount applicable")
  
 




