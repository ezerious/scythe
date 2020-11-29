'''
Randomly selects factions/economy boards for N players in Scythe. 
Second optional parameter allows to use Invaders Factions and Player Mats even if fewer than 6 players are playing.
'''
import sys
import random

def main():
	if len(sys.argv) == 1:
		print("Invalid input");
		return;
	N = int(sys.argv[1]);
	if len(sys.argv) > 2:
	# If second argument set to y/Y expansion factions/players will be used
		if 'y' == str(sys.argv[2]).lower():
			N = 7
	if N > 7 or N < 1:
		print("Invalid input");
		return;
	players = get_combos(N)
	count = int(sys.argv[1]);
	print(players[:count])
	

def get_combos(n):
	#randomly generates n pairings of factions/player mats. Recalls player mats if any combo is invalid
	factions = get_faction_mats(n);
	playerMats = get_player_mats(n)

	while True:
		combos = []
		for i in range(n):
			val = factions[i] +'|'+playerMats[i];
			combos.append(val);
		if bad_combos(combos):
			playerMats = get_player_mats(n);
		else:
			return combos;
	return []

def get_player_mats(n):
	if n <= 5:
		playerMats = ['Agricultural', 'Engineering', 'Industrial', 'Mechanical', 'Patriotic'];
	else:
		playerMats = ['Agricultural', 'Engineering', 'Industrial', 'Mechanical', 'Patriotic', 'Innovative', 'Militant'];

	playerNums = list(range(len(playerMats)));
	random.shuffle(playerNums);
	playerList = []
	for i in range(n):
		playerList.append(playerMats[playerNums[i]])
	return playerList
	
def get_faction_mats(n):
	#randomly generates n factions 
	if n <= 5:
		factions = ['Polania', 'Nordic', 'Rusviet', 'Saxony', 'Crimea'];
	else:
		factions = ['Polania', 'Nordic', 'Rusviet', 'Saxony', 'Crimea', 'Albion', 'Togawa'];
	factionNums = list(range(len(factions)));
	random.shuffle(factionNums);
	factionList = []
	for i in range(n):
		factionList.append(factions[factionNums[i]])
	return factionList

def bad_combos(combos):
	# checks for any bad combos. Returns true if any found
	for val in combos:
		if val == 'Rusviet|Industrial' or val == 'Crimea|Patriotic' or val == 'Crimea|Innovative' or val == 'Crimea|Militant' or val == 'Rusviet|Innovative' or val == 'Rusviet|Militant':
			return True;
	return False;


if __name__ == "__main__":
    main()