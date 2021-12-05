
## Code validation
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
- [W3C Markup Validation Homepage | Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fproject4-german-in-color.herokuapp.com%2F)

- [W3C Markup Validation Login | Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fproject4-german-in-color.herokuapp.com%2Faccounts%2Flogin%2F)
- [W3C Markup Validation Register | Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fproject4-german-in-color.herokuapp.com%2Faccounts%2Fsignup%2F)
- [W3C Markup Validation Logout | Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fproject4-german-in-color.herokuapp.com%2Faccounts%2Flogout%2F)

- The Dashboard page HTML was checked by entering the code as text area and did not show error.

- [W3C CSS Validator | Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fproject4-german-in-color.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)


Javascipt code was tested using [jshint](https://jshint.com/) and no error was found with /*jshint esversion: 6 */

Python the code was passed in [PEP8 online checker](http://pep8online.com) without showing errors except for few lines in the setting.py file because some line are too long. This was for lines automatically written at the Django installation and these lines were left.

## Testing User Stories
### Learners Goals
  - As a German learner, I want to have an online tool to learn German, so that my German can improve.
    - The site offers a new way to learn German


  - As a German learner, I want to have tools to learn the specific challenges of the German learners, so that I can improve a specific area of the language
    - The website focus on learning the genders of the nouns.


  - As a person using colors to learn, I want to have tools uing colors to learn, so that I can improve by using the way my brain works naturally
    - The website offers to associate German nouns gender to colors

### First Time Visitor Goals
  -  As a First Time Visitor, I want to Easily understand the main purpose of the site, so that So that I don't lose patience on the website
      - The title DieDerDas + German with colors gives some indications about the purpose of the site and still in the Hero part, a sentence explains the purpose of the site "Learn German NAMES by associating colors with GENDERS".

  - As a First Time Visitor, I want to Easily understand how learning works, so that I start to learn quickly.
    - An animation is made to explain how the website works and in the learning section, the user can click on buttons to see how it works with default nouns.

  - As a First Time Visitor, I want to Get motivation and inspiration, so that So that I can spend more time learning what I've started to learn
    - The colorful images have been placed in a way that stimulates the user and makes them feel surrounded by color.

  - As a First Time Visitor, I want to Start playing/learning rapidly, so that I don't get distracted by anything else.
    - In the hero page, a button is placed to quickly access the learning section.

  - As a First Time Visitor, I want to Navigate the site easily, so that So that I don't lose patience on the website
    - The navigation bar is fixed so that the user can always access the link it contains. The buttons are placed in such a way as to facilitate navigation on the site.

  - As a First Time Visitor, I want to access the site from a range of devices, so that I can learn anywhere, anytime
    - The site is designed for all devices

### Returning Visitor Goals


  - As a Returning Visitor, I want to I want to be able to use my own nouns, so that I can work with the vocabulary that interests me the most
    - The user can log in to use, add, modify and delete nouns.
  - As a Returning Visitor, I want to I want to find how to contact the organisation with any questions I may have, so that So I can ask question and share feedback
    - In the footer, an email address is provided so that the user can contact the website owner.

- ### Frequent User Goals
  - As a Frequent User, I want to I want to organize my learning in the website, so that It motivates me to go there often and learn more
    - A Todo section allows the user to organize his/her work.


## Automatic testing

### Python
Some automatic python tests were conducted and can be found in home and dashboard apps.

In the app home:
  - file "test_views.py": The accesses to the home page and to the categories were tested.

In the app dashboard:
  - file "test_form.py": The forms for creating Todo Items and entering nouns were tested
  - file "test_views.py": It was tested that the dashboard cannot be accessed if the user is not logged in.
  - file "test_model.py": It was tested that when a Todo Item is created, it is by default not done and that the string of the item returns the name of the item.


## Manual testing

### Test on browsers
The website was tested on computers using the browsers:
- [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome)
- [Firefox](https://en.wikipedia.org/wiki/Firefox) 
- [internet explorer](https://en.wikipedia.org/wiki/Internet_Explorer)
- [Microsoft edge](https://en.wikipedia.org/wiki/Microsoft_Edge)
- [Safary](https://en.wikipedia.org/wiki/Safari_(software))

### Test on devices
[Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to see how the site looks like on various phones and tablets. Additionally, after deployment the website was tested on various phones: iphone11, iphone10, Samsung Galaxy A3.


### Testing the website manually
The animations were tested by moving the mouse over German in Color several times. In the section Why not with colors by watching the text change.

The color picker was tested by changing the colors several times, refreshing the page to make sure the colors stayed, and clicking on the reset default colors button.


The Backend was tested by clicking on the Die Der Das buttons, the theme button + the Die Der Das buttons. 

Creating new users and adding Names in the Dashboard, deleting and editing. 

Creating ToDo Items, editing, deleting and toggling. 

In the homepage, when the user is logged in, it has been tested that custum nouns can be used and that they are not used in the default nouns.

To ensure that the user knows they can log in, it has been verified that the user sees the status in the navigation bar.
