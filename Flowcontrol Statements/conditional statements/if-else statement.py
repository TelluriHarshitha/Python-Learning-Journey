'''if-else statement: these are the decision making statements that allows program to execute in different blocks of code based on the condition.

Syntax:
if condition is true:
    execute true block of code
else:
    execute the false block of code

example:
if the payment done ,your order is confirmed
if not payment failed try again'''

payment_status=input("Enter your payment status sucess/failed/pending")
res=payment_status.upper()
if res=="SUCCESS":
  print("Your payment is successfully done")
  print("Your order is confirmed")
else:
  print("Your payment is pending/failed")
  print("Please try again later")


  
