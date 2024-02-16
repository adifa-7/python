import random
number = random.randint(1, 10)
count = 0
while count < 3:
        guess = int(input())

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        elif guess == number:
            print('congratulations')
	    break;
	else:
	    print('sorry')
	count+1

