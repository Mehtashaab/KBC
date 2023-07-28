#Kaun Banega Crorepati
def kbc():
  print("Welcome, In the KBC world\n ")


kbc()
name = input("Enter Your Name here :  ")
print(name, "#Lets start the Game!\n")
print("Your First Question is on your computer screen!\n")
questions = [
  "1. Who is the father of Computers?\n", "A. James Gosling\n",
  "B. Charles Babbage\n", "C. Dennis Ritchie\n", "D. Bjarne Stroustrup\n"
]
print(questions[0])
print(questions[1])
print(questions[2])
print(questions[3])
print(questions[4])

answer = (input("Enter The correct answer number:\n ", ))
if (answer == "B"):
  print(
    "wow, Your answer is correct and you won 1000 rs.  And Next Question on Your Screen.\n"
  )

else:
  print("!!!Wrong Answer!!!\n")

print("Second question on your computer screen .\n")
questions2 = [
  "2. What is the full form of CPU?\n", "A. Computer Processing Unit\n",
  "B. Computer Principle Unit\n", "C. Central Processing Unit\n",
  "D. Control Processing Unit"
]
print(questions2[0])
print(questions2[1])
print(questions2[2])
print(questions2[3])
print(questions2[4])

answer = (input("Enter The correct answer number: ", ))
if (answer == "C"):
  print(
    "wow, Your answer is correct and you won 10000 rs.  And Next Question on Your Screen."
  )
else:
  print("Wrong Answer & GameOver")

print(
  "Thanks 😊 for participating in this game, i hope you enjoyed, Thank You 💕")
