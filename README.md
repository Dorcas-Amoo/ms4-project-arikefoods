# Welcome to Arike Foods!

![Page Screenshot](media/arikefoods.jpg)


## [Visit Site](https://ms4-project-arikefoods.herokuapp.com/)

## Table of Contents
1. [Project Description](#description)
2. [User Experience & Design](#ux)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits & References](#credits--references)


## Project Description
The idea of creating this project was born from my desire to start an online restaurant business and influenced by a few recipe and restaurant sites I had visited. I have an in-born passion for good cooking and I enjoy seeing people being served with excellence in that regard. 

The idea of this online restaurant is help reduce the burden of many who do not enjoy cooking or who many not have the time to do their own cooking due to many other commitments. As we know, everyone needs to eat and having access to good food without lifting a pot would be a great advantage to many. Also, due to the present situation in the world, we see many turning to online shopping which is making many high street restaurant businesses reduntant at present. 

I believe strongly in this idea and I look forward to what it will become in the near future.

Thank you and enjoy the ride. :rocket:


## UX

This project was created to meet the needs of the everyday people. Below are some _User Stories_:

* As a potential user and customer on visiting your site, I want to be able to do the following:
  + 'Register easily.'
  + 'Once registered to receive an email confirmation.'
  + 'Securely and easily login and logout as desired.'
  + 'View a list of available meals for purchase.'
  + 'See images of some meals available for sale.'
  + 'Have a smooth user experience by easily understanding how to navigate through and use the site.'
  + 'Have a full understanding of the items available for purchase.
  + 'Have access to the price list of items.'
  + 'Easily select one or more items for purchase.'
  + 'View items in my shopping bag.'
  + 'See a summary of my purchase before checkout so as to allow for making an informed decision before purchase.'
  + 'Be able to control or edit the quantity of items I'd like to purchase.'
  + 'Get a feedback on actions as I perform them where possible.'
  + 'Make a secure payment for items I want to purchase.'
  + 'Be sure my purchase has been successful.'
  + 'Leave a review on any given meal wherever possible.'
  + 'Have access to additional features like a blog post on your menu.'
  + 'Have access to some contact details.'
  
In order to meet the requirements of the user, I began brainstorming on what to do and how to go about delivering the desired result. I decided to visit related websites, and those created by other code institute students which helped me to make an informed decision. After this, I began creating the wireframe designs of my proposed website on Balsamiq, please [see wireframes folder attached](https://github.com/Dorcas-Amoo/ms4-project-arikefoods). This helped me to really put a deeper thought into the idea, the layout, colour-scheme and many more features to be implemented. Though I am pleased with the result so far, given the scope of this project and due to time constraint, I have had to postpone some of the features I had in mind and will be implementing them in the future. 

Please kindly note that the final product may not be an exact replica of the wireframes. Thank you.

### Model Design 
The requirement of this project is to build the site with relational database models including additional two models beyond what was covered in the course tutorial. I came up with the **RecipePost and Feedback models** as my additional models. Please see the [schema folder attached](https://github.com/Dorcas-Amoo/ms4-project-arikefoods) for further information.


[Back To Table of Contents](#table-of-contents)
  

## Features
1. **Home Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The Carousel (Image Slider).
  + The Welcome message (includes links to the Recipe blog and Feedback pages).
  + The Navigation button to access Food Menu and Menu Order pages.
  + The Footer which displays the copyright content.
2. **The Food Menu Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The menu table which displays the menu details (Name, Description, Category and Price).
  + The Navigation button to the Order page.
3. **The Recipe_Blog Page (Based on additional Model 1)-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The recipe with ingredients and instructions.
  + The Navigation button back to the Home page.
4. **The Menu Order Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The Order form which has the add to cart button and quantity selection features.
  + A 'Comment' navigation button to the feedback page
  + A 'Success' message toast appears next to Cart once an item has been added successfully.
  + The Navigation button back to the Food Menu page.
5. **The Order(Cart) Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + A Navigation button to the Checkout and Payment page.
  + The Navigation button back to the Order page.
6. **The Checkout and Payment Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The Order summary and the payment form which consists of the user details and payment card details.
  + A Secure Complete Order button that saves the payment and triggers the Success page once payment is successfully processed otherwise, an error message appears to inform the     user that their card has not been charged.
  + A Navigation button back to the home page which also serves as a cancel order button.
  + Users have to be logged in to access this page.
7. **The Order Success Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + A paragraph of message indicating that the payment has been successful.
  + A Navigation button back to the home page
8. **The Feedback Page (Based on additional Model 2)-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The comment form which consists of the user's name and a submit button.
  + Users have to be logged in to access this page.
9. **The Sign Up Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The registration form which consists of the user's email, username, password, password confirmation and a submit button.
  + Email Confirmation is sent after form submission.
10. **The Sign In Page-** This contains the following:
  + The Navbar which displays the Logo (links to the homepage on click), the "Home", "Food Menu", "Sign Up", "My Account", and "Cart" links.
  + The login form which consists of the user's email, username, password, forgot password and a submit button.
  
  **Other Pages:** These consists of all other [django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) user authorisation functionalities like email           confirmation, password reset and many more.
  
  **PLEASE NOTE: For the credit card payment functionality, use 4242 4242 4242 4242 as your credit card number. However, you can use any futuristic date, security code and ZIP     code.**

### Features to be Implemented
+ The User Profile page.
+ Enable users to edit and update their profiles.
+ Add a subscription feature where users can have access to more benefits of being registered.
+ A link to the Cookbook site where users can have access to more Recipes and get more involved with the ability to add their own recipes.
+ Allowing users to save their delivery addresses, payment cards and order details.
+ Viewing of Order history.
+ To send order confirmation via email.
+ A product admin were admin can add more items to the menu.
+ To give access to the feedback page only a user who have purchased a product.
+ To ensure that when a user signs in, they are redirected to the page they were before signing in not to the homepage first.
  (This list is not exhaustive).


[Back To Table of Contents](#table-of-contents)


## Technologies Used
The following technologies were used to achieve the requirements of this project:

+ [Django](https://docs.djangoproject.com/en/3.0/) HTML templating, URL routing, Form validation, Authentication, Admin and Security.
   + A lot of the heavy lifting for achieving the website at a short space of time was done with this.
+ [Python](https://www.python.org/)
  + I used this as the backend language to help manipulate data.
+ [Heroku](https://www.heroku.com/)
  + This was used to host my website.
+ [Heroku's PostgreSQL database](https://data.heroku.com/datastores/f3ba8873-adda-49a5-bf37-ea9ddde11767/)
  + This was used to host database on cloud.
+ [Github](https://github.com/)
  + This was used as the project repository. 
+ [Gitpod](https://www.gitpod.io/) 
  + This was used to develop the site and [Git](https://git-scm.com/) for version control.
+ [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  + CSS3 was used to custom sytle my website to my desired outcome.
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
  + HTML5 was used as the markup language to structure and present my website on the Web.
+ [Javascript](https://www.javascript.com/)
  + This was used to achieve the interactive and Stripe payment part of the site.
+ [JQuery](https://www.jquery.com/)
  + These scripts from Bootstrap and the Boutique Ado Tutorial were used to initialise some features on my site.
+ [Markdown](https://www.markdownguide.org/) 
  + This was used to document the readme.
 
 **Other Frameworks & APIs Used**
 
+ [Dj-database-url](https://pypi.org/project/dj-database-url/)
  + Allows use of environment variable for database connections.
+ [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) 
  + A mobile friendly CSS framework based on a responsive grid system. Provides out of the box UI components such as navigation menu bar, carousels, forms and cards.
+ [Font Awesome](https://fontawesome.com/) 
  + This was used for all icons.
+ [Django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
  + Allows style and HTML control of Django template form displays.
+ [Stripe](https://pypi.org/project/stripe/)
  + A python library to talk to Stripe's API.
+ [Boto3](https://pypi.org/project/boto3/)
  + Allows Python to talk to AWS SDK so you can store data in S3 buckets .
+ [Django-storages] 
  + A collection of custom storage backends with django to work with boto3 and AWS S3.
+ [Gunicorn](https://pypi.org/project/gunicorn/)
  + Python WSGI HTTP Server for UNIX so you can host your application.
+ [Psycopg2](https://www.psycopg.org/docs/)
  + PostgreSQL database adapter for the Python.
+ [Pytz](https://pypi.org/project/pytz/)
  + World timezone calculations.
+ [AWS S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html)
  + Allows seamless uploading of user files to cloud storage using application credentials.
 

[Back To Table of Contents](#table-of-contents)

  
## Testing
Over the course of building this project, I encountered a few challenging **bugs** which I was able to **fix** by asking relevant questions from the Tutors, my Mentor and carrying out extensive research. This made it paramount for me to adopt the *defensive* approach and habitually carry out print test and other testings as I build the site (I made use of the **developer tool**) so as to ensure things work properly, and in addition to this, I carried out the following:

+ **Defensive Design Testing**
Implemented the folowing measures to prevent a user from making mistakes or carrying out malicious actions.
1. General form validation.
2. Stripe's security system (Influenced by Code Institute's Boutique Ado project).
3. Get_object_or_404 instances in the views.
4. User authentication before accessing certain pages. e.g The Checkout Page.

+ **Responsiveness Testing**
1. During construction, I regularly test the site against its *Responsiveness* by clicking on **Inspect** to view the *developer tool*.
2. I then checked the layout by clicking on the **Ipad, the Iphone and selected other devices to view**.
3. I also adjusted the pane to view the point at which the design changes to a mobile, tablet, laptop or desktop view.
4. This helped me to notice that some of the features were not well displayed in mobile view and prompted me implement some changes in the design.

+ **All Pages Testing**
I carried out the following tests for all pages on these devices (Mobile, tablet, laptop):
   + Once the site loads, all contents were displayed as expected.
   + I clicked on all links in the Navigation and side bars which opens the required page successfully.
   + I clicked on all buttons which acted as expected.
   + All icons behave as expected.
   + All forms stored and displays data as expected.
   + Form input validations works as expected.
   + The dropdown options work correctly.
   + The submit button on click, stores the entered data in the database as expected.
   + The cancel and other navigation buttons take you to the expected pages.
   + The Carousel images scroll as expected.
   + The copyright displays correctly on all pages.
   + Email verification was sent successfully once signed up.
   + Could not access the checkout page without being logged in.
   + Could not access the feedback page without being logged in.
   + The correct items are being added to cart once selected.
   + The success messages pops up as expected.
   + A payment intent is created in Stripe correctly and displays the total price.
   + Error message during card decline was correctly displayed.
   + The blog post was displayed as expected.
   + All menu were correctly displayed as stored in the database.
   + Comments are correctly stored in the database.
   + Order deails are correctly stored in the database.
   + Order line details were correctly stored in the database.
   + User details are correctly stored in the database.
   + Update button works as expected.
   + Able to set quantity of items as expected.
   + No items in cart message is displayed as expected when items are deleted from the cart.
   + At checkout, order summary are being displayed as expected.
   + When payment was processed successfully, checkout success is displayed as expected.
   + Cart item is set to null.
   + All other django allauth authorisation functionalities works as required.
   + Used the back button to navigate successfully.
   

+ **UX Testing**
To validate the user experience, I asked a number of my friends and family members to help. They were asked to use the site so as to help give an unbias and accurate feedback.
 
   1. They were to try using all the links to test its functionality and usability.
 
   2. They all came back with different feedbacks as follows:
     + "The site is beautiful and easy to use, a job well done!"
     + "I had a very pleasant and enjoyable experience"
     + "However, the background image clashes with the wordings on the homepage when it is scrolled" (My emphasis: This will be looked into and corrected in due course).
     + "Maybe change the "Meat Stew" to say "Beef Stew".
     + "I was able to sign up successfully and got email verification" (This was confirmed from admin section).
     + "I tried paying but I got a message on the site that my card has not been charged and when I visited the link attched to the message, I used the test card and it worked".
     
 + **Other Testings**
  + For my **HTML5 code testing**, I used [The W3C Markup Validation Service](https://validator.w3.org/)
  + For my **CSS3 code testing**, I used [The W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/)
  + For my **Javascript and JQuery code testing**, I used [JSHint](https://jshint.com/)
  + For my **Python code testing**, I used [PEP8](http://pep8online.com/)
  + For **Browsers testing**, I did not have any issues opening or viewing the site on the different browsers that was used namely: **Microsoft Edge**, **Mozilla Firefox**,          **Google Chrome**, **Safari** and other different mobile browsers, namely, **Android** and **iOS.** On all of these platforms, I had a smooth user-friendly experience.
  

[Back To Table of Contents](#table-of-contents)


## Bugs

I encountered a number of time consuming bugs in the process which made the development process more challenging. However, with constant research and tutor support, I was able to overcome the majority of them.

I encountered a lot of  ```NoReverseMatch at //, Reverse for '' with arguments'(",)' not found ```. Encountering this eventually helped me to know more about solving such errors in django as I went researching and at ther times asked for help from the tutors.

Heroku deployment was challenging but I realised I had mispelt my website name in settings.py and in gunicorn which after I made corrections, worked. However, I noticed my data were not being displayed which after asking for guidance, I was made to understand that I had to upload the data as it had not been successfully uploaded to Heroku.

I then faced a lot of challenges with uploading my data to Postgres and I had to manually add them with the guidance of tutor support.

Finally, after uploading my files unto AWS S3, my Carousel images stopped working, however the alt attribute were being displayed. I later found that I had to change the URL path for it to work. Thanks to Igor from tutor support.


## Deployment

To deploy my site, I made use of the Heroku hosting platform following this process:

1. Created a new app in Heroku
2. In the settings tab, the following environment variables configuration were set in place:
  
  - SECRET_KEY = "My secret key"
  - 
3. From the heroku dashboard of my application, I clicked on "Deploy" > "Deployment method" and selected GitHub.
4. I connected to my GitHub repository.
5. I then set the project up for automatic deployment which helped to deploy easily whenever the master branch is updated through pushing to Github.
6. To do this manually, in the deployment section, select the master branch and click 'Deploy Branch".
7. The site should then be successfully deployed.
  
To run code **locally**:
1. From [GitHub](https://github.com/), click on the "Clone" button.
2. Choose "Download Zip" (The download starts).
3. After the download is complete, open the zip folder by double clicking to access created page.
4. The page will launch on your chosen browser.
NOTE: Ensure that you have ..... downloaded on your device else this will not work. Also, install the following:
  + `pip install -r requirements.txt`.
  + For any newly added packages to the project, use `pip freeze --local > requirements.txt ` this will update the requirements.txt file with new dependencies.
  + Also ensure that a Procfile is installed for it to run on Heroku.
  

[Back To Table of Contents](#table-of-contents)
  

## Credits & References
From my research, the following made an impact in the successful completion of this project as it had been extremely challenging yet enjoyable. I have also learnt a lot from completing the project. Please kindly see links below. Thank you.

### Content

**Tutorials and Other useful resources**
+ [Code Institute for HTML, CSS, JavaScript & UX](https://courses.codeinstitute.net/program/FullstackWebDeveloper)
+ [Challenger](https://github.com/maliahavlicek/ms4_challenger)
+ [The Woodworks](https://github.com/codewouter/milestone4-the-woodworks)

### Media
The images and recipes used, and my *Wireframes* were from the following:
+ [Balsamiq](https://balsamiq.com/)
+ [QQ Lounge](https://www.qqlounge.com/)

### Acknowledgements
I got inspiration for my project from the following:
+ [Code Institute](https://courses.codeinstitute.net/program/FullstackWebDeveloper)
+ [QQ Lounge](https://www.qqlounge.com/)

My gratitude goes first to **God Almighty** for the gift of life, love and strength to see this to the end. Many thanks to my highly supportive and understanding husband, **Oluwaseun Olomofe** and to my Mentor **Dick Vlaanderen** for his guidance and sacrifices despite the challenge of time difference. Also to my brother, **Leke Amoo** and everyone else who helped to test the usability and functionality of the project and gave valuable feedbacks to assist in improving the site.

Also a huge THANK YOU to the Code Institute Team! The tutors, especially, **Michael, Roman, Igor, Scott and Sammy** for their guidance and patience and to the Student care team for their exceptional support since I started the course. Special thanks to **Neil Kavanagh, Lucy Rush and Claire Lally.**

--------

Thank you for visiting! :smile:
