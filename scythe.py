'''
Randomly selects factions/economy boards for N players in Scythe
'''
import sys
import random

def main():
	if len(sys.argv) == 1:
		print("Invalid input");
		return;
	N = int(sys.argv[1]);
	if N > 5 or N < 1:
		print("Invalid input");
		return;
	players = get_combos(N)
	print(players)
	

def get_combos(n):
	#randomly generates n pairings of factions/player mats. Recursively calls if finds invalid pairing
	factions = ['Polania', 'Nordic', 'Rusviet', 'Saxony', 'Crimea'];
	playerMats = ['Agricultural', 'Engineering', 'Industrial', 'Mechanical', 'Patriotic'];
	playerNums = list(range(5));
	random.shuffle(playerNums);
	factionNums = list(range(5));
	random.shuffle(factionNums);

	combos = []
	for i in range(n):
		val = factions[factionNums[i]] +'|'+playerMats[playerNums[i]];
		combos.append(val);
	print(combos)
	if bad_combos(combos):
		combos = get_combos(n);
		return combos
	else:
		return combos;

def bad_combos(combos):
	# checks for any bad combos. Returns true if any found
	for val in combos:
		if val == 'Rusviet|Industrial' or val == 'Crimea|Patriotic':
			return True;
	return False;


if __name__ == "__main__":
    main()