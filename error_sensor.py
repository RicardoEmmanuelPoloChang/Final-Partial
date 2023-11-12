
iteration= 0
wrong=0
right=0
number = int(input("How many readings do you have? "))

while iteration < int(number):
  iteration+= 1
  temp= float(input(f"Insert temperature {iteration}:"))
  if temp < 10 or temp > 40:
    wrong+= 1 
  else:
    right+= 1

fail = (wrong*100)/number 
gud= (right*100)/number

print(f"Our sensor went wrong {wrong} times")
print(f"The sensor error rate is {fail}%, and the succes rate is {gud}%")
