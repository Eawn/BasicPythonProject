print("Welcome to my quiz world")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Okay, let's play.")

answer = input("what does cpu stands for? ")
if answer == "central proccessing unit":
    print("Correct!")
else:
    print("Incorrect!")
