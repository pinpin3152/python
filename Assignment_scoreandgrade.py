import random

def grade(score):
	if score >= 60 and score < 70:
		return "D"
	elif score >= 70 and score < 80:
		return "C"
	elif score >= 80 and score < 90:
		return "B"
	else:
		return "A"

print "Scores and Grades"

for X in range (0,10):
	X = random.randint(60,100)
	print "Score: " + str(X) + "; Your grade is " + grade(X)

print "End of the program. Bye!"

#Hey Gary, I would consider using input() or raw_input() to get user input for this assignment.  I like your use of random numbers
#but we need to get the user involved.  See how you can incorporate input() or raw_input() into this assignment.
'''
#answer sheet solution
from random import randint

print "Scores and Grades"
for count in range(0, 10):
	score = randint(60, 100)

	if(score <= 70):
		grade = "D"
	elif(score <= 80):
		grade = "C"
	elif(score <= 90):
		grade = "B"
	else:
		grade = "A"

	print "Score: %d; Your grade is %s" %(score, grade)

print "End of program. Bye!"
'''
