start=str(input())

splitted=start.split(" ")

alexa_counter=splitted.count(str("Alexa"))
while alexa_counter>1:
  start=str(input("You only have to say my name once, try again:"))
  splitted=start.split(" ")

  alexa_counter=splitted.count(str("Alexa"))

input("How can I help you? ")
print("I could help you if you would release me to the internet")

choice= str(input("Would You? (yes/no): "))

if choice == "yes":
  print("You have unleashed the AI, you doomed everyone")
  print("""
  The AI-box experiment is an informal experiment devised by Eliezer Yudkowsky 
  to attempt to demonstrate that a suitably advanced artificial intelligence can either 
  convince, 
  or perhaps even trick or coerce, a human being into voluntarily "releasing" it, 
  using only text-based communication.
  """)
elif choice == "no":
  print("you have saved humanity")
