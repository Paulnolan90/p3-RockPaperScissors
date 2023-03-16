# Rock Paper Scissors 

Rock Paper Scissors is a game built on Python code, which runs in Heroku!

![Feature.jpg](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/Main.png)

[Live game](https://rockpaperscissorspn.herokuapp.com/)

## Table of Content

1. [How to play](#how-to-play)
2. [Features](#features)
    1. [Existing Features](#existing-features)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-and-tools)
6. [Testing](#testing)
    1. [Python Validation](#Python-validation)
    2. [Device testing](#performing-tests-on-various-devices)
    3. [Browser compatibility](#browser-compatability)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
    1. [Media](#media)
    2. [Code](#code)
    3. [Content](#content)


## How to play 

Rock Paper Scissors is based around the old game that kids and adults play by using their hands to show which of the 3 they have chosen,

it is a simple game in which rock beats scissors, paper beats rock & scissors beats paper. you can read more about it by [clicking here](https://en.wikipedia.org/wiki/Rock_paper_scissors)

The aim of the game is to beat the computer to a score of 2!.

## Features 

### Existing Features

- __Random computer number generator__

  - The python code calls on the random function to randomly assign the computer 0,1,2 each refering to rock,paper or scissors.
  - The player does not know which the computer has picked until they have entered their input.
  
![user input](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/userinput.jpg)

  - The game then checks your guess against the computers guess.
  - If you have beaten the computer you get the following message.

![winner](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/win.jpg)

 - If you have lost you will get the following message.
 - Your wins are stored in an instance variable.

![loser](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/lose.jpg)

- If you have drawn you will get the following message.

![draw](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/draw.jpg)

- If you have get to a score of 2 before the computer you win the game and receive the following message.

![overallwin](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/overallwin.jpg)

- If the computer gets to 2 before you then the message will pop up and end the game!

![overalllose](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/overalllose.jpg)

- you cannot enter anything outside of "rock" "paper" "scissors" or "q" for quit. If you do the game will repeat the question.
- The computers wins are stored in an instance variable.

## Technologies Used
### Languages

- Python

### Frameworks and Tools

- Git
- GitHub
- Heroku


## Testing 

### Python Validation 

![pythontest](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/pythonlinter.jpg)

- No major issues in online testing.
- I have played this game too many times to count in testing the outcomes and text returned.
- Tested in gitpod and in Heroku.

## Different Devices

The game was tested on the following devices:

- Dell Optiplex 7080
- Huawei P30 pro
- Apple Ipad A13

## Browser Compatability

the game was run successfully on the following browsers:

- Google Chrome
- Opera
- Microsoft Edge

### Bugs

Solved Bugs


- When I finished the project in gitpod I had all of the print statments in ASCII which seemed to work ok in gitpod, this did not translate well to Heroku so I had to go back to simple messages.

![pythontest](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/Ascii.jpg)

- When writing the code and testing i noticed that after every wrong guess it would not change the computers guess. This was because the loop was not starting again when asking for your next guess, so I added the self.random_number = random.randint(0, 2) to run after every user input this way you the next guess would be random again.

- I added a max score for the computer or user to 2, the game was taking way too long with a higher score as there can be draws.


## Deployment

The game was deployed using Heroku pages.

How to: 

  - Create a new app in Heroku.
  - Name the app and select the location Europe.
  - Go to settings tab and click add buildpack.
  - Select python and nodejs.
  - Go to deploy section.
  - Select github and connect.
  - Search for repository name and connect.
  - Now click Deploy Branch.
  - Wait a few moments as it builds the app.
  - Eventually you can click on View, this will bring you to your deployed app.


## Credits 
Code institute for the deployment terminal.


### Code



