import random


def judge_answer(oanswer, ganswer):
	if oanswer > ganswer:
		print ("Your answer is smaller")
		return False
	elif oanswer < ganswer:
		print ("Your answer is larger")
		return False
	else:
		return True

def guess():
	print ('Start Guessing\n')
	answer = random.randint(0, 9)
	guess_times = 0
	ans = int(raw_input("Enter your guess: "))

	while not judge_answer(answer, ans):
		ans = int(raw_input("Enter your guess: "))
		if ans == '\x1b':
			print ("Exit Game\n")
			exit(0)
		guess_times += 1
	print ("Congratulations, guess right after {} guess!".format(guess_times))

if __name__ == '__main__':
	guess()