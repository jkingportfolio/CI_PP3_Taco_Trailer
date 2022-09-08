# The Taco Trailer
Developer: Jamie King

![Mockup image](docs/images/home-screenshot.png)

The Taco Trailer website has been developed to provide users the chance to order food for delivery or pick-up via a command line based interface. 

[View live website](https://taco-trailer.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
    5. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    1. [Structure](#structure)
    2. [Flowchart](#flowchart)
    3. [Data Models](#data-models)
4. [Technologies Used](#technologies-used)
    1. [Coding Languages](#coding-languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
5. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Implementations](#future-implementations)
6. [Testing](#testing)
    1. [Python Valiadation](#python-validation)
    2. [Device Testing](#device-testing)
    3. [Browser Compatibility](#browser-compatibility)
    4. [Testing User Stories](#testing-user-stories)
    5. [Automated Testing](#automated-testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
    1. [Tutorial](#tutorials)
    2. [Code](#code)
    3. [Literature](#literature)
    4. [Misc](#misc)
10. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Be able to easily interact with the app to order food for pick up or delivery.
- Navigate the app seamlessly.
- Receive clear instructions on their current input options.
- Be provided with negative and postive feedback based on their inputs.
- Be able to remove items from an order or cancel the order prior to submission.
- The ability to create an account.
- The ability to change account password.

### Site Owner Goals

- Provide potential customers an easy to use app to order food from The Taco Trailer.
- Include an admin area in which information intended for staff only can be accessed. 
- As the site owner i wanted to secure the admin area of the app with a password.
- Have the ability to view previous orders that had been placed.
- Have the ability to view current pending orders that have yet to be picked up or delivered.
- Ensure all user inputs are validated as to not provide issues with orders and a negative user experience.

## User Experience

### Target Audience

- People looking to have food ordered for delivery.
- People looking to pick up food from the store.

### User Requirements and Expectations

- The ability to seamlessly navigate through the app.
- To use an app that provides feedback to the user.
- To have validation that inputs have been successfully entered.
- Personalisation in the form of a user login with saved details.

### User stories

1. As a user, I want to be provided with clear instructions throughout the app.
2. As a user, I want to be able to create an account.
3. As a user, I want to be able to log into my account.
4. As a user, I want to be able to change my account password.
5. As a user, I want to be able to chose between order pick up or delivery.
6. As a user, I want to be able to change current order address if the stored one is incorrect.
7. As a user, I want to be able to view the menu.
8. As a user, I want to be able to add items to my order.
9. As a user, I want to be able to remove items from my order.
10. As a user, I want to be able to preview an order.
11. As a user, I want to be able to cancel an unplaced order.
12. As a user, I want to be able to place an order.
13. As a user, I want to be shown a receipt.
14. As a user, I want to be able to exit the app.


### Site Owner Stories

15. As the site owner, I would want users to be greeted with a welcome message to give a friendly feel to the app.
16. As the site owner, I would want to be able to access a password locked admin area.
17. As the site owner, I would want to be able to access all previous order records.
18. As the site owner, I would want to be able to access a list of pending orders.
19. As the site owner, I would want the registered users information to be saved to a google sheets file.
20. As the site owner, I would want orders to be saved to a google sheets file. 
21. As the site owner, I would want the user to get feedback in the case of invalid input.

### User Manual

## Technical Design

### Structure

This app was designed using Code Institutes Python Essentials Template. The template creates a command line interface within a blank page with a run button located above the command line interface. As this project is only intended for use on large screen devices there was no need to incorporate responsivness to the page. On arrival to the page, the user will be presented with a welcome message and instructions on user input choices. 

### Flowchart

A flowchart was created during the design process to help identify functions that would be required in the Python files.

<details>
<summary>Flow Chart</summary>
<img src="docs/js-logic-flow-annotated.jpg">
</details>

### Data Models

This project uses Object Orientated Programming to interact and manipulate the following:

- Classes - This project uses two classes. The first class called 'User' is used to create an instance of a new user based on inputs and append the details to a Google Sheets file. The second class called 'Order' is used to create an instance of an order based on inputs and then display the receipt of the order and append the order details to a Google Sheets file.
- Lists and dictionaries - This project uses list and dictionaries to aid the storage of data from the Google Sheets file to variables and vice versa. Using list comprehension dictionaries are used to validate if a new user name is not already, the user input for ordering an item exists and to store/view order records.
- Google Sheets API - Google Sheets was used in this project to store all required data outwidth the container and provide a level of security in user name and passwords.

## Technologies Used

### Coding Languages
- Python 3 - Used to create the command line based app.

### Frameworks and Tools
- Balsamiq - Used to create wireframes.
- Git - Used for version control.
- GitHub - Used to deploy the projects code.
- Gitpod - Used to develop and test code.
- LibreOffice Draw - Used to create the game logic flowchart.
- Eightshapes - Used to check colours for contrast and accessibility.

### Libraries

## Features

In its entirety the website consists of one main page, with a mock terminal within that page to run The Taco Trailer app. <>

### Existing features

#### <> 

The <> is featured on the main page and will <>

<details>
<summary>Flow Chart</summary>
<img src="docs/js-logic-flow-annotated.jpg">
</details>

- Covered in user story: <>


### Future implementations

In the future as my skills grow I would like to implement the following features:

- <>
    - <>
    - <>
- <>
    - <>

## Testing

### Python Validation

[PEP-8 Validation](http://pep8online.com/) was used to validate the Python code used in the app. <>

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
<summary>Python file - taco_trailer_command_line.py</summary>
<img src="docs/validation-js/validation-jshint-contact.png">
</details>
<details>
<summary>Python file - user.py</summary>
<img src="docs/validation-js/validation-jshint-contact.png">
</details>

### Device Testing

As this app is only intended to be used on desktops the website was tested on the following devices:
- Windows 10 PC with a 24" MSI Curved gaming monitor
- Raspberry Pi 4 with a 24" MSI Curved gaming monitor

In addition to testing on physical devices, <>

### Browser Compatibility

The website was tested on the following web browsers:
- Google Chrome (Version 104.0.5112.102)
- DuckDuckGo

### Testing User Stories

#### Users

1. As a user, I want to be provided with clear instructions throughout the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |     |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-1.png">
</details>

2. As a user, I want to be able to view the menu.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-2.png">
</details>

3. As a user, I want to be able to add items to my order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  |  |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-3.png">
</details>

4. As a user, I want to be able to remove items from my order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |  |
|  |  |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-4.png">
</details>

5. As a user, I want to be able to preview an order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |     |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-5.png">
</details>

6. As a user, I want to be able to cancel an unplaced order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-6.png">
</details>

7. As a user, I want to be able to place an order.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |  |
|   |   |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-7.png">
<img src="docs/testing-user-stories/testing-user-stories-7.1.png">
</details>

8. As a user, I want to be shown a receipt.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |  |   | |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-8.png">
</details>

9. As a user, I want to be able to exit the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |  |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-9.png">
</details>

#### Site Owner

10. As the site owner, I would want users to be greeted with a welcome message to give a friendly feel to the app.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|  |  |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-10.png">
</details>

11. As the site owner, I would want to be able to access a password locked admin area.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |   |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-11.png">
</details>

12. As the site owner, I would want to be able to access all previous order records.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-12.png">
</details>

13. As the site owner, I would want to be able to access a list of pending orders.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|   |   |    |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-13.png">
</details>

14. As the site owner, I would not want the user to have to restart the app due to bugs in the code.

| Feature       | Action        | Expected Result  | Actual Result |
| ------------- | ------------- | -------------    | ------------- |
|      |    |      |  |

<details>
<summary>Screenshots</summary>
<img src="docs/testing-user-stories/testing-user-stories-14.png">
</details>

### Automated Testing

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
2. Once logged in navigate to the desired [GitHub Repository](https://github.com/jkingportfolio/CI_PP3_Taco_Trailer) that you would like to fork.
3. At the top right corner of the page click on the fork icon.
4. There should now be a copy of your original repository in your GitHub account.

Please note if you are not a member of an organisation on GitHub then you will not be able to fork your own repository.

### Clone a GitHub Repository

You can make a local clone of a repository via the following steps: 

1. Navigate to www.github.com and log in.
2. Once logged in navigate to the desired [GitHub Repository](https://github.com/jkingportfolio/CI_PP3_Taco_Trailer) that you would like to clone.
3. Locate the code button at the top, above the repository file structure.
4. Select the preferred clone method from HTTPS. SSH or GitHub CLI then click the copy button to copy the URL to your clipboard.
5. Open Git Bash
6. Update the current working direction to the location in which you would like the clone directory to be created.
7. Type `git clone` and paste the previously copied URL at Step 4.
8. `$ clone https://github.com/jkingportfolio/CI_PP3_Taco_Trailer`
9. Now press enter and the local clone will be created at the desired local location

## Credits

### Tutorials

- <>
- <>
- <> - [<>](https://www.w3schools.com/howto/howto_css_modals.asp)

### Code

 Code from external sources were used as a basis and built on top of in this project, they are credited below:

 - <> [<>](https://github.com/kubowania/connect-four)
 - <> [<>](https://animista.net/)

### Literature

The use of reference books were used throughout the creation of this project and are credited below:

- Python Crash Course by Eric Matthes, published by No Startch Press
- Learn Python Programming by Fabrizio Romano & Heinrich Kruger, published by Packt Publishing
- Python Object-Orientated Programming - Fourth Edition by Steven F. Lott & Dusty Phillips, published by Packt Publishing

### Misc

The source of where I learned how to produce a GitHub fork and clone was from the following pages of the GitHub Documentation. Although I did not use a fork or clone in this project it is something I hope to implement to future projects now I have the knowledge to do so.

- https://docs.github.com/en/get-started/quickstart/fork-a-repo
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository


## Acknowledgements

I would like to also thank the following:
- My wife and family for their support and feedback whilst doing this project
- My fellow Code Institute students whom i have bounced ideas and problems back and forth with via Slack
- [Carina Browning](https://github.com/carinaAJ) for testing and providing feedback through out the project
- Code Institute tutor support who helped with an issue i had with iteration of list of dictionaries.
- My Code Institute mentor Mo Shami for his guidance through this project.