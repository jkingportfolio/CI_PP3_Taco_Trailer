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

- A user would want to be able to easily interact with the app to order food.
- A user would want to state if order is for pick up or delivery.
- A user would want to be able to navigate the app seamlessly.
- A user would want to be given clear instructions on their current input options.
- A user would want to be provided negative and postive feedback based on their inputs.
- A user would want to be able to remove items from an order or cancel the order prior to submission.

### Site Owner Goals

- As the site owner i wanted to be able to give potential customers an easy to use app to order food from The Taco Trailer.
- As the site owner i wanted to have an admin area in which i could access information intended for staff only. 
- As the site owner i wanted to secure the admin area of the app with a password.
- As the site owner i wanted to have the ability to view previous orders that had been placed.
- As the site owner i wanted to have the ability to view current orders that have yet to be picked up or delivered.
- As the site owner i wanted to have all user inputs validated as to not provide issues with orders.

## User Experience

### Target Audience

- People looking to have food ordered for delivery.
- People looking to pick up food from the store.

### User Requirements and Expectations

- The ability to seamlessly navigate through the app.
- To use an app that provides feedback to the user.
- To have validation that an order has been placed.
- To view a receipt of the order with all relevant details such as time order and ordered items presented in an easy to read format.

### User stories

1. As a user, I want to be provided with clear instructions throughout the app.
2. As a user, I want to be able to view the menu.
3. As a user, I want to be able to add items to my order.
4. As a user, I want to be able to remove items from my order.
5. As a user, I want to be able to preview an order.
6. As a user, I want to be able to cancel an unplaced order.
7. As a user, I want to be able to place an order.
8. As a user, I want to be shown a receipt.
9. As a user, I want to be able to exit the app.

### Site Owner Stories

12. As the site owner, I would want users to be greeted with a welcome message to give a friendly feel to the app.
13. As the site owner, I would want to be able to access a password locked admin area.
14. As the site owner, I would want to be able to access all previous order records.
15. As the site owner, I would want to be able to access a list of pending orders.
16. As the site owner, I would not want the user to have to restart the app due to bugs in the code. 

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
|   |   |     |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-1.png">
</details>

2. As a user, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-2.png">
</details>

3. As a user, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  |  |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-3.png">
</details>

4. As a user, I want to be <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |  |
|  |  |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-4.png">
</details>

5. As a user, I want to be <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |     |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-5.png">
</details>

6. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-6.png">
</details>

7. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |  |
|   |   |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-7.png">
<img src="docs/testing-user-stories/testing-user-stories-7.1.png">
</details>

8. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   | |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-8.png">
</details>

9. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-9.png">
</details>

10. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  |  |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-10.png">
</details>

11. As a user, I want to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |   |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-11.png">
</details>




12. As the site owner, I want users to be able to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-12.png">
</details>


13. As the site owner, I want to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-13.png">
</details>

14. As the site owner, I would want the user to <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|      |    |      |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-14.png">
</details>

15. As the site owner, I would not want the user to have to result in using the browser back button to navigate back to the site if a 404 error occurs.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |     |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-15.png">
</details>

16. As the site owner, I would want users to be <>.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |     |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-16.png">
</details>

17. As the site owner, I want users to be greeted with a welcome message to give a friendly feel to the site.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |   |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-17.png">
</details>


## Bugs

### Code Bugs

During the project i encountered a number of bugs some of which were solved some of which were not as stated below:

| Bug           | Fix           |
| ------------- | ------------- |
|   |  |
|   | | 
|   |  |
|   |  |
|  |  |
|   |  |

### Console Bugs

| Bug           | Reason           |
| ------------- | ---------------- |
|  | |
| |

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