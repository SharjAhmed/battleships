# Battleships 

(Developer: Sharj Ahmed)

[Live Webpage]()

![Alt text](assets/images/game-screenshot.png)

Battleships is a classic game.

This is a python version I created. The player must try and guess where the randomly placed ships are by choosing coordinates.

If the player guesses a coordinate where a ship is placed, that ship is sunk!

The aim of the game is to sink all of the 5 ships placed randomly by the computer, within 25 guess, or shots! 

A great little game to kill a few minutes when you're bored.

Can you beat the computer and sink all the ships before your turns run out? Choose your first coordinate and find out! 

## Table of contents
* [Project Goals](#project-goals)
* [User Experience](#user-experience)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Project Goals
* User Goals
    - play a fun game of Rock Paper Scissors Lizard Spock.
    - Check the rules of the game whenever they wish to.
    - Easily choose their option to play against the computer.
    - Keep track of the scores in the current game.
    - Play again when the player or computer reaches 5 points.
* Site Owner Goals
    - Make it easy for the player to understand how to play the game.
    - Make the scores easily visible to the player.
    - Reset the game once the player/computer reaches 5 points so the player can play again.
    - Make the gameplay experience fun to encourage revisits to the game. 

## User Experience
* Target Audience
    - This game is designed for anyone looking for a fun time passer.
    - Designed to keep all ages engaged.
* User Requirements and Expectations
    - A simple gameplay experience
    - The ability to choose rock, paper, scissors, lizard, or Spock.
    - Scores that are easily visible when playing.
    - An interactive and responsive page, regardless of what device they are on. 

## User Stories
* First-time Player
    1. As a first-time player, I want to be able to easily play a game of rock, paper, scissors, lizard, Spock.
    2. As a first-time player, I want to be able to check the rules easily whenever I want.
    3. As a first-time player, I want to be able to check the score as I am playing the game.
    4. As a first-time player, I want to be able to see what option the computer has chosen as I am playing the game.
* Returning Player
    1. As a returning player, I want to be able to play the game with as much enjoyment as the initial visit.
    2. As a returning player, I want to be able to re-check the rules. 
* Site Owner
    1. As the site owner, I want to be able to make the page well laid out so the player can easily navigate their way around.
    2. As the site owner, I want to be able to make it clear how to play, and how to check the rules.
    3. As the site owner, I want to make it clear what the scores are and who has won the game. 

## Design
* Color Scheme
    - The main decision for the color scheme chosen for the page is to make the page look appealing and clear for the player. 
    - I used a dark background with bright icons and a gold results bar.

* Fonts
    - I wanted to use a font that was easy to read but also looked fun.
    - I decided to use Comfortaa from [Google Fonts](https://fonts.google.com/specimen/Comfortaa/about?query=comfortaa) (Designed by [Johan Aakerlund](https://www.deviantart.com/aajohan/art/Comfortaa-font-105395949)) as I feel the rounded style gives a fun feel but is also easy to read.
        
    ![Alt text](assets/images/font.png)

* Structure
    - The page has been structured so that everything appears without the need to scroll up or down - all features appear on the one page in front of the player.
    - This makes the page user-friendly and easy to navigate. 
    - The title is at the top of the page with the game choices underneath.
    - The middle of the page has the game area where the player can see their score and choice, along with the computer's score and choice.
    - The gold banner shows the result after each round.
    - At the bottom of the page is the rules button, which when clicked on, brings up the rules of the game.

![Alt text](assets/images/page.png)

* Wireframes
    <details><summary>Desktop Wireframe</summary>
    <img src="assets/images/wireframe.png">
    </details>

    <details><summary>Tablet Wireframe</summary>
    <img src="assets/images/wireframe-tablet.png">
    </details>

    <details><summary>Mobile Wireframe</summary>
    <img src="assets/images/wireframe-mobile.png">
    </details>

        
   
## Features
* Title Area
    - I wanted the title to stand out so I decided to add the game icons alongside the text of each 'weapon'.

![Alt text](assets/images/title-area.png)

* Choice Area
    - I decided to stick with the colored theme to make the site consistent.
    - In keeping with the simple page design, the game choice icons are laid out horizontally.
    - A border appears over the icon when the mouse is hovering over it to make it easy for the player to see which option is being selected.

![Alt text](assets/images/choice-area.png)

![Alt text](assets/images/choice-area-hover.png)

* Game Area
    - The game starts with a "ready" image, to make it clear to the player that we are ready to start the game.
    - The image updates as the player chooses, to the player's chosen weapon and the randomly selected, computer choice.
    - This updates with each click.
    - Once the game is over (when either the player or computer reaches a score of 5), the images reset to the "ready" image.

![Alt text](assets/images/game-area.png)

* Results Area
    - Continuing the "ready" theme at the beginning of the game, the results banner starts with a "ready" message.
    - I wanted the results area to stand out on the page, so I decided to give the banner a gold color, which contrasts with the gray background.
    - As the player chooses, the message in the banner changes to inform the player of the outcome of that round - (if the player chooses rock, and the computer chooses paper - "You Lose! Paper Covers Rock!" will show, etc.)
    - I made this decision as it keeps the game more engaging, as if the player is like myself, and doesn't know the rules by heart, this makes it easy to understand who won the round and why without having to click on the rules button frequently to check.

![Alt text](assets/images/results-area.png)

* Rules Area
    - I decided to place the rules area hidden until the rules button is clicked.
    - This keeps in theme with the simple layout of the page, as I found having the rules listed out visible permanently made the page look a lot messier.
    - Rules appear once the rules button is clicked on.
    - Once again, to keep things simple for the player, I have decided to list the rules out in order of rock -> paper -> scissors -> lizard -> Spock.
    - I have also clarified the criteria on how to win the game - the first to 5 points wins!

![Alt text](assets/images/rules-button.png)

![Alt text](assets/images/rules-content.png)

## Technologies
The project is created with:
* Languages
    - HTML
    - CSS
    - JavaScript

* Libraries Used 
    - [Git](https://git-scm.com/)
        - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
    - [GitHub](https://github.com/):
        - GitHub is used to store the project's code after being pushed from Git.
    - [Heroku](https://www.heroku.com)
        - 
    - [Balsamiq](https://balsamiq.com/):
        - Balsamiq was used to create the wireframes during the design process.

## Testing
* Browser Testing:
    - The site has been tested in the following browsers:
        - Google Chrome
        - Mozilla Firefox
        - Microsoft Edge

## Validator Testing
* Validator testing was done to ensure there are no syntax errors with the code:
    * PEP8
        - State if any errors were found

![Alt text]()


### Testing User Stories from User Experience Section
1. First-Time Player Goals:
    * 

2. Returning Player Goals:
    * 

3. Site Owner:
    * 
### Bugs
- Solved bugs
    - 
- Unfixed bugs
    - 


## Deployment

* This project was deployed using Code Institute's mock terminal for Heroku.

 - Steps for deployment:
     - Fork or clone this repository
     - Create a new Heroku app
     - Set the build-backs to ```Python``` and ```NodeJS``` in that order
     - Link the Heroku app to the repository
     - Click on **Deploy**
    
## Credits 

* 