'''Nested if statements in python is used to check the condition inside a condition 
it means writing if inside another if statement

syntax:
if cond1 is true:
   it comes inside if and looking for another condition to check
   if cond11 is true:
       executes this block of code
    else:
        executes this block of code
else:
   if the main condition false executes the else block 

   example:check the customer has the account if yes,check the password 
   if not create an account'''

account=input("Do you have an account yes/no")
res=account.upper()
if res == "YES":
  password=input("Enter your password")
  if password=="harshi":
    print("You login succesfully")
  else:
    print("Invalid password")
else:
  print("Please create an account")
