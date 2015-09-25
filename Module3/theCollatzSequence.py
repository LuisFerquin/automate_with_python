# The Collatz Sequence

def collatz(number):
	value= number
	if number % 2 == 0:
		value = number // 2
		print(str(number // 2))
	else:
		value = 3 * number + 1
		print(str(value))
	return value

try:
	userNumber = int(input('Enter a number: '))
	while userNumber != 1:
		if userNumber == 0:
			print('The number cannot be zero')
			break
		userNumber= collatz(userNumber)
except ValueError:
	print('Make sure a number is entered')


