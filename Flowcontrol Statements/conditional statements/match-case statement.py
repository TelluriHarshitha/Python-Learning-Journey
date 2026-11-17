'''match-case is a decision making statement in python is used forr menu driven application or to deal with predesigned conditions
 It is used to compare a value against multiple patterns and execute the corresponding block when a pattern matches.
syntax: 

match(userinput):
case 1:
     if userinput enters 1 it performs case 1 operations
case 2:
  if userinput enters 2 it performs case 2 operations
case 3:
  if userinput enters 3 it performs case 3 operations
default:
  it is like else block '''

print("-----onine shopping appilicaton")
print("1.Login")
print("2.Register")
print("3.View products")
print("4.exit")
choice=int(input("Select the option to perform"))
match choice:
   case 1:
     user=input("Do you have an account yes/no")
     res=user.upper()
     if res=="YES":
       pwd=input("Please enter the password")
       if pwd=="harshi":
         print("Login success")
       else:
         print("invalid password")
     else:
       print("Please register first")
   case 2:
     pwd=input("Please create a password")
   case 3:
    print("View all products")
   case 4:
     print("You exited successfully")
   case '_':
      print("Please select option between 1 and 4")
   
