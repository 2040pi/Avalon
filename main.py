##
## Title:  Avalon
## Author: Bobby Greenan
## Date:   2023
##

import random
import time

players_playing_bad = []
player_side = []
players_playing_merlin = []

##
## pick_team - start
##
def pick_team(quest_number):
	quest_teams = [[2, 2, 2, 3, 3, 3], [3, 3, 3, 4, 4, 4], [2, 4, 3, 4, 4, 4],
								 [3, 3, 4, 5, 5, 5], [3, 4, 4, 5, 5, 5]]
	return players_on_team


merlin = ["Merlin", 1, 0, 0, 0, 1, 0, 0, 1]
assassin = ["Assassin", 2, 1, 1, 1, 0, 0, 1, 0]
good1 = ["Sir Galahad", 3, 0, 0, 0, 0, 0, 0, 0]
good2 = ["Sir Bedivere", 4, 0, 0, 0, 0, 0, 0, 0]
good3 = ["Sir Gaheris", 5, 0, 0, 0, 0, 0, 0, 0]
good4 = ["Sir Lamorake", 6, 0, 0, 0, 0, 0, 0, 0]
bad1 = ["Maleagant", 7, 1, 1, 1, 0, 0, 0, 0]
bad2 = ["Annowre", 8, 1, 1, 1, 0, 0, 0, 0]
percival = ["Percival", 9, 0, 0, 0, 0, 1, 0, 0]
morgana = ["Morgana", 10, 1, 1, 1, 0, 0, 0, 1]
#oberon = ["Oberon",11,1,0,1,0,0,0,0]
#mordred = ["Mordred",12,1,1,0,0,0,0,0]
max_players = 10

good_players = 1
bad_players = 1
players_count = 2
players_playing = [merlin[0], assassin[0]]
bad_per_player = [0, 0, 0, 0, 2, 2, 3, 3, 3, 4]

players = 6

## can we calculate these based on the number of players?
percival_in_play = 1
#oberon_in_play = 0
#mordred_in_play = 0
good1_in_play = 1
good2_in_play = 1
good3_in_play = 0
good4_in_play = 0
bad1_in_play = 0
bad2_in_play = 0

if players < 5:
	print("Need More Players")
	exit()

if players > max_players:
	print("Too Many Players")
	exit()

print("Merlin Added")

if percival_in_play:
	good_players += 1
	print(percival[0], " Added")
	players_count += 1
	players_playing.append(percival[0])

if good1_in_play:
	good_players += 1
	print(good1[0], " Added")
	players_count += 1
	players_playing.append(good1[0])

if good2_in_play:
	good_players += 1
	print(good2[0], " Added")
	players_count += 1
	players_playing.append(good2[0])

if good3_in_play:
	good_players += 1
	print(good3[0], " Added")
	players_count += 1
	players_playing.append(good3[0])

if good4_in_play:
	good_players += 1
	print(good4[0], " Added")
	players_count += 1
	players_playing.append(good4[0])

print("Assassin Added")
if bad1_in_play:
	bad_players += 1
	print(bad1[0], " Added")
	players_count += 1
	players_playing.append(bad1[0])

if bad2_in_play:
	bad_players += 1
	print(bad2[0], " Added")
	players_count += 1
	players_playing.append(bad2[0])

if percival_in_play:
	bad_players += 1
	print(morgana[0], " Added")
	players_count += 1
	players_playing.append(morgana[0])

#if oberon_in_play:
#	bad_players += 1
#	print(oberon[0] ," Added")
#	players_count += 1
#	players_playing.append(oberon[0])

#if mordred_in_play:
#	bad_players += 1
#	print(mordred[0] ," Added")
#	players_count += 1
#	players_playing.append(mordred[0])

print("Good players: ", good_players)
print("Bad players:  ", bad_players)

if good_players + bad_players > players:
	print("Error: Too many characters added - %d required, %d entered", players, good_players + bad_players)
	exit()

if good_players + bad_players < players:
	print("Error: Too few characters added - %d required, %d entered", players, good_players + bad_players)
	exit()

if bad_players != bad_per_player[players - 1]:
	print("Bad Players added exceed or fall short of bad players needed")
	exit()

##
## enter player names
##
player_names = []
for q in range(players):
	while True:
		player_name = input("What is your name? (One word please): ")
		if player_name and player_name not in player_names:
			print(player_name, "You are player number", q + 1)
			player_names.append(player_name)
			break
		else:
			print("Invalid input. Please enter a non-blank and non-duplicate name.")

random.shuffle(players_playing)

for a in range(0, players_count):
	if players_playing[a].startswith('Sir') or players_playing[a].startswith('Mer') or players_playing[a].startswith('Per'):
		 players_playing_bad.append(0)
	else:
	 	 players_playing_bad.append(1)

players_playing_morgana = []

for c in players_playing_bad:
	if c == 0:
		player_side.append("Good")
	else:
		player_side.append("Bad")

for d in range(0, players_count):
	if players_playing[d].startswith('Mer'):
		players_playing_merlin.append(1)
	else:
		players_playing_merlin.append(0)

for i in range(0, players_count):
	if players_playing[i].startswith('Morg'):
		players_playing_morgana.append(1)
	else:
		players_playing_morgana.append(0)

bad_numbers = [""] * players_count
print(players_playing_bad)
for e in range(0, len(players_playing_bad)):
	if players_playing_bad[e] == 1:
		if e < len(bad_numbers):
			bad_numbers[e] = e + 1
bad_numbers = [name for name in bad_numbers if name != ""]
print(bad_numbers)
bad_names = []
for q in range(len(bad_numbers)):
	bad_names.append(player_names[bad_numbers[q] - 1])
print(bad_names)
percival_numbers = [""] * players_count
players_playing_percival = [""] * players_count
percival_reveal = [""] * players_count

for h in range(0, players_count):
	if players_playing[h] == "Percival":
		players_playing_percival[h] = 1
	else:
		players_playing_percival[h] = 0

k = 0
for j in players_playing:
	if j == "Merlin" or j == "Morgana":
		percival_numbers[k] = 1
	else:
		percival_numbers[k] = 0
	k += 1

for l in range(0, len(percival_numbers)):
	if percival_numbers[l] == 1:
		if l < len(percival_reveal):
			percival_reveal[l] = l + 1
percival_reveal = [name for name in percival_reveal if name != ""]

percival_names = []
for r in range(len(percival_reveal)):
	percival_names.append(player_names[percival_reveal[r] - 1])

# list all player numbers and names
for z in range(len(player_names)):
	print(player_names[z], ":", z+1 )

# show each player what character they are
# TODO - check for duplicate numbers

validentry = 0
while validentry == 0:
	tellstr = input("What is your player number? ")
	if tellstr.isnumeric():
		tell = (int(tellstr) - 1)
		if tell < players:
			validentry = 1
		else:
			print("That number is too high")
	else:
		print("YOU NEED TO TYPE IN A NUMBER YOU IDIOT!!!!")

	input("Everyone else look away and press enter")
	print(players_playing[tell], player_side[tell], end="\r")
	time.sleep(2)
	
	if players_playing_percival[tell] == 1:
		print("Mer and Morg:", percival_names, end="\r")
	
	if players_playing_merlin[tell] == 1:
		print("Bad:", bad_names, end="\r")
	
	if players_playing_bad[tell] == 1:
		print("Bad:", bad_names, end="\r")
	
	time.sleep(3)
	print("                                          ", end="\r")

print(
 "All players have viewed their roles. We can now move on to play the game")

players_on_team = []

failed_quests = 0
denied_quests = 0
passed_quests = 0

for n in range(5):
	accept = []
	pass_quest = []
	print(
	 f"Quest {n + 1} Started. {player_names[random.randint(0, players - 1)]} is the leader."
	)
	players_on_team = pick_team(n + 1)
	print(players_on_team)
	for o in range(players):
		print(f"{player_names[o]}, do you accept this team? Type 'y' or 'n'")
		validentry = 0
		while validentry == 0:
			acceptst = input("")
			if acceptst == "y" or acceptst == "n":
				validentry = 1
				accept.append(int(acceptst))
	if accept.count(1) <= players / 2:
		print("Denied. :(")
		denied_quests += 1
		n -= 1
		if denied_quests == 5:
			print("Minions of Mordred win.")
	else:
		print("Accepted. :)")

for p in range(len(players_on_team)):
	print("Everyone apart from ", player_names[p], "look away")
	print("Do you PASS or FAIL? wait for this to go away", end="\r")
	time.sleep(2)
	print("                                                  ", end="\r")
	pass_quest.append(input(""))
	print("                               ", end="\r")
if pass_quest.count("FAIL") > 0:
	print("QUEST FAILED!")
	failed_quests += 1
	if failed_quests == 3:
		print("Minions of Mordred win.")
else:
	print("QUEST PASSED")
	passed_quests += 1
	if passed_quests == 3:
		print("Loyal servants of Arthur have secured the victory")

		print(
		 "Assassin, it's time to guess Merlin. Enter the ID of the player you suspect:"
		)
		assassin_guess = int(input())

		if players_playing[assassin_guess - 1] == "Merlin":
			print("Assassin's guess is correct! Minions of Mordred win.")
		else:
			print("Assassin's guess is incorrect! Loyal servants of Arthur win.")
print("Denied Teams", denied_quests, "/5")
print("Failed Quests", failed_quests, "/3")





team_size = quest_teams[quest_number - 1][players - 5]
print(team_size, "test")
players_on_team = []
print("Pick", team_size, "players")
for m in range(team_size):
		validentry = 0
		while validentry == 0:
			playerst = input(
			 f"Enter the ID of player for quest {quest_number}, position {m + 1}: ")
			if playerst.isnumeric():
				player = (int(playerst) - 1)
				if player < players:
					validentry = 1
				else:
					print("That number is too high")
			else:
				print("YOU NEED TO TYPE IN A NUMBER YOU IDIOT!!!!")

		players_on_team.append(player)




##
## pick_team - end
##
