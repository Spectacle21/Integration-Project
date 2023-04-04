#Thomas Cramer
#This is a code to track progress when doing bench press in the gym
#In other words it's supposed to track progress and give feedback of how to have a better workout#Got help from a friend named Brandon Nguyen
#And looked up how to do the space feature using https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/
#import math
print("Hello, welcome to your FitPal" , end="!\n")
print("Lets","get started" , sep=" ")

#Before doing the exercise record what is being done
#the input is prompted for the user and asks them to input something
#when the input is put in it will verify the amount or whatever is put in
Weight = input("What is your starting weight:")
print(Weight)

Reps = input("How many reps:")
print(Reps)

Sets = input("How many sets:")
print(Sets)

print("Keep good form and technique")
#each set will in crease the weight but decrease the reps
print("Continue next few sets by adding weight, but decreasing reps for each set")

#Addition when adding weight for each set +
#using the weight as a variable that was input by the user and then added to the ten
print(int(Weight) + 10, end="lbs\n")
print(3+5)

#Subtraction -
print(int(Reps) - 1, end="reps\n")
print(9-4)

#Multiplication *
#The sets was used as a variable that the user inputted a number and then multiplied
print(int(Sets) * 2,end="sets\n")
print(2*6)

#exponent **
print(2**3)

#Division /
print(6/3)

#dividing without the remainder //
print(9//4)

#dividing with the remainder %
print(11%5)
#this is asking the person working out how they can improve on their workout
print("How did the last set go?")
print("Were the reps consistent and have good form?")
Feedback = input("What can you improve on:")
print(Feedback)
#Sprint 2
#This is to calculate the area of the plates
def calculateArea(radius):
    area = math.pi * radius ** 2
    print("Area of circle with a radius of", radius, "is",
          format(area, ".2f"))

def main():
   radius = int(input("Enter the radius: "))

startingWeight = float(input("Enter your beginning weight: "))
startingReps = float(input("Enter your starting reps: "))
print("Starting Weight: lbs", format(startingWeight, ".2f"), sep=" ")
print("Starting Reps: reps", format(startingReps, ".2f"), sep=" ")
if(startingWeight>=150):
    print("You're off to a great start!!!")
elif(startingWeight>=115):
    print("Great work you're getting there")
else:
    print("You've just begun your fitness journey, keep it up!!")
sets = input("How many sets: ")
for x in range(1):
    print(sets + " ", end=" ")
print()
x = 0
while(x<6):
    print(sets)
    x = x + 1
#This is showing That I know how to use Boolean
x=True
y=False
z=False
if(x==y):
    print("x is equal to y")
else:
    print("x and y are not equal")
if(x==y and y==z):
    print("They are all equal")
else:
    print("They are not equal")
if(x==z or y==z):
    print("They are the same")
else:
    print("None are the same")
#This is showing I know how to use the !=
#and the not function
x = 13
y = 4
z = 2
print(x!=z)
print(z!=y)
print(not(z * 2 ==y))
#Back into the idea of the project
print(input("What else can we do for your fitness journey?", end=" "))