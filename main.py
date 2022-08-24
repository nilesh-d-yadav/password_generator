# Password Generator
import random
import time
import os

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
     
def game():
  alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
  integerss=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  
  signs=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+']
  
  print("\t\tWelcome to the Password Generator!\n\n")
  
  letters=int(input("How many letters you want? "))
  symbols=int(input("How many symbols you want? "))
  numbers=int(input("How many numbers you want? "))
  
  password_list=[]
  for letters in range(0,letters):
    password_list+=random.choice(alphabets)
  
  for symbols in range(0,symbols):
    password_list+=random.choice(signs)
  
  for numbers in range(0,numbers):
    password_list+=random.choice(integerss)
  
  
  # Either use this
  # --> shuffle changes the original list and doesn't return a new list.
              # random.shuffle(password_list)
              # print(password_list)
  # OR
  
  updated_pass=""
  for password in password_list:
    updated_pass+=random.choice(password_list)
  
  print(f"\n\nThe generated password is:-  {updated_pass}\n")
  
  
  time.sleep(3)
  consent=input("Wanna Go AGAIN? Type 'Y' or 'N':- ").upper();
  print("\n")

  if(consent=="Y"):
    time.sleep(1)
    screen_clear()
    game()
  else:
    return None

game()


