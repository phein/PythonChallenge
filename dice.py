from random import randint
from collections import Counter

def roll_dice(*dice,num_trials=1_000_000):
	counts = Counter()
	for roll in range(num_trials):
		counts[sum((randint(1,sides) for sides in dice))] += 1

	print('\nOUTCOME\tPROBABILITY')
	for outcome in range(len(dice), sum(dice)+1):
		print('{}\t{:0.2f}%'.format(outcome,counts[outcome]*100/num_trials))


#print(roll_dice(4,6,6))
# OUTCOME	PROBABILITY
# 3	0.69%
# 4	2.09%
# 5	4.14%
# 6	6.99%
# 7	9.70%
# 8	12.50%
# 9	13.93%
# 10	13.91%
# 11	12.49%
# 12	9.74%
# 13	6.89%
# 14	4.18%
# 15	2.07%
# 16	0.68%