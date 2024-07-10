# functions
# functions to add two numbers


def add(x,y):
  return x + y


# functions to subtract two numbers
def sub(x,y):
  return x - y

# functions to multiply two numbers
def multiply(x,y):
  return x*y
         
# functions to divide two numbers
def div(x,y):
  return x/y

# showing user calc menu
print("select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
int(input("select operation"))

# Take input from the user
while True:
  choice = input(" Enter choice (1/2/3/4):")

# Check if choice is one of the four options
  if choice in('1', '2' , '3', '4'):
    try:
      num1 = float(input("enter first number: "))
      num2 = float(input("enter second number: "))
    except ValueError:
      print("Error, enter a number.")
      continue 

  if choice == '1':
    print(num1, '+' ,num2, '=',add(num1,num2))
  elif choice == '2':
    print(num1, '-' ,num2, '=',sub(num1,num2))
  elif choice == '3':
    print(num1, '*' ,num2, '=', multiply(num1, num2))
  elif choice == '4':
    if num2 == 0:
      print("Error, No zeroes allowed!")
    print(num1, '/' ,num2, '=', div(num1,num2))#Cannot Divide by 0

#Ask user If they want to continue using calculator
  next = input("next calculation? (yes/no):")
  if next == 'no':
    break
  

 