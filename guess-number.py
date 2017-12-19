import sys
import random
def main():
	if len(sys.argv) >= 2:
		randomNum = random.randint(1, int(sys.argv[1]))
	else:
		randomNum = random.randint(1,1000)
	counter = 0
	while True: 
		guess = int(input('Enter your guess: '))
		if guess == randomNum:
			print 'Good job!'
			break;
		elif guess < randomNum:
			print 'Too Low'
		else:
			print 'Too High'
		counter = counter + 1
	print 'Number of guess taken: ', counter
if __name__ == '__main__':
  main()