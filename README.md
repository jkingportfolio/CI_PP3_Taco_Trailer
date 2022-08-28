# The Taco Trailer
Developer: Jamie King

![Responsive image](docs/am-i-responsive.png)

[The Taco Trailer](https://taco-trailer.herokuapp.com/) website has been developed to provide users the chance to <>. 

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colours](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
    6. [Game Flowchart](#game-flowchart)
4. [Technologies Used](#technologies-used)
    1. [Coding Languages](#coding-languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#testing)
    1. [HTML Valiadation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [JavaScript Validation](#javascript-validation)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Device Testing](#device-testing)
    7. [Browser Compatibility](#browser-compatibility)
    8. [Testing User Stories](#testing-user-stories)
7. [Bugs](#bugs)
    1. [Code Bugs](#code-bugs)
    2. [Console Bugs](#console-bugs)
8. [Deployment](#deployment)
    1. [EmailJS API](#emailjs-api)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- A user would want to <>.
- A user would want to <>.
- A user would want to <>.
- A user would want to <>.
- A user would want to <>.

### Site Owner Goals

- As the site owner i wanted to <>.
- As the site owner i wanted to <>. 
- As the site owner i wanted to <>.
- As the site owner i wanted to <>.

## User Experience

### Target Audience

- <>.
- <>.
- <>.

### User Requirements and Expectations

- <>.
- <>.
- <>.
- <>.
- <>.
- <>.
- <>.

### User stories

1. As a user, I want to <>.
2. As a user, I want to <>.
3. As a user, I want to be <>.
4. As a user, I want to be <>.
5. As a user, I want to be <>.
6. As a user, I want to be <>.
7. As a user, I want to be able to <>.
8. As a user, I want to be able to <>.
9. As a user, I want to be able to <>.
10. As a user, I want to be able to <>.
11. As a user, I want to be able to <>.

### Site Owner Stories

12. As the site owner, I want <>.
13. As the site owner, I want <>.
14. As the site owner, I would want the user to <>.
15. As the site owner, I would not want the user to have to result in using the browser back button to navigate back to the site if a 404 error occurs.
16. As the site owner, I would want <>.
17. As the site owner, I want users to be greeted with a welcome message to give a friendly feel to the site. 

## Design

### Design Choices

The app was designed with a clean simple design in mind. <>. 

### Colours

The colour palette for the website is made up of 5 main colours:

- #FFFFFF (White)
- #000000 (Black)
- #FF0000 (Red)
- #FFFF00 (Yellow)
- #2B2EE2 (Blue)

The background gradient consists of <> colours:

- #E0B5B5 
- #EABFB0
- #ECCBAD
- #D6DAAF
- #DAE9BA

All colours contrast was tested using [EightShapes contrast grid](http://eightshapes.com/)

<details>
<summary>Colour Contrast Results</summary>
<img src="docs/validation-colour-contrast.png">
</details>

### Fonts

There were 2 fonts used in this project, as stated below:
- <>.
- <>.

### Structure

The website's structure was carefully constructed whilst making it recognizable, user friendly and simple. On arrival to the website the user will be presented with a notification that indicates click to play and a navigation bar which in which page modals can be accessed. The website is made of one main page, a 404 page and 4 modals:

- A homepage, which houses the game and comes with a nav bar which on click will display the desired modal.

### Wireframes

Balsamiq was used in the initial design stage to layout sketches of each page and its design intent

<details>
<summary>Index</summary>
<img src="docs/wireframes/index.html.png">
</details>

### Flowchart

A flowchart was created during the design process to help identify functions that would be required in the Python files.

<details>
<summary>Flow Chart</summary>
<img src="docs/js-logic-flow-annotated.jpg">
</details>

## Technologies Used

### Coding Languages
- Python - Used to create <>

### Frameworks and Tools
- Balsamiq - Used to create wireframes.
- Git - Used for version control.
- GitHub - Used to deploy the projects code.
- Gitpod - Used to develop and test code.
- LibreOffice Draw - Used to create the game logic flowchart.
- Eightshapes - Used to check colours for contrast and accessibility.

## Features

In its entirety the website consists of one main page, <>

### Existing features

#### <> 

The <> is featured on the main page and will <>

- Covered in user story: <>

##### Desktop 

![Nav Bar Desktop](docs/features/feature-nav-bar-tablet-desktop.png)

#### <>

The main <>.

- Covered in user story: <>

![Main game area](docs/features/feature-main-game-area.png)

### Future implementations

In the future as my skills grow I would like to implement the following features:

- <>
    - <>
    - <>
- <>
    - <>

## Testing

### HTML Validation
[W3C Markup Validation](https://validator.w3.org/) was used to validate the HTML code of The Connect 4 website. All pages passed and produced no errors.
<details>
<summary>Index</summary>
<img src="docs/validation-html/validation-index-html.png">
</details>
<details>
<summary>404 page</summary>
<img src="docs/validation-html/validation-404-html.png">
</details>

### CSS Validation

[W3C Jigsaw CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate the CSS used in the website. The file passed and produced no errors if testing my own CSS however it did produce some warnings which are related to Bootstrap 5.0.2
<details>
<summary>CSS styles</summary>
<img src="docs/validation-css/validation-css-style.png">
</details>
<details>
<summary>Bootstrap warnings</summary>
<img src="docs/validation-css/validation-bootstrap-css-warnings.png">
</details>

### Python Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python used in the app. <>

<details>
<summary>Python file - run.py</summary>
<img src="docs/validation-js/validation-jshint-connect-4.png">
</details>
<details>
<summary>Python file - order.py</summary>
<img src="docs/validation-js/validation-jshint-welcome.png">
</details>
<details>
<summary>Python file - google_sheet.py</summary>
<img src="docs/validation-js/validation-jshint-modals.png">
</details>
<details>
<summary>Python file - admin.py</summary>
<img src="docs/validation-js/validation-jshint-contact.png">
</details>
<details>
<summary>Python file - command_line.py</summary>
<img src="docs/validation-js/validation-jshint-contact.png">
</details>

### Accessibility

[The WAVE WebAIM](https://wave.webaim.org/) tool for evaluating accessibility of a webpage was used to verify that all pages of the site met the needs for users with disabilities.

<details>
<summary>Index</summary>
<img src="docs/validation-accessibility/accessibility-validation-index.png">
</details>

- Icons from Font Awesome are used in the site. Font Awesome already populates the code to be copied with an aria-hidden="true" attribute to accommodate accessibility.

### Performance

[Chrome dev tools lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test all pages for performance, accessibility, best practices and SEO.

<details>
<summary>Index</summary>
<img src="docs/validation-performance-lighthouse/lighthouse-performance-index.png">
</details>
<details>
<summary>404 page</summary>
<img src="docs/validation-performance-lighthouse/lighthouse-performance-404.png">
</details>


### Device Testing

As this app is only intended to be used on desktops the website was tested on the following devices:
- Windows 10 PC with a 24" MSI Curved gaming monitor

In addition to testing on physical devices, <>

### Browser Compatibility

The website was tested on the following web browsers:
- Google Chrome (Version 103.0.5060.114)
- DuckDuckGo

### Testing User Stories

#### Users

1. As a user, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Help Modal  | Click on the Help link from the Nav Bar  | The Help link from the nav bar is clicked and the help modal with information on the aim of the game, how to play and user controls is displayed     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-1.png">
</details>

2. As a user, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| New game modal  | Click on the New game modal from the Nav Bar  |  The New Game link from the nav bar is clicked and the new game modal will display. From there two buttons are presented, one being human the other being computer. The desired opponent button is clicked and the yes button is clicked to confirm and start the new game    | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-2.png">
</details>

3. As a user, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Notification Bar  | Play a game and the notification bar will display the correct notification  | Whilst in game the notification bar will be updated to state which player currently has a turn to take    | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-3.png">
</details>

4. As a user, I want to be <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Notification Bar  | Try to place a counter on an invalid cell  | Whilst in game the notification bar will be updated to state invalid move if the user clicks on a cell which is either occupied or does not have a counter beneath it     | Works as intended |
| Vibration Alert | Try to place a counter on an invalid cell | If a user is playing on a device which supports vibration, the device will vibrate to indicate a wrong move | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-4.png">
</details>

5. As a user, I want to be <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Notification Bar  | Play a game and the notification bar will display the correct notification |  When a player achieves 4 in a row the notification bar will update to state who won and disable all clicks    | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-5.png">
</details>

6. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Stats Button  | Hover over the stats button on Desktop or click if on a Mobile / Tablet device  | Whilst hover / click occurs the stats information will display to show the total number of player 1 wins, player 2 wins and draws     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-6.png">
</details>

7. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Settings modal  | Click on the Settings link in the Nav Bar, from the settings modal set music / sounds to be on or off | To be able to control if music / sounds are on or off whilst playing the game     | Works as intended |
| Master mute button  | Locate master mute button below the game board and click on it  | If clicked on it will turn both music and sounds off or on dependant on what state the sounds currently are     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-7.png">
<img src="docs/testing-user-stories/testing-user-stories-7.1.png">
</details>

8. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Contact modal  | Click on the Contact link in the Nav Bar, from the contact modal enter relevant information  | To be presented with the contact modal which once populated, entered information validated and submit button clicked will send the information to the site owner and a message will display to let the user know if the submission was successful or not      | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-8.png">
</details>

9. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Play again button  | Click on the Play Again button  | On game end the Play again button would appear and when clicked, the board will clear and a new game will commence  | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-9.png">
</details>

10. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Nav Bar  | Click on the desired Nav Bar link  |  To display the desired modal dependant on the choice of the user   | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-10.png">
</details>

11. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Main game area  | Open the game on a mobile device  | The site to show a high level of responsiveness to adjust to the mobile device screen     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-11.png">
</details>




12. As the site owner, I want users to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Contact modal  | Click on the Contact link in the Nav Bar  | To be presented with the contact modal which once populated, entered information validated and submit button clicked will send the information to the site owner and a message will display to let the user know if the submission was successful or not      | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-12.png">
</details>


13. As the site owner, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Footer  | Scroll to the bottom of the page and locate the social icons  | Social pages to open in new window if clicked on from the footer     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-13.png">
</details>

14. As the site owner, I would want the user to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| 404 page      | Try to access a page which does not exist   |  The user will be presented with a 404 error page indicating that the page does not exist    | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-14.png">
</details>

15. As the site owner, I would not want the user to have to result in using the browser back button to navigate back to the site if a 404 error occurs.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| 404 page return button  | Locate the Return Home button and click on it  | To be returned to the main page to be able to start a new game     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-15.png">
</details>

16. As the site owner, I would want users to be <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Orientation warning modal  |  On a mobile device rotate the screen from portrait to landscape |  On first instance of this orientation change the Orientation Warning modal will display. Once it has been shown once it will not be shown again until the page is reloaded.   | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-16.png">
</details>

17. As the site owner, I want users to be greeted with a welcome message to give a friendly feel to the site.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
| Welcome modal  | Navigate to the connect 4 website  | On page load the welcome modal will display automatically     | Works as intended |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-17.png">
</details>


## Bugs

### Code Bugs

During the project i encountered a number of bugs some of which were solved some of which were not as stated below:

| Bug           | Fix           |
| ------------- | ------------- |
| Computer opponent not placing a counter and turn reverting back to player 1  | This bug was due to the cells array adding 7 to the total length of the array when trying to validate if there was a counter underneath it thus trying to find a number outside of the array length if one of the randomly selected cells for placement was on the last row of the board, to fix this a variable called maxCells was added. Then the game play functioned as expected |
| Multiple turns for player 1 whilst it is computer player 2s turn  | There was no code to stop clicks, a function called disableClicks was added which would loop all cells and add the disable-click class to them which had pointer events set to none. This would then limit clicks by player one whilst the computer took its turn. | 
| Multiple wins within one game  | If there was an instance in which a player managed to get multiple 4 in a rows due to the loop looking for a match on all combinations a win could be counted multiple times in one game, a simple break was added to the function which would exit the function once one had been found. |
| Sound button does not update to reflect set values in settings modal  | A function was added to the click event listener for the buttons located in settings which if both buttons are set to off would be reflected by the master sound button displaying the muted symbol and if both music and sound settings were set to on the image would display the on symbol |
| In vs computer game, on game end the invalid move sound will still sound if clicked  | This bug happened due to the disable-click class being removed as soon as it was added. To fix this, the gameActive variable was added to control if the onePlayerGame function should run, previously it would by default which would be the cause of removal for disable-click class thus creating the bug in which the invalid move sound would still play. |
| Viewport height glitch whilst Player 2 animation running  | This glitch only happens when it is player 2s turn. The height of the page is set to 100vh and when the computer players turn animation runs the page can be scrolled down. This then stops once the animation stops running. After spending a lot of time trying to fix this I could not find the reason behind the bug and due to this bug self fixing and not effecting the user experience i decided to leave it as a known bug |

### Console Bugs

| Bug           | Reason           |
| ------------- | ---------------- |
| Interest cohort error | When the page is reloaded using Chrome there is an error message in the console `Error with Permissions-Policy header: Origin trial controlled feature not enabled: 'interest-cohort'.` Research online has shown that this is an effort to protect the privacy of users whilst using GitHub pages sites. As this bug is outwith my own control and does not affect functionality or User Experience it has been left as a known bug.|
| Navigator user agent error |When using Chrome there is an issue `Audit usage of navigator.userAgent, navigator.appVersion, and navigator.platform`. According to Chrome documentation this is done to "limit browser data shared to remove sensitive information and reduce fingerprints. As this bug is outwith my own control and does not affect functionality or User Experience it has been left as a known bug.|

<details>
<summary>Screenshots</summary>
<img src="docs/console-bugs/interest-cohort-error.png">
<img src="docs/console-bugs/navigator-user-agent-error.png">
</details>



## Deployment

### Heroku

This project was deployed to Heroku in the project's early stages to allow continual responsive testing. This was achieved via the following steps:

The website was deployed using Heroku by "following these steps:

1. Use the "pip freeze -> requiremnts.txt" command in the terminal to save any libraries that need to be instaled in the file
2. Login or create a Heroku account
3. Click the "new" button in the upper right corner and select "create new app"
4. Choose an app name and your region and click "Create app"
5. Go to the "settings" tab, add the python build pack and then the node.js build pack
6. Go to the "deploy" tab and pick GitHub as a deployment method
7. Search for a repository to connect to
8. Click enable automatic deploys and then deploy branch
9. Wait for the app to build and then click on the "View" link

### Forking the GitHub Repository

We can make a copy of the original repository on our GitHub account to view or make changes too without affecting the original repository, this is known as forking. Forking in GitHub can be done via the following steps:

1. Navigate to www.github.com and log in.
2. Once logged in navigate to the desired [GitHub Repository](https://github.com/jkingportfolio/CI_PP2_Connect4) that you would like to fork.
3. At the top right corner of the page click on the fork icon.
4. There should now be a copy of your original repository in your GitHub account.

Please note if you are not a member of an organisation on GitHub then you will not be able to fork your own repository.

### Clone a GitHub Repository

You can make a local clone of a repository via the following steps: 

1. Navigate to www.github.com and log in.
2. Once logged in navigate to the desired [GitHub Repository](https://github.com/jkingportfolio/CI_PP2_Connect4) that you would like to clone.
3. Locate the code button at the top, above the repository file structure.
4. Select the preferred clone method from HTTPS. SSH or GitHub CLI then click the copy button to copy the URL to your clipboard.
5. Open Git Bash
6. Update the current working direction to the location in which you would like the clone directory to be created.
7. Type `git clone` and paste the previously copied URL at Step 4.
8. `$ clone https://github.com/jkingportfolio/CI_PP2_Connect4`
9. Now press enter and the local clone will be created at the desired local location

## Credits

### Tutorials

- <>
- <>
- <> - [<>](https://www.w3schools.com/howto/howto_css_modals.asp)

### Terminal Font Images

Font images produced in this app were produced using the Pyfiglet library.

### Code

 Code from external sources were used as a basis and built on top of in this project, they are credited below:

 - <> [<>](https://github.com/kubowania/connect-four)
 - <> [<>](https://animista.net/)

### Literature

The use of reference books were used throughout the creation of this project and are credited below:

- Python Crash Course by <>, published by No Startch Press
- Python from beinnger to professional by <>, published by Packt Publishing
- JavaScript Pocket Reference by David Flanagan, published by O'Reilly

### Misc

The source of where I learned how to produce a GitHub fork and clone was from the following pages of the GitHub Documentation. Although I did not use a fork or clone in this project it is something I hope to implement to future projects now I have the knowledge to do so.

- https://docs.github.com/en/get-started/quickstart/fork-a-repo
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository


## Acknowledgements

I would like to also thank the following:
- My wife and family for their support and feedback whilst doing this project
- My fellow Code Institute students whom i have bounced ideas and problems back and forth with via Slack
- Carina Browning for testing and providing feedback through out the project
- Code Institute tutor support who helped with an issue i had with iteration of list of dictionaries.
- My Code Institute mentor Mo Shami for his guidance through this project.