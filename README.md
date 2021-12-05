<h1 align="center"> Project 4 for Code Institute formation | DieDerDas | HTML - CSS - JS - DJANGO</h1>

[View the live project here.](https://project4-german-in-color.herokuapp.com/)

DieDerDas is a website to learn the gender of German nouns with colors.

In this version, users can log in and interact with the database to enter their own set of nouns or they can use the default nouns.


This project is built as part of a project for the [code institute](https://codeinstitute.net/) (training to become a web developer). 

<h3 align="center"><img src="static/images/readme/main-readme.png"></h3>

# Table of content

[About The Project](#about-the-project) 

[Target audience](#target-audience)  

[User Experience](#user-experience)

[Features](#features)  

[Technologies used](#technologies-used)

[Tests](#tests)

[Deployment](#deployment) 

[Credits](#credits)

[Acknowledgments](#acknowledgments)


# About The Project

## Background to understand the purpose of the website
In German, nouns are associated with one of three genders: masculine, feminine or neuter.

It leads to the question: 
How do we learn which gender is associated with a noun?

## Aim of the project
Create a website to help the user learn German nouns by associating colors to the nouns.

# Target audience
Learners of German. Especially those who want to improve their knowledge of German Nouns genders and tend to use colors to learn.


# User Experience
The details of the design evolution, user project can be found **[here](UXEVOLUTIO.md)**. It includes diagrams, pictures, explanation of changes in the project process.

## User Story
The user project has been mapped in this github project under issues. 
The user stories for this project are:

<h3 align="center"><img src="static/images/readme/user-story-excel.png"></h3>

## UI Design
- ### Fonts 
Default Font from bootstrap were kept, i.e:"Helvetica Neue", Helvetica, Arial, sans-serif, because it looks nice and it is and easy to read.

- ### Colors
Colors were inspired from the hero pictures. A color picker was used in PowerPoint to take some colors codes in the picture. A dark background was used using the color #06546b; orange and Bordeaux buttons using the colors: #e75e2cc9; #5F1C29.

## Wireframes

### Home page
<details>
<h3 align="center"><img src="static/images/readme/home-page.png"></h3>
</details>

### Dashboard page
<details>
<h3 align="center"><img src="static/images/readme/Dashboard.png"></h3>
</details>

# Features 

- ### Hero Section
An image with colors was used for the hero section to illustrate the theme of the site which aims to help learn German with colors.
An animation was made on the text, where "German with Colors" becomes "Learn with colors" when the mouse passes over it. The objective is to stimulate and interest the user.

Buttons to access sub-sections of the site are placed in the hero so that the user can quickly go to the desired place on the site.

<h3 align="center"><img src="static/images/readme/Hero-section.png"></h3>

- ### How it works Section
The section explains the concept of the website without too much text to not bore the user. 

An example with animation has been created so that the user can understand the concept even without reading the text. 

The user can also customize the colors associated with each gender.
<h3 align="center"><img src="static/images/readme/How-it-works.png"></h3>

- ### Start learning Section
The user can click on the buttons to start learning. If the user is registered, he/she has the possibility to use own nouns as well as the default nouns.
<h3 align="center"><img src="static/images/readme/start-learning.png"></h3>


- ### Register, Login, Logout Section
Users can register, log in and log out to access their own dashboard.
<h3 align="center"><img src="static/images/readme/signin.png"></h3>


- ### Dashboard Section
In the dashboard, the user can have a list of tasks, edit, toogle and delete the items.
The user can also enter, edit and delete nouns.
<h3 align="center"><img src="static/images/readme/Dashboard-pic.png"></h3>

- ### Add edit delete

#### Add nouns
It is expected that a user will want to enter many nouns. Therefore, when a noun is created, the user remains on the Add noun page and can enter many nouns in a row. A return to dashboard button is present so that the user can return to the dashboard easily .
<h3 align="center"><img src="static/images/readme/add-nouns.png"></h3>

#### Add Item
It is expected that the user will not want to add many new tasks in a row. Therefore, when a ToDo item is added, the user is redirected to the dashboard with the Todo list open. This way, the user can see all ToDo items and get an overview of them.

- ### Footer
The footer was kept simple, with a sentence and an email address for contact. Since no social media was created for this project, no links were added. The email address is real and I would receive inquiries.

## Responsiveness
The website is designed to be suitable for all devices. For example, the responsive navigation bar turns into a burger button for phone screens.

## Future
- The user can add his/her own categories

- The difficulty level of the nouns

- When a noun is clicked, the card can rotate and a sentence with the noun is written to help learn the nouns in context.

    
# Technologies used
## Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  
- [js](https://en.wikipedia.org/wiki/JavaScript)  
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


## Frameworks
- [Bootstrap](https://getbootstrap.com/)

- [Django](https://www.djangoproject.com/)

- [GreenSock](https://greensock.com/)

- [jQuery](https://jquery.com/)

## Others

- [PostgreSQL](https://www.postgresql.org/) database used in development mode and database in production mode

- [Git](https://git-scm.com/) | used as version control system

- [Gitpod](https://gitpod.io/workspaces) | used to code, commit to git and push the codes to github

- [GitHub](https://github.com/) | used to store the project code, show it and deploy the website

- [Balsamiq](https://balsamiq.com/) |  used to create the wireframe

- [Powerpoint](https://simple.wikipedia.org/wiki/Microsoft_PowerPoint) | used to create images from screenshots and work with images

- [Word](https://en.wikipedia.org/wiki/Microsoft_Word) | used to correct the grammar

- [am I responsive?](http://ami.responsivedesign.is/) | used to look at the responsiveness of the website and to present an introductory picture in the readme file

- [W3C Markup Validation Service](https://validator.w3.org/) | used to check the validity of the HTML code

- [W3C CSS Validation service](https://jigsaw.w3.org/css-validator/) | used to check the validity of the CSS code

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) | used to inspect the elements, codes and to see the how the site look like on various phones and tablets

- [DeepL](https://www.deepl.com/) | used to translate words from French to English and to write the content of the website and the 'Read me' file

- [Linguee](https://www.linguee.com/) | used to translate nouns, verify the gender and get the plural of the nouns.

- [cloudinary](https://cloudinary.com/) | used to store images

- [aconvert](https://www.aconvert.com/document/xls-to-json/) and [beautifytools](https://beautifytools.com/excel-to-json-converter.php) | used to convert excel file into json format

- [Inkscape](https://inkscape.org/) | used to create the favicon


# Tests
The details of testing can be found [here](TESTING.md).


# Deployment
## GitHub Pages
The project was stored in GitHub and deployed in Heroku. Heroku Postgres was used for the database. Cloudinary to store the pictures.

## Making a Local Clone
- Log in to GitHub and locate the GitHub Repository.
- Click the Code drop down menu.
- Either download the ZIP file, unpackage locally and open with IDE OR to clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location where you want the cloned directory to be made
- Type `git clone`, and then paste the URL you copied.
- Press Enter. Your local clone will be created.
- Create a file called env.py to hold your app's environment variables, which should contain the following:
```console
import os

os.environ["DATABASE_URL"] = "app database"
os.environ["SECRET_KEY"] = "app secret key"
os.environ["CLOUDINARY_URL"] = "cloudinary URL"

```
- Make sure the following are listed in your .gitignore file to prevent any environment variables being pushed publicly:
`env.py`


### Installing required softwares
In the terminal enter 

`pip3 install -r requirements.txt`

### Applying database migrations
In the terminal enter 
```
python manage.py migrate
```
### Creating a new superuser
```
python manage.py createsuperuser
```
### Creating a Default User
To be done just after the superuser creation so the id of the Default user will be 2 (important to use the default nouns).
Can be done in Admin.

### Entering Genders
Still in Admin, Add 3 genders. It is important to keep the following order:
1- Neutral
2- Masculin
3- Feminin

### Load categories and noun data from json file (found in home --> fixtures)
- load first categories by entering in the terminal:
`python3 manage.py loaddata categories`
- Then load the nouns by entering in the terminal:
`python3 manage.py loaddata nouns`

### The app can now be run locally using
```
python manage.py runserver
```

## Heroku Deployment
- Register or login [Heroku](https://id.heroku.com/login)
- Choose a unique name for the app and the location nearest to you.
- Under **Resources** search for and add **Heroku Postgres** to your app
- In your local environment in the env.py file, enter the database URL (to find the URL, in HEROKU go to settings --> click "Reveal Config VARS")
- In Heroku, add a SECRET_KEY var (must be the same as the one in your env.py file)
- Add the hostname of your Heroku app to settings.py
```
ALLOWED_HOSTS = ['YOUR-APP-NAME.herokuapp.com', 'localhost']
```
- In Heroku, select the **Deploy** tab and under **Deployment method** choose GitHub
- In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
- under **Manual deploy** choose **Deploy Branch**

- The steps from the previous section have to be repeated to load data in the new database (can be done in the local environment):
  - Applying database migrations
  - Creating a new superuser
  - Creating a Default User
  - Entering Genders
  - Load categories and noun data from json file


# Credits

## Code credits
[code institute](https://codeinstitute.net/) - Parts of the code throughout the website have been adapted from the courses.
The main courses were: "I think Therefore I Blog"; "Hello Django"; "Boutique Ado"

[w3schools](https://www.w3schools.com/) - Used throughout the project.

[stakocverflow](https://stakocverflow.com/) - Used throughout the project.

[very Academy](https://www.youtube.com/watch?v=eC95DrKMEo8) Trick to Create Django Fixtures from Excel/CSV File.


## Read me file credits
Some parts of the readme file from [farrelleoin93](https://github.com/farrelleoin93/12-acres-beer) have been adapted to write this readme file.

## Pictures credits
The [picture in the hero section](https://pixabay.com/fr/photos/gobelins-carr%c3%a9-cercle-d%c3%a9tail-jaune-1491577/) was taken from Stux from [Pixabay](https://pixabay.com/).
The [colored brain image](https://pixabay.com/fr/illustrations/r%c3%a9seau-de-neurones-artificiels-ann-3501528/) was from ahmedgad from [Pixabay](https://pixabay.com/)

## Nouns list
The list of nouns comes mainly from the German courses I took at the IKI and IFU schools in Vienna. The genders, English translations and plurals were checked with [Linguee](https://www.linguee.com/). Themes were done manually.

# Acknowledgments
- My mentor, Nishant Kumar, for giving me the direction to start the project, for guiding me through the project, for giving me the idea to implement new features and for giving me feedback.

- Andras Raab for the suggestions to improve the design.

- The Slack community for clarifying certain concepts, sharing tips and links and, of course, for always helping me with the codes.

- The tutors in Code institutes for helping with the codes.
