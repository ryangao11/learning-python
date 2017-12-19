import sys
import random
def main():
	if len(sys.argv) >= 2:
		number = int(sys.argv[1])
	else:
		number = 1
	i = 1
	sum = 0
	while i <= number: 
		roll = random.randint(1,6)
		print 'Roll', i, 'is:', roll
		sum = sum + roll
		i = i + 1
	print 'Average of the rolls is: ', float(sum)/number
if __name__ == '__main__':
  main()