<h1 align="center">Fine Spirits :cocktail: | Milestone :four: Project </h1>

### [View live project here](https://fine-spirits.herokuapp.com/)

### [Main README.md file](/README.md) ###

### Testing User Stories from User Experience (UX) Section

-   #### Anonymous user/ First time visitor Goals:

    1. xxx.

        1. xx.
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/navbar.png">
           </details>
        2. xx.
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/cards.png">
           </details>
        3. xxx. 
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/footer.png">
           </details>

    2. xxx.

        1. xx. 
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/play_card.png">
           </details>
        2. xx.
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/login_card.png">
           </details>

    3. xxx.

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/registered_and_anonymous.png">
           </details>

    4. xx

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/hover_footer_links.gif">
           </details>

-   #### Registered user/ returning/ frequent visitor goals

    5. xx

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/score_dates.png">
           </details>
        2. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/crud/image_crud_functions.png">
           </details>

    6. xx

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/cards.png">
           </details>

    7. xx
        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/score_dates.png">
           </details>

    8. xx
        1. xx
           <details><summary></summary>
           <img src="docs/testing/validators/ux_stories/score_dates.png">
           </details>

    9. xx
        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/footer.png">
           </details>
    
    10. xx
        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/footer.png">
           </details>
       

-   #### Admin Goals

    11. xx

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/delete_user.gif">
           </details>

    12. xx

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/edit_questions.png">
           </details>

    13. xx

        1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/admin_power.png">
           </details>

-   #### Site Owner Goals, Testing

     14. xx

         1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/home.gif">
           </details>

     15. xx

         1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/footer.png">
           </details>

     16. xx

         1. xx
           <details><summary>xxe</summary>
           <img src="docs/testing/validators/ux_stories/home.gif">
           </details>

     17. xx

         1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/footer.png">
           </details>

     18. xx

         1. xx
           <details><summary>Evidence</summary>
           <img src="docs/testing/validators/ux_stories/footer.png">
           </details>

## User testing 
Friends and family members were asked to review the site and documentation to point out any feedback and possible way of improving it. Their helpful advice throughout the process led to many UX changes in order to create a better experience, especially regarding the styling. 

It was through this testing that the following changes were made:
- Assessing the combinations of colours and the related contrast.
- Fonts choice looking smart and not invasive.
- Overall balance in the positioning and sizing of elements in the pages.

## Manual Testing  :wrench:

### Common Elements Testing
Manual testing was conducted on the following pages in order to assess responsiveness,functionality and usability:

- Hovering over the Navbar will trigger `hover` effect.
  <details><summary>Navbar hover</summary>
    <img src="docs/testing/validators/ux_stories/hover_navbar.gif">
  </details>

- Hovering over Social links will trigger `hover` effect and clicking on them will open a new tab. 
  <details><summary>Hover and open new tab</summary>
    <img src="docs/testing/validators/ux_stories/hover_footer_links.gif">
  </details>

- Clicking on the logo will take you back to the home page or refresh it.
  <details><summary>Click logo to return to home page</summary>
    <img src="docs/testing/validators/ux_stories/back_homepage_logo.gif">
  </details>

- Hovering over the email in the footer will trigger `hover` effect and clicking on them will redirect you to the email (mailto).
  <details><summary>Mailto</summary>
    <img src="docs/testing/validators/ux_stories/mailto.gif">
  </details>

### Home Page
Manual testing was conducted on the following elements of the [Home Page](home.html):

 - All the elements are responsive (header, footer, cards).
 - The buttons in the Navbar turns into smaller buttons ordered in the same way.
   <details><summary>Home Page</summary>
    <img src="docs/testing/validators/ux_stories/home_responsiveness.gif">
  </details>
 
### Login Page
Manual testing was conducted on the following elements of the [Login Page](login.html):

 - All the elements are responsive (header, footer, central window).
 - The buttons in the Navbar turns into smaller buttons ordered in the same way.
   <details><summary>Login page</summary>
    <img src="docs/testing/validators/ux_stories/login_responsiveness.gif">
  </details>

### Registration Page
Manual testing was conducted on the following elements of the [Registration Page](registration.html):

 - All the elements are responsive (header, footer, central window).
 - The buttons in the Navbar turns into smaller buttons ordered in the same way.
   <details><summary>Registration page</summary>
    <img src="docs/testing/validators/ux_stories/registration_responsiveness.gif">
  </details>

### 404 Page
Manual testing was conducted on the following elements of the [404 Page](404.html):

 - All the elements are responsive (header, footer, text).
 - The buttons in the Navbar turns into smaller buttons ordered in the same way.
   <details><summary>404 Page</summary>
    <img src="docs/testing/validators/ux_stories/404_responsiveness.gif">
   </details>

## Automated Testing  :wrench:

### Code Validation
- The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML` code used.

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
home.html | Passed, No errors found | [Results](xx)
login.html | Passed, No errors found | [Results](xx)
registration.html | Passed, No errors found | [Results](xx)
404.html | Passed, No errors found | [Results](xx)

<br>

### CSS Validation Service
- The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the `CSS` code used.

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
style.css | Passed, No errors found | [Results](xx)

<br>

### JSHint
- The [JS Hint](https://jshint.com/) service was used to validate the `JS` code used.

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
script.js | 0 errors | [Results](xx)
admin.js | 0 errors | [Results](xx)

<br>

### PYlint
- [PYlint](https://www.pylint.org/) was used to validate the `PYTHON` code used.

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
app.py | 0 errors | [Results](xx)

<br>

### PEP8 Online Check
- [PEP8 Online](http://pep8online.com/) was used to analyse the `PYTHON` file.

Page | Result | Test Detail/Screenshot
------------ | ------------- | -------------
app.py | 0 errors | [Results](xx)
<br>

### Browser Validation
- I have used [Lambda Test](https://www.lambdatest.com/) for cross-browser testing among the major browsers. 
- [Click here to check browser testing](docs/testing/browser_testing)

- **Microsoft Edge**: Website and user stories work as expected. 
- **Google Chrome**: Website and user stories work as expected. 
- **Safari**: Website and user stories work as expected.
- **Firefox**: Website and user stories work as expected. 

<br>

### Lighthouse Auditing
- I have used [Lighthouse](https://developers.google.com/web/tools/lighthouse) to test the performance, seo, best practices and accessability of the site

Page | Test Detail/Screenshot
------------ | -------------
home.html | [Results](xx)
login.html | [Results](xx)
registration.html | [Results](xx)
404.html | [Results](xx)

<br>

### AWS Testing
- The image uploaded by the logged in user in the app has been successfully added in the S3 bucket.
   <details><summary>Evidence</summary>
    <img src="docs/deployment/aws/aws_image_uploaded.png">
   </details>

<br>

### Bugs found during the testing phase

Bug no. | Bug description |  Bug fix |
------------ | ------------- | ------------- | 
1 | The biggest trouble i had was trying to work out why the app (successfully deployed) on Heroku would not run| After several days of consulting the specific documentation i was suggested to go and check the settings. I neglected to add:  <code>PORT 5000</code>  and  <code>IP 0.0.0.0</code>.
2 | Semicolons left in the app.py by mistake | They have been promptly removed as they were giving error warnings.
4 | External links would not open in another tab | Problem solved by adding <code>target="_blank"</code> attribute to the anchor tags.
10 | app.py code issues| A fair amount of time has been spent at the end of the project to make the PY code fully PEP8 compliant.

<br>

### CRUD Features (Creation, Reading, Updating and Deleting) evidence

 - <strong>Creation - </strong> xx
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/crud_create.png">
  </details>

 - <strong>Reading - </strong> xx
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/crud_read.png">
  </details>

 - <strong>Updating - </strong> xx
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/crud_edit.png">
   </details>

 - User <strong>Updating - </strong> xx
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/image_crud_functions.png">
   </details>


 - <strong>Deleting - </strong> xx
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/crud_delete.png">
   </details>

 - User <strong>Deleting - </strong> xx
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/image_crud_functions.png">
   </details>

<br>

### Other Features

 - <strong>Already existing username - </strong> If the username already exists, the user is advised.
   <details><summary>Evidence</summary>
    <img src="docs/testing/other_features/existing_user.png">
  </details>

 - <strong>Welcome message - </strong> The registered user can see his name on the page.
   <details><summary>Evidence</summary>
    <img src="docs/testing/other_features/personalised_message.png">
  </details>

 - <strong>Hover effect - </strong> Both the admin and any user always trigger a hover effect that helps with clicling onto the right button.
   <details><summary>Evidence</summary>
    <img src="docs/testing/other_features/hover_admin.gif">
  </details>

 - <strong>Adding profile image - </strong> The logged in user can add the profile image to his/her page. A the moment it is a simple page where the image gets uploaded, just to show the functionality for learning purposes. In the future could be developed into a proper profile page.
   <details><summary>Evidence</summary>
    <img src="docs/testing/crud/image_crud_functions.png">
  </details>

### Security Features Considered

#### General
- Use of <code>.gitignore</code> to hide all secret keys.
- Only the default DJANGO insecure key has been pushed to github. Later on, after delpyingonto heroku, a new secure key has been generated, inserted into the env.py file which has been as well secured from pushing thanks to the .gitignore file.
- Hypertext Transfer Protocol Secure (HTTPS) for the Heroku App.
#### App
- Only the <strong>ADMIN</strong> has some privileges, such as:
  - Add/Edit/Remove Questions.
  - Delete users.
  - Change privileges to the registered users.

***