try:
    statement
except:
    statement
try:
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    result=a/b
    print("result:",result)
except zerodivision error:
   print("error:division by zero is not allowed")
except value error:
  print("error:please enter valid integer")
