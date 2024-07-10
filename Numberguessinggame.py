
print("Guess A Number Between 1-10")

import random

number = random.randint(1,10)

while True:
  guess = int(input("Guess A Number: "))
  
  if guess > number and guess <= 10:
      print("Incorrect, Guess Lower")
  
  elif guess < number and guess >= 1:
     print("Incorrect, Guess Higher")
  
  if guess > 10 or guess < 1:
      print("Incorrect, not on range")
  
  if guess == number:
      print("Correct")
      response = input("Try Again?")
      if response == "n":
        break
      
      
    
      
  
    
      
  

  
    