# Mini project — number guessing game
# Random number 1–100. Loop until correct guess. Count attempts. Print hints.




print("Welcome To Number Gussing Game")
print("Guess The number betweeen 1 - 100")

randomNum = 43
attempt = 0
while True :
  attempt += 1
  guss = int(input("\nguess the Number  : "))
  if randomNum < guss :
    print("gussing Number is Too High")

  elif randomNum > guss :
        print("gussing Number is Too Low")
  else :
   print(f"your are Correct , You Take {attempt} attempt to finish ")
