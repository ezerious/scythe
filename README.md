# scythe
Randomize Scythe Faction/Player Board combos for base game. 
It will not allow for banned combos (Rusviet/Industrial, Crimea/Patriotic, and Rusviet or Crimea with Innovative or Militant).

Run with number of players as parameter. Will return list of faction/player mat combos.

ex. 

$ python scythe.py 4

would return
['Saxony|Engineering', 'Crimea|Agricultural', 'Nordic|Mechanical', 'Rusviet|Patriotic']

Can support up to 7 players for Invaders from Afar Expansion. Can also optionally include the Invaders factions/player mats in a game with 5 or fewer by adding an additional parameter 'y' to indicate including them.

ex. 

$ python scythe.py 6
['Saxony|Militant', 'Nordic|Industrial', 'Rusviet|Patriotic', 'Crimea|Engineering', 'Togawa|Innovative', 'Polania|Agricultural']

ex. 

$ python scythe.py 4 y
['Polania|Militant', 'Togawa|Innovative', 'Rusviet|Engineering', 'Crimea|Agricultural']
