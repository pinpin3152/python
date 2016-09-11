# Part 1 Odd number from 1 to 1000
odd_number = 1
for odd_number in range (0, 1001):
	if odd_number % 2 == 1:
		print(odd_number)
raw_input("\n\nPress the enter key to exit.")

# Part 2 Print all multiples of 5 from 5 to 1,000,000
number = 5
for number in range (5, 1000001):
	if number % 5 == 0:
		print(number)

