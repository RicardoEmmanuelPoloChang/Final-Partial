gryffindor_score = 0
slitheryn_score = 0
iteration=0

numberevents= int(input("Number of events in the Quidditch: "))
while iteration < int(numberevents):
  iteration+= 1
  event= str(input("Enter an event (goal/snitch/foul):"))
  team = str(input("which team scored? Gryffindor or Slytherin:"))
  if team == "Gryffindor" and event == "goal":
    gryffindor_score+=10
  elif team == "Gryffindor" and event == "snitch":
    gryffindor_score+=150
  elif team == "Gryffindor" and event == "foul":
    gryffindor_score-=30
  elif team == "Slytherin" and event == "goal":
    slitheryn_score+=10
  elif team == "Slytherin" and event == "snitch":
    slitheryn_score+=150
  elif team == "Slytherin" and event == "foul":
    slitheryn_score-=30



print(f"Gryffindor: {gryffindor_score} points")
print(f"Slytherin: {slitheryn_score} points")

gryfwins = gryffindor_score-slitheryn_score
slywins = slitheryn_score-gryffindor_score
if gryffindor_score > slitheryn_score:
  print(f"Gryffindor wins by {gryfwins} points")
elif gryffindor_score < slitheryn_score:
  print(f"Slytherin wins by  {slywins} points")
elif gryffindor_score == slitheryn_score:
  print("We have a draw!")
