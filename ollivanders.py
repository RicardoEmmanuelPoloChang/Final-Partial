counter = 0
number_wands = 0
elder= 0
hawthorn=0
dragon=0
willow=0 
sales=0
notsold=0
client = input("Is there any client? (yes/no): ")

while client == "yes":
  counter+= 1
  wand= input("Has a Wand been sold? (yes/no)")
  if wand == "yes":
    sales+= 1
    print("""
    1. Elder wand
    2. Hawthorn wand
    3. Dragon wand
    4. Willow wand
    """)
    type_of_wand = int(input("Which one has been bought?"))
    if type_of_wand == 1:
      elder += 1
    elif type_of_wand == 2:
      hawthorn += 1
    elif type_of_wand == 3:
      dragon += 1
    elif type_of_wand == 4:
      willow += 1
  elif wand == "no":
      notsold+=1 
      
  client=(input("Is there any client? (yes/no)"))

print(f"Today {counter} clients came in")
print(f"of them, {sales} bought a wand, and {notsold} didn´t")
print(f"{elder} elder wands were sold")
print(f"{hawthorn} hawthorn wands were sold")
print(f"{dragon} dragon wands were sold")
print(f"{willow} willow wands were sold")
print("What a great day for Olivanders!")
