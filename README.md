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
5. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
6. [Testing](#testing)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatability)
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

![loser](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/lose.jpg)

- If you have drawn you will get the following message.

![draw](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/draw.jpg)

- If you have get to a score of 2 before the computer you win the game and receive the following message.

![overallwin](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/overallwin.jpg)

- If the computer gets to 2 before you then the message will pop up and end the game!

![overalllose](https://raw.githubusercontent.com/Paulnolan90/p3-RockPaperScissors/main/assets/overalllose.jpg)

- __Home page big image__

  - The home page displays an image of mountains, with an overlay of the Irish scouting logo with “115th Ballinteer” and “expect the unexpected!” text appearing slowly to grab the user’s attention.
  - This image introduces the user to Ballinteer scouts with an animated image that zooms slowly away and fades in the text.


![Home Page](https://github.com/Paulnolan90/p1-scoutinggroup/blob/main/assets/images/MainImage.jpg)

- __Our Groups Section__

  - The Groups section will give users information on the age range for our different groups within Ballinteer scouts, it will also give a small introduction to what each group does throughout the year.
  - The user will also see images of each of the age groups having fun and enjoying themselves


![Our Groups](https://github.com/Paulnolan90/p1-scoutinggroup/blob/main/assets/images/OurGroups.jpg)
- __Group Weekdays/Times__

  - This section shows which group meetup on which day and what time they meet, all meetings are in Ballinteer scout den so I did not put the location as I have a separate “Find us” page.

![Group Times](https://github.com/Paulnolan90/p1-scoutinggroup/blob/main/assets/images/GroupTimes.jpg)


- __The Footer__ 

  - The footer section has 4 images representing the 4 main social media channels, these social media accounts provide further enchantment for the user to see what Ballinteer scouts are about.

![Footer](https://github.com/Paulnolan90/p1-scoutinggroup/blob/main/assets/images/footer.jpg)

- __Find us Page__

  - The Find us page will present a google map, that will show where we are located in Ballinteer.
  - This section is of high importance as we are slightly hidden away from the road and this will make the user’s experience easier. It also shows our address plus Eircode.
 

![Find us](https://github.com/Paulnolan90/p1-scoutinggroup/blob/main/assets/images/Findus.jpg)
- __Find us Page__

  - This page will allow the user to sign up for Ballinteer scouts and get a call back from one of the leaders depending on which section they choose in the form.
  - The form asks for the parent’s details and the child’s details that they wish to get involved.
 

![Sign Up](https://github.com/Paulnolan90/p1-scoutinggroup/blob/main/assets/images/SignUp.jpg)
For some/all of your features, you may choose to reference the specific project files that implement them.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:


## Technologies Used
### Languages

- HTML
- CSS

### Frameworks and Tools

- Git
- GitHub
- Font awesome
- Google Fonts
- Git
- Canva palette generator
- GIMP image editing software

## Design

### Design Choices
The main focus when desigining the website was for easy navigation, after completeing this I wanted to make sure that it looked modern whilst also looking slihghtly outdoorsy as it is a scout group after all.

### Colours
The colour scheme was picked to represent the outdoor aspect of the group while also representing the colors used on ballinteers neckerchief.

### Fonts
Merriweather was used for the headings while Robotto was used in the paragraphs.

### Structure

The website was designed in a traditional way with the logo to top left and the navigation links to the far right, the navigation links were designed with an underline+overline when hovered over so that they are extremely responsive.

The Navigation bar turns into a "burger" menu when the viewed on a mobile screen which when clicked slides across the screeen to reveal the 3 options.

The webiste has 3 pages:
1. a home page with a big image with text appearing to capture the user.
2. a find us page that shows our location on a google map.
3. a form page that allows parents to submit a form with their details plus their childs for a call back from a leader.


## Testing 

### HTML Validation 
<details><summary>Home</summary>
    <img src="docs/Valid/Validation/indexvalid.jpg">
    </details>

<details><summary>Find Us</summary>
    <img src="docs/Valid/Validation/findusvalid.jpg">
    </details>

<details><summary>Sign up</summary>
    <img src="docs/Valid/Validation/signupvalid.jpg">
    </details>

### CSS Validation 

<details><summary>CSS</summary>
    <img src="docs/Valid/Validation/cssvalid.jpg">
    </details>

### Accessibility

<details><summary>Home</summary>
    <img src="docs/Valid/Validation/indexAccessibility.jpg">
    </details>

<details><summary>Find Us</summary>
    <img src="docs/Valid/Validation/findusaccess.jpg">
    </details>

<details><summary>Sign up</summary>
    <img src="docs/Valid/Validation/signupaccess.jpg">
    </details>

### Performance

<details><summary>Home</summary>
    <img src="docs/Valid/Validation/indexspeed.jpg">
    </details>
<details><summary>Find Us</summary>
    <img src="docs/Valid/Validation/findusspeed.jpg">
    </details>
<details><summary>Sign Up</summary>
    <img src="docs/Valid/Validation/signupspeed.jpg">
    </details>

## Different Devices

The website was tested on the following devices:

- Dell Optiplex 7080
- Huawei P30 pro
- Apple Ipad A13

## Browser Compatability

the website was run successfully on the following browsers:

- Google Chrome
- Opera
- Microsoft Edge

### Bugs

Submit button on sign up page was not contrasting enough with the background according to Wave testing so font color was changed.
Retest was done and all clear.

The form that I built on the sign-up page does not send information to anyone as this would require further knowledge that is later in the course.

## Deployment

The website was deployed using Github pages.

How to: 

  - In Github login and go to the correct repo. go into its settings.
  - Once in settings go to the "pages" page.
  - Select "Deploy from Branch".
  - Select "Main" and "root" in the branch options below.
  - After a few minutes you will get a message saying "Your site is live at https://paulnolan90.github.io/p1-scoutinggroup/"


## Credits 

Any images not mentioned below were my own images editited in GIMP.
### Media

In order of appearance:
- Two beavers looking scruffy having fun - [Scouting Ireland Beaver page](https://www.scouts.ie/what-we-do/beaver-scouts)
- Cub in uniform smiling - [Scouting Ireland Cub page](https://www.scouts.ie/what-we-do/cub-scouts)
- Scouts celebrating in uniform - [Scouting Ireland Scout page](https://www.scouts.ie/what-we-do/scouts)
- Venture scouts talking in field - [Scouting Ireland Venture page](https://www.scouts.ie/what-we-do/venture-scouts)

### Code

In order of appearance:
- For the text fading in i read through and implemented this tutrial [HubSpot](https://blog.hubspot.com/website/css-fade-in#text-transition)
- To add the google map to my Find us page I read through this tutorial [Uni of Maine](https://extension.umaine.edu/plugged-in/technology-marketing-communications/web/tips-for-web-managers/embed-map/)
- For the sign up form I rewatched the tutorial Love Running done by Code institute. I also reused the CSS to zoom out the main image, but I reversed this as it suited my image more [Code Institute](https://code-institute-org.github.io/love-running-2.0/index.html)
- To make and add the Favicon  I went through this tutorial [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-a-favicon-to-your-website-with-html)


### Content 

- The text for the Home page Our Groups section was taken from [Scouting Ireland](https://www.scouts.ie)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- The form page was inspired by the Love Running task done with [Code Institute](https://codeinstitute.net/ie/)


