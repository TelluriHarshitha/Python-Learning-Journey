#if statement---it is one of the conditional statements that is used to execute  only when the condition is True.
#if the condition is false,python skips the if block of code and executes the outside of if block statements.

'''syntax:
if (condition is true):
  Execute the code'''

'''program:
a shopping applications needs to display the message when the price is greater than the 1500'''

price=int(input("Enter the price"))
if price>=1500:
  print("You reach the highest price")
  print("You are the highest customer")
