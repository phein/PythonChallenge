import time
import random

def waiting_game():
	target = random.randint(2,5)
	print("\nYou have {} seconds for the waiting game".format(target))
	
	input("Press Enter to begin\n")
	start = time.perf_counter()
	input()

	elapsed = time.perf_counter() - start

	if elapsed > (target - 0.03) and elapsed < (target + 0.03) :
		print("Good job! Perfect Timing!")
	elif elapsed < target:
		print("Too fast. You hit {0:.3f} seconds ahead".format(target - elapsed))
	else:
		print("Too slow. You hit {0:.3f} seconds after".format(elapsed - target))
