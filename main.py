#Write a program that takes a number and tells the user if the number is greater than 10, less than 10, or equal to 10. Don't forget to convert the string into an integer. 

user_num = int(input("enter enter a number: "))

if user_num > 10:
  print("Your number is greater than 10!")
elif user_num < 10:
  print("Your number is less than 10!")
else:
  print("Your numbers equal to 10!")