## Game Description
- I present to you a dynamic and interesting war game, where the troops, kings and 
  barbarians attack a base with various buildings and a strong defense system

## How to Run
In your Linix Bash Terminal, 
- python3 game.py
- Press S to start
and voila !!

For replay,
- python3 replay.py
- Enter the name of saved game

## Code Details
- Made using python, without the pygame library 
- Relies heavily on OOPS concepts like Inheritance, Polymorphism,
  Encapsulation and Abstraction

## Game Features

### Village
- Townhall
- Huts 
- Walls
- Cannon :
    Acts as defense against the troops
- Each building will have a certain amount of hitpoints (basically health) 
  and the remaining hitpoints of the building is denoted by its colour.
- A building with 0 hit points is considered destroyed and not
  displayed on the screen or targeted by troops.

### King
- User controlled character (by W/A/S/D) capable of attacking and destroying buildings.

### Barbarians
- The barbarians will always try to attack the nearest non-wall building and 
  will always move towards it. 
- The barbarian movement is automated.

### Spells
- Rage Spell:
  The Rage spell affects every troop alive in the game and the King.
  It doubles damage and movement speed.
- Heal Spell:
  The Heal spell affects every troop alive in the game and the King.
  It increases their health to 150% of the current health (capped at the maximum health)
- Area of Effect :
  The king  instead of attacking a single building with a sword, now uses an
  axe to do an AoE (Area of Effect) attack to all buildings in a specific vicinity.
- Noob Wall:
  Makes all walls ineffective and dissapear

### Game End 
- Each game can end in either victory or defeat.
  1. Victory: All buildings (excluding walls) have been destroyed.
  2. Defeat: All troops and the King have died without destroying all buildings.
- Once either of these conditions is satisfied, the game would end.

### Replays
- There is an option to store the replay of game after the end of each game.
- Every game played is stores in the replay directory
- Replay can be accessed by the command
  1. python3 replay.py
  2. Enter the name of saved game


## GAME INSTRUCTIONS

1. W,A,S,D (capital only) to move King
2. R for Rage spell
3. H for Heal spell
4. Press P for King AOE
5. Press 1 to Spawn at (1,1)
6. Press 2 to Spawn at (18,18)
7. Press 3 to Spawn at (1,10)
8. Press N for Noob Wall spell
9. Press E to end game
PRESS S TO START

## Specifics (can be modified easily)
1. Max Barbarians = 15
2. Defeat conditions : All 15 barbarians are used and dead and king is dead
3. Grid size : 20,20
4. Cannon range : 6
5. Cannon damage : 50
7. Buildings and walls health : 100
8. King health : 500
9. Barbarian health : 1000