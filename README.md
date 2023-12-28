# Introduction

This Python script implements a simplified version of the board game "Avalon," a social deduction game where players take on the roles of characters from Arthurian legend. The game involves quests, alliances, and hidden identities, making it an engaging experience for a group of players.

## Game Rules and Logic

The script defines a set of characters, both good and bad, with unique abilities. The game progresses through a series of quests, and players must form teams to complete these quests. The success or failure of each quest is determined by the players on the team, with the bad characters trying to sabotage the quests.

## Characters

### Good Characters:

- Merlin
- Percival
- Sir Galahad
- Sir Bedivere
- Sir Gaheris
- Sir Lamorake

### Bad Characters:

- Assassin
- Maleagant
- Annowre
- Morgana

## Gameplay

1. Players enter their names and are assigned characters randomly.
2. The script reveals each player's character privately, with special information for characters like Merlin and Percival.
3. The game then progresses through a series of quests, where players form teams, and the success or failure of each quest is determined by the choices made by the team members.
4. The game ends when either the Loyal Servants of Arthur or the Minions of Mordred achieve their victory conditions.

# Script Organization

The script is organized into two main sections: character definition and the main game logic.

## Character Definition

The characters are defined with their names, IDs, and abilities. The number of good and bad players is determined based on the number of players in the game.

## Main Game Logic

1. Players are assigned characters based on the number of players and character availability.
2. Players view their roles secretly, and specific characters receive additional information.
3. The game progresses through a series of quests, with players forming teams and deciding whether to accept or reject each team.
4. Teams that are accepted proceed to the quest phase, where players secretly vote to pass or fail the quest.
5. The game ends when a team successfully completes three quests or when the bad characters successfully sabotage three quests.

**Note:** This script is a simplified version of the Avalon game and may require further refinement for a complete and polished gaming experience. Enjoy playing Avalon!
