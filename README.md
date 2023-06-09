![Title](assets/images/title.png)

(Developer: Sharj Ahmed)

[Live Webpage](https://battleships-01.herokuapp.com/)

![Responsive](assets/images/responsive.png)

![Game Screenshot](assets/images/game-screenshot.png)

Battleships is a classic game.

This is a python version I created. The player must try and guess where the randomly placed ships are by choosing coordinates.

If the player guesses a coordinate where a ship is placed, that ship is sunk!

The game aims to sink all of the 5 ships placed randomly by the computer, within 25 guesses, or shots! 

A great little game to kill a few minutes when you're bored.

Can you beat the computer and sink all the ships before your turns run out? Choose your first coordinate and find out! 

## Table of contents
* [Project Goals](#project-goals)
* [User Experience](#user-experience)
* [User Stories](#user-stories)
* [Flowchart](#flowchart)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Validator Testing](#validator-testing)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)


## Project Goals
* User Goals
    * play a fun game of Battleships.
    * Check the status of the game board as they play.
    * Easily choose their options to play against the computer.
* Site Owner Goals
    * Make it easy for the player to understand how to play the game.
    * Make the scores easily visible to the player.
    * End the game either when all 5 ships are hit or when all 25 turns have been used up.
    * Make the gameplay experience fun and challenging to encourage revisits to the game. 


## User Experience
* Target Audience
    * This game is designed for anyone looking for a fun time passer.
    * Designed to keep all ages engaged.
* User Requirements and Expectations
    * A simple gameplay experience
    * The ability to choose the coordinates for their shot.
    * Game board that is easily visible when playing.


## User Stories
* First-time Player
    1. As a first-time player, I want to be able to easily play a game of Battleships.
    2. As a first-time player, I want to understand how to play the game.
    3. As a first-time player, I want to be able to check the game board as I am playing the game.
* Returning Player
    1. As a returning player, I want to be able to play the game with as much enjoyment as the initial visit.
    2. As a returning player, I want to be able to re-check the rules. 
* Site Owner
    1. As the site owner, I want to be able to make it clear how to play, and how to check the rules.
    2. As the site owner, I want to make it clear what the progress is and who has won the game. 


## Flowchart
* I designed the basic function of this game in a flowchart in [Lucidchart](https://www.lucidchart.com/pages/examples/flowchart-maker). 
* This helped me to plan the logic and structure of the game. 
* The flowchart runs through the initial stage of setting up the game and loops through each guess stage until a win is detected.

![Flowchart](assets/images/flowchart.png)


## Features
* Title Area
    * I wanted to keep the title area clean and simple, but not boring. So I added the ship emoticons on either side.

![Title Area](assets/images/title-area.png)

* Game Criteria
    * I wanted to state the criteria on how to beat the game early on before the player starts playing so that they have an understanding of what needs to be done to win.
    * I also included a Game Legend so the player understands what each emoticon on the board means.

![Game Criteria](assets/images/game-criteria.png)

* Game Board
   * I wanted the board to be visible after every round and to be easy to understand.
   * I decided to label each axis with numbers (1-8) for the rows and letters (A-H) for the columns.

![Game Board](assets/images/game-board.png)

* Gameplay
    * The player is asked to enter a row and column to play their shot

![Gameplay](assets/images/gameplay.png)

* Invalid Row/Column
    * If an invalid character is entered, then they are met with the message "Please enter a valid column"

![Error Message](assets/images/error.png)

* Duplicate Guess
    * If a player guesses a spot they have already chosen, they are met with the message "You've already guessed that! Please guess again"

![Guess Again](assets/images/guess-again.png)

* Missed Shot
    * If the player misses a ship with their shot, they are met with the message "Ah unlucky, you missed!"

![Missed Shot](assets/images/missed-shot.png) 

* Hit Ship
    * If the player hits a ship with their guess, they are met with the message "GREAT SHOT! you sunk a battleship!"

![Hit Ship](assets/images/hit-ship.png)

* Game Won
    * If the player hits all 5 ships, they win the game and are met with the message "CONGRATULATIONS! You've sunk all 5 battleships!"

![Game Won](assets/images/win-game.png)

* Game Over
    * If the player uses up all 25 guesses and hasn't sunk all 5 ships, then they lose and are met with the message "GAME OVER! you have 0 turns remaining"

![Game Over](assets/images/game-over.png)


## Technologies
The project is created with:
* Languages
    * Python

* Libraries Used 
    * [Git](https://git-scm.com/)
        * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
    * [GitHub](https://github.com/):
        * GitHub was used to store the project's code after being pushed from Git.
    * [Heroku](https://www.heroku.com)
        * Heroku is a cloud-based platform used to deploy the application on.

## Testing
* Browser Testing:
    * The site has been tested in the following browsers:
        * Google Chrome
        * Mozilla Firefox
        * Microsoft Edge


## Validator Testing
* Validator testing was done to ensure there are no syntax errors with the code:
    * PEP8
        * Code ran through [CI Python Linter](https://pep8ci.herokuapp.com/) and no error were found.

![PEP8](assets/images/pep8.png)


### Bugs
| Bug | How I solved the issue |
| :--- | :--- |
| When testing the game I realised that when the player guesses a space they have already guessed, the function did not work. | After investigating further, I realised that there was a space in the function that should not have been there after "⊗ " - corrected to "⊗" - this solved the issue. |

### Unsolved Bugs
| Bug | Image |
| :--- | :--- |
| On the initial game board, the column headings appear twice, this does not happen once the player has made a guess | ![Game Board Bug](assets/images/bug.png) |

### Testing User Stories
| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| | | |
|`First Time Player` |
| Easily play a game of Battleships | Game automatically moves onto mext step once the player has made a choice | |
| Understand how to play |  Rules are explained before player makes a choice | ![Game Screenshot](assets/images/game-screenshot.png)
| Be able to check the game board as the game is being played | After every turn the game board is visible showing what cooridnates have already been chosen | |
| | | |
|`Returning Player` |
| Play the game with as much enjoyment as the initial visit | Game is randomised so no two games will ever be the same | |
| Ability to recheck the rules | As before, the rules are stated before the game begins | | 
| | | |
|`Site Owner` |
| Make it clear how to play, and how to check the rules | Rules are clearly stated before the game is played | | 
| Make it clear what the progress is and who has won the game | Updated board is shown after every round, and a message is shown depending on whether the player has hit/missed a ship or guessed a space they have already guessed previously. Upon game ending, they will be informed whether they have won after hitting all ships or lost after running out of moves | |

## Deployment

* This project was deployed using Code Institute's mock terminal for Heroku.

 * Steps for deployment:
     * Fork or clone this repository
     * Create a new Heroku app
     * Set the build-backs to ```Python``` and ```NodeJS``` in that order
     * Link the Heroku app to the repository
     * Click on **Deploy**
    

## Credits 
* My fellow students for helping me understand the python code for the gameplay.
* https://www.youtube.com/watch?v=XTr5OF9MRCg&list=PLw22WCqAVCN6EXylkzhtMwvgcLq4TrcQX and https://www.youtube.com/watch?v=7Ki_2gr0rsE for helping me understand python behind the gameplay.
* [Code Playground](https://trinket.io/python/f7ad7f9864) - Used to write code freely and do quick testing.
* [Geeks for Geeks](https://www.geeksforgeeks.org/python-string-join-method/) - for helping me better understand Python String join()
* [Learn Python](https://learnpython.com/) - for helping me understand some basic Python functions.
* And as always, my mentor Jubril for helping me through my projects!
