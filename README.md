# eCommerce: Creative Design

![Am I Responsive](readme/am-I-responsive.png)


**Developer: Sebastian Smerd**

💻 [Visit live website](https://creativedesign-1a4929c2fa0f.herokuapp.com/)  

(Ctrl + click to open in new tab)



## Table of Contents
  - [Executive Summary](#executive-summary)
     - [Market Analysis](#market-analysis)
     - [Marketing and Sales Strategy](#marketing-and-sales-strategy)
     - [Operations and Management](#operations-and-management)
     - [Financial Plan](#financial-plan)
  - [Marketing](#marketing)
     - [Social Media](#social-media)
     - [Mailing List](#mailing-list)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [AWS](#aws)
      - [Database](#database)
      - [Models](#models)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

<hr>

## Business Plan  
### Executive Summary:

Creative Design is a web-based platform that alows to order a graphical desing online. It offers a convenient and easy-to-use platform for oredring icons, posters, illustrations and other graphical designs. It also shows the current portfolio of different designs.

In terms of revenue, Creative Design will generate income through the form to order a design where a prospective client can
describe what they want and get a price automatically. The ready design can be sent to them via email.


### Market Analysis:

The graphical desin industry is a big revenue industry. The client look for graphical design on different sorts that can be purchased quickly. The clients need designs to use them in Facebook, X, Instagram, Snapchat, Pinterest and others.


### Marketing and Sales Strategy:

Teetime will utilize a combination of online and offline marketing tactics to reach our target market. These tactics will include:

Online advertising through Google AdWords and social media platforms such as Facebook and Instagram
Content marketing through our email newsletter


### Operations and Management:

Creative Dsign will be operated and managed by a small team of experienced professionals. The team will consist of mainly graphical design proffesionals.

In terms of operations, we will utilize a cloud-based platform to host the website and software such as Heroku, as well as a payment gateway for processing transactions such as Stripe. 

#### Financial Plan:

Creative Designwill generate revenue through the sale of graphical desing. In terms of expenses, the main cost will be marketing and advertising efforts to drive traffic to the website and attract customers and contracted graphical designers who will create all the designs. We will also incur expenses related to the development.

In terms of financing, Teetime will initially be funded through a combination of personal investment and a small seed round of funding. As the business grows, we will explore additional funding options such as venture capital or a larger round of financing.

In terms of projections, we anticipate steady growth in a revenue streams. There are many potential users who need graphical desings in today's online world.



##### Back to [top](#table-of-contents)<hr>

## Marketing  

### Social Media  

The web app CreativeDesign has a presence on Facebook. The Facebook page serves as a platform to promote the website, post updates on the latest features, and share the portfolio. These social media accounts allow users to stay informed and connected with the Creative Design community.

[Facebook]()  


### Mailing List  

Creative Desig uses Mailchimp to manage its mailing list. By joining the mailing list, users will receive updates on new features and exclusive promotions. The process to join the mailing list is simple, users just need to provide their email address on the website, and they will start receiving email updates. Mailchimp allows the Creative Design team to segment the mailing list, personalize emails and track the success of email campaigns. By joining the mailing list, users will stay informed and be the first to know about new developments in the Creative Design web app.  



## User Goals

- To easily and conveniently order graphical designs
- To browse a portfolio of graphical desings
- To access the latest newsletter


## Site Owner Goals

- Generate revenue through the sale of graphical desings
- Build a strong and loyal customer base by providing an easy-to-use platform
- Establish Creative Design as a trusted and respected brand 
- Achieve profitability and sustain long-term growth
<hr>


## User Experience

### Target Audience

There are many individual users and companies that need graphical design in today's online world. They use them in a plethore of social media platforms. The website allows them to order a design with a few keystrokes and get in on their email.

### User Requirements and Expectations

- A user-friendly interface: Users will expect the app to be easy to navigate and use, with clear and concise instructions for ordering a design.
- Reliability: Users will expect the app to be reliable and function smoothly, without any errors or technical issues.
- Security: Users will expect their personal and financial information to be secure when using the app, and will expect the app to have appropriate measures in place to protect their data.
- Competitive prices: Users will expect the prices for graphical designs to be competitive with other options available on the market.
- Good customer service: Users will expect the app to have good customer service, including responsive and helpful support in the event of any issues or questions.
- Accessibility

##### Back to [top](#table-of-contents)<hr>


## User Stories


| User Story ID                  | As A/AN             | I CAN...                                                | SO THAT I CAN...                                          |
|--------------------------------|---------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Registration and User Accounts ||||
| 1 | Site User | register for an account | have an account and view my profile |
| 2 | Site User | login and logout | have an account with my information stored for fast usage |
| 3 | Site User | recover my password | set a new password if I forgot it                         |
| 4 | Site User | receive an email confirmation after registration| be notified registration was successful                   |
| 5 | Site User | have a profile | store my information for faster checkouts in the future |
| Viewing and navigation ||||
| 6 | Site User | navigate across the site | can access all parts of the site                          |
| 7 | Site User | be notified of my actions | be aware the action was completed successfully or not     |
| 8 | Site User | see my login status | know if I am logged in or not |
| 9 | Site User | visit the website| view protfolio |
| 10| Site User | can oder a graphical design and pay be a credit card| can order a praphical design of their choice|
| 11 | Site User | use a card as the payment method | complete my purchase                                      |
| 12 | Site User | receive order confirmation | be notified of a successful order |
| Admin and Store Management | | | |
| 13 | Store Owner / Admin | add a protfolio design | add new designs to the website |
| 14 | Store Owner / Admin | edit a portfolio design | edit existing portfolio designs on the website |
| 15 | Store Owner / Admin | delete a portfolio design | delete existing portfolio design from the website |



##### Back to [top](#table-of-contents)<hr>

## Wireframes
I used Balsamiq to create wireframes for my project. It's a user-friendly wireframing tool that enables me to quickly and easily create mockups for my website or application. It offers a wide range of pre-built UI elements, and allows for easy collaboration with my team. I linked a pdf of my wireframes, which you can access it and check it out the design, layout and the flow of the project before implementing it in the real product.  

<a href="https://github.com/ArronBeale/CI_PP5_tee_time/raw/main/docs/wireframes/wireframes-teetime.pdf" target="_blank">Download Wireframes PDF</a>  
(Ctrl + click to open in new tab)  

<details><summary>Wireframe Home</summary>  

![Wireframe Home](readme/balsamiq-1.png)

</details>



<details><summary>Wireframe Checkout</summary>  

![Wireframe Checkout](readme/balsamiq-2.png)

</details>



<details><summary>Wireframe Portfolio</summary>  

![Wireframe Home](readme/balsamiq-3.png)

</details>

<hr>

## Design

### Colors

The colours are minimalistic: white, grey and black.

### Fonts

 The font selected was from Google Fonts, Lato.

<hr>

# Structure

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

It contains an email sign up form and useful links as well as contact information.

## Website pages

- The site consists of the following pages:
  - Home, Add a Quote
  - Order Details
  - Checkout and Payment page
  - Portfolio pages
  - Add, edit and delete portfolio pages - Design Management
  - My Profile pages
  - List and details of orders
  - Login
  - Logout
  - Reset Password
  - Register
  - 404

  ##### Back to [top](#table-of-contents)
  <hr>

## AWS 

I am using AWS S3 buckets to store my data. S3 is a highly scalable and durable cloud storage service provided by Amazon Web Services. It allows me to easily store and retrieve large amounts of data, and its built-in security features provide added protection for my files. I chose S3 for its scalability, durability, and security features.

<hr>


## Database

I built my database using PostgreSQL. It's a powerful and open-source object-relational database system that is known for its reliability, robustness, and performance. I chose it because it provides a flexible tool for efficiently managing and organizing my data.

<details><summary>Erd Diagram</summary>  

![Erd Diagram](readme/erd-diagram.png)

</details>

## Models  

### User Model

| Key        | Name         | Type        |
| ---------- | ------------ | ----------- |
| PrimaryKey | user_id      | AutoField   |
|            | password     | VARCHAR(45) |
|            | last_login   | VARCHAR(45) |
|            | is_superuser | BOOLEAN     |
|            | username     | VARCHAR(45) |
|            | first_name   | VARCHAR(45) |
|            | last_name    | VARCHAR(45) |
|            | email        | VARCHAR(45) |
|            | is_staff     | BOOLEAN     |
|            |              |             |
|            | is_active    | BOOLEAN     |
|            | date_joined  | VARCHAR(45) |

### User Profile Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | user_profile_id      | AutoField     |
| ForeignKey | user                 | User model    |
|            | default_phone        | CharField[20] |
|            | default_email        | CharField[40] |



### Design Model

| Key        | Name        | Type           |
| ---------- | ----------- | -------------- |
| PrimaryKey | product_id  | AutoField      |
|            | name        | CharField[50]  |
|            | description | TextField      |
| ForeignKey | category    | Category model |
|            | image       | ImageField     |

### Category Model  

| Key        | Name          | Type      |
| ---------- | ------------- | --------- |
| PrimaryKey | category_id   | AutoField |
|            | name          | Char[254] |
|            | friendly_name | Char[254] |

### Order Model  

| Key        | Name            | Type               |
| ---------- | --------------- | ------------------ |
| PrimaryKey | order_id        | AutoField          |
|            | order_number    | CharField[40]      |
|            | category        | CharField[254]     |
|            | description     | TextField[254]     |
|            | size            | CharField[32]      |
| ForeignKey | user_profile    | User profile Model |
|            | name            | CharField[50]      |
|            | email           | EmailField[254]    |
|            | phone           | CharField[20]      |
|            | date            | DateTimeField      |
|            | total           | DecimalField[10]   |
|            | stripe_pid      | CharField          |

### OrderLineItem Model  

| Key        | Name             | Type            |
| ---------- | ---------------- | --------------- |
| PrimaryKey | OrderLineItem_id | AutoField       |
| ForeignKey | order            | Order Model     |
| ForeignKey | product          | Product Model   |
|            | product_size     | CharField[2]    |
|            | quantity         | IntegerField    |
|            | line_item_total  | DecimalField[6] |


##### Back to [top](#table-of-contents)
<hr>



## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](https://ui.dev/amiresponsive/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v4](https://getbootstrap.com/)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [AWS](https://aws.amazon.com/)
- [jQuery](https://jquery.com)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

##### Back to [top](#table-of-contents)


## Features  


### Search Engine Optimisation (SEO)
I have used meta tags in the HTML of my web app's pages to optimize them for search engines. The description tag provides a brief summary of the content on the page, while the keywords tag lists relevant keywords to help search engines understand the content of the webpage and its relevance to related search queries.



### Home page
- Home page includes nav bar, main body and a newsletter.


<details><summary>See feature images</summary>

![Home page](readme/home.png)
</details>  



### Navigation
- Fully Responsive.
- On small screens switches to hamburger menu.
- displayed on all pages.  

<details><summary>See feature images</summary>

![Navigation](readme/navigation.png)
</details>



### Mailing List Sign Up
- Mailchimp signup for email mailing list.  

<details><summary>See feature images</summary>

![Mailing](readme/newsletter.png)
</details>


### Sign up / Register
- Allow users to register an acoount.

<details><summary>See feature image</summary>

![Signup](readme/register.png)
</details>


### Sign In
- User can sign in.  

<details><summary>See feature images</summary>

![Signin](readme/signin.png)
</details>


### Sign Out
- Allows the user to securely sign out.
- Ask user if they are sure they want to sign out.  

<details><summary>See feature image</summary>

![Sign out](readme/logout.png)
</details>  


### Alert Box
- Allows the user to see relevant alerts.  

<details><summary>See feature image</summary>

![Alert](readme/alert.png)
</details>  


### Portfolio design
- Allows the user to view the listed designs.  

<details><summary>See feature image</summary>

![Designs](readme/designs.png)
</details>  

 

### Search
- Allows the user to search for designs.  

<details><summary>See feature image</summary>

![Search](readme/search.png)
</details>  



### Quote
- Allows the user to get a quote.  

<details><summary>See feature image</summary>

![Quote](readme/quote.png)
</details>  


### Checkout
- Allows the user to purchase designs  

<details><summary>See feature image</summary>

![Checkout](readme/checkout.png)
</details>  


### Stripe
- Allows the user to use stripe for card payments.  


<details><summary>See feature image</summary>

![Stripe](readme/stripe.png)
</details>  


### Email Confirmation
- Allows the user to receive an email confirmation for their order.  

<details><summary>See feature image</summary>

![Email Confirmation](readme/confirmation.png)
</details>  


### Profile
- Allows the user to update their information and see their order history.  


<details><summary>See feature image</summary>

![Profile](readme/profile.png)
</details>  


### Add Design to the portfolio
- Allows the Admin to add new products.  

<details><summary>See feature image</summary>

![Add Product](readme/add_design.png)
</details>  


### Edit Design
- Allows the user to edit the designs.  

<details><summary>See feature image</summary>

![Edit Product](readme/edit_design.png)
</details>  


### Delete Design
- Allows the user to delete products, includes confirmation prompt before deletion.  


<details><summary>See feature image</summary>

![Delete Product](readme/delete_design.png)
</details>  




##### Back to [top](#table-of-contents)<hr>

# Validation  

## HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website.  

### Home  

index.html [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com) 
- Two Errors Found


![Errors](readme/checker.png)

 ### Home, Quote, Checkout, Designs, Add Design, Edit Design, Sign Up, Log in, Log out

Home [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com) 
Quote [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/quote) 
Checkout [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/checkout) 
Designs [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/designs) 
Add design [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/designs/add) 
Edit design [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/designs/edit/1) 
Profile [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/profile) 
SignUp [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/accounts/signup) 
Log in [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/accounts/login) 
Log out [results](https://validator.w3.org/nu/?doc=https://creativedesign-1a4929c2fa0f.herokuapp.com/accounts/logout) 



- Two Errors Found in navigation. Not sure what they are as the navigation is taken from the bootstrap documentaiton.


![Errors](readme/checker.png)

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.

base.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcreativedesign-1a4929c2fa0f.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 

profile.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcreativedesign-1a4929c2fa0f.herokuapp.com%2Fprofile%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 

checkout.css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcreativedesign-1a4929c2fa0f.herokuapp.com%2Fprofile%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) 


### JavaScript Validation
JSHint javaScript Validation Service was used to validate all javaScript files.

<details><summary>stripe_elements.js</summary>  
<img src="readme/jshint_stripe.png">
</details>  

- some undefined variable Stripe which originates from a external script


##### Back to [top](#table-of-contents)<hr>  

## PEP8 Validation
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code for PEP8 requirements.


<summary>Home</summary>

<details><summary>forms.py</summary>
<img src="readme/home_forms.png">
</details>

<details><summary>basket_tools.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-tools.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-views.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-test-views.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-urls.PNG">
</details>

<hr><summary>Blog</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-views.PNG">
</details>

<hr><summary>Bookings</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-models.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-test-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-urls.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-test-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-views.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-test-views.PNG">
</details>

<hr><summary>checkout</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-forms.PNG">
</details>  

<details><summary>test-forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-test-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-models.PNG">
</details>

<details><summary>test-models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-test-models.PNG">
</details>

<details><summary>signals.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-signals.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-views.PNG">
</details>  

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-test-views.PNG">
</details>  

<details><summary>webhook_handler.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-webhook-handler.PNG">
</details>  

<details><summary>webhook.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-webhooks.PNG">
</details>  

<hr><summary>contact</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-forms.PNG">
</details>

<details><summary>test-forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-test-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-models.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-test-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-views.PNG">
</details>

<hr><summary>home</summary>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-home-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-home-views.PNG">
</details>

<hr><summary>products</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-admin.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-models.PNG">
</details>

<details><summary>test-models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-test-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-views.PNG">
</details>  

<details><summary>test-views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-test-views.PNG">
</details>  

<details><summary>widgets.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-widgets.PNG">
</details>

<hr><summary>profiles</summary>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-views.PNG">
</details>  

<hr><summary>teetime</summary>

<details><summary>asgi.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-asgi.PNG">
</details>

<details><summary>settings.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-settings.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-views.PNG">
</details>  

<details><summary>wsgi.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-wsgi.PNG">
</details>

<hr><summary>root</summary>

<details><summary>custom_storages.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-root-custom-storages.PNG">
</details>  

##### Back to [top](#table-of-contents)<hr>  

## Accessibility  
The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/ was used to ensure the website met high accessibility standards.  
- All pages returned 0 errors.  
- All alerts presented were for redundant links whichweres taken into account duringdevelopmentt.

<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-home.PNG">
</details>  

<details><summary>Golf Clubs</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-golf-clubs.PNG">
</details>  

<details><summary>Club Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-club-expand.PNG">
</details>  

<details><summary>Booking List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-booking-list.PNG">
</details>  

<details><summary>Edit Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-edit-booking.PNG">
</details>  

<details><summary>Cancel Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-cancel-booking.PNG">
</details>  

<details><summary>Product List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-product-list.PNG">
</details>  

<details><summary>Product Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-product-expand.PNG">
</details>  

<details><summary>Add Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-add-product.PNG">
</details>  

<details><summary>Edit Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-edit-product.PNG">
</details>  

<details><summary>Basket</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-basket.PNG">
</details>  

<details><summary>Checkout</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-checkout.PNG">
</details>  

<details><summary>Checkout Success</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-checkout-success.PNG">
</details>  

<details><summary>Blog</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-blog.PNG">
</details>  

<details><summary>Blog Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-blog-expand.PNG">
</details>  

<details><summary>Contact</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-contact.PNG">
</details>  

<details><summary>Profile</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-profile.PNG">
</details>  

<details><summary>Sign Up</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-sign-up.PNG">
</details>  

<details><summary>Sign In</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-sign-in.PNG">
</details>  

<details><summary>Sign Out</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-log-out.PNG">
</details>  

<details><summary>404</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-404.PNG">
</details>  

##### Back to [top](#table-of-contents)<hr>  

## Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-home.PNG">
</details>

<details><summary>Sign Up</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-sign-up.PNG">
</details>

<details><summary>Sign In</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-login.PNG">
</details>

<details><summary>Sign Out</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-logout.PNG">
</details>

<details><summary>Golf Clubs</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-golf-clubs.PNG">
</details>

<details><summary>Club Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-club-expand.PNG">
</details>

<details><summary>Booking List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-booking-list.PNG">
</details>

<details><summary>Edit Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-edit-booking.PNG">
</details>

<details><summary>Cancel Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-cancel-booking.PNG">
</details>

<details><summary>Product List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-product-list.PNG">
</details>

<details><summary>Product Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-product-expand.PNG">
</details>  

<details><summary>Add Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-add-product.PNG">
</details>  

<details><summary>Edit Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-edit-product.PNG">
</details>  

<details><summary>Basket</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-basket.PNG">
</details>  

<details><summary>Checkout</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-checkout.PNG">
</details>  

<details><summary>Checkout Success</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-checkout-success.PNG">
</details>  

<details><summary>Blog</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-blog.PNG">
</details>  

<details><summary>Blog Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-blog-expand.PNG">
</details>  

<details><summary>Contact</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-contact.PNG">
</details>  

<details><summary>Profile</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-profile.PNG">
</details>  

##### Back to [top](#table-of-contents)<hr>


## Testing

1. Manual testing User Stories
2. Automated testing

### Manual testing

1.	As A/AN Shopper / Site User	I CAN register for an account	SO THAT I CAN have an account and view my profile  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sign Up | Click pofile button and select register, user is brought to the sign up page| User is brought to the sign up page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01b.PNG">
</details>  

2.	As A/AN Shopper / Site User	I CAN login and logout SO THAT I CAN have an account with my information stored for fast usage  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sign In | Click pofile button and select login, user is brought to the sign in page | User is brought to the sign in page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-02-b.PNG">
</details>  

3.	As A/AN Shopper / Site User	I CAN recover my password	SO THAT I CAN set a new password if I forgot it  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Reset Password | Click pofile button and select login, user is brought to the sign in page, click forgot password to go to password reset page | User is brought to password reset page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-02-b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-03b.PNG">
</details>  

4.	As A/AN Shopper / Site User	I CAN receive an email confirmation after registration	SO THAT I CAN be notified registration was successful  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Registration | Upon registration an email is sent to verify the email address submitted | Registration email arrives into inbox of the email address used to sign up | Works as expected  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-04b.PNG">
</details>  

5.	As A/AN Shopper / Site User	I CAN have a profile SO THAT I CAN store my information for faster checkouts in the future  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Profile | From the Nav click the profile icon, select profile from dropdown and be broought to the profile page where user information is stored | Be brought to profile page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-05.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-05b.PNG">
</details>  

6.	As A/AN Shopper / Site User	I CAN navigate across the site 	SO THAT I CAN can access all parts of the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar | Click on any link in the navbar to be brought to a relevant page, shop for example | Be brought to shop to view all products after clicking all products in the navbar | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-02-b.PNG">
</details>  

7.	As A/AN Shopper / Site User	I CAN use a navbar, footer, and social icons  SO THAT I CAN navigate the site, access menus, and access socials  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar/Footer | Scoll to footer, click on the Instagram logo | A new tab will open and bring user to the Teetime Instagram page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-07.PNG">
</details>  

8.	As A/AN Shopper / Site User	I CAN be notified of my actions	SO THAT I CAN be aware the action was completed successfully or not  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Alert Box | Add an item from the shop to the basket | A message will appear in the alert box on screen to notify the user of this action | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-08a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-08b.PNG">
</details>  

9.	As A/AN Shopper / Site User	I CAN see my login status	SO THAT I CAN know if I am logged in or not  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navigation | While logged out the profile icon in the navbar will be gray, log in it will change to a green color | Once logged in the profile icon will be green | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
</details>  

10.	As A/AN Shopper / Site User	I CAN visit the shop SO THAT I CAN view all products available  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Shop | Click shop in the navbar, select all products | User is then brought to the all products page of the shop | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-10.PNG">
</details>  

11.	As A/AN Shopper / Site User	I CAN view my basket and total cost at any time	so I am aware of what I am buying and it's cost  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Basket | Click the basket icon in the navbar | User is brought to the basket page where all products in basket are displayed along with their price and total cost | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-11a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-11b.PNG">
</details>  

12.	As A/AN Shopper / Site User	I CAN view a list of products	SO THAT I CAN select a product to purchase  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Categories | Select a category on the side panel, select Gents Polos     |     User is brought to the selected category of product and all products are listed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-12.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-12b.PNG">
</details>  

13.	As A/AN Shopper / Site User	I CAN view an individual product details SO THAT I CAN view a more detailed view of the product  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Product Detail | Click on any item image in the shop, or the view button     |  User is borught to the product detail page where product details are displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-13.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-13b.PNG">
</details>  

14.	As A/AN Shopper / Site User	I CAN view a list of golf courses	SO THAT I CAN select a golf course I want to play on  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs |  From the navbar click Clubs | User is brought to the Golf Clubs List page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-14b.PNG">
</details>  

15.	As A/AN Shopper / Site User	I CAN view individual golf course details	SO THAT I CAN see more detailed information about it  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Club Details | From the Golf Clubs List page select a club and click the view golf club button | User is brought to the details page for the selected golf club | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-15.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-15b.PNG">
</details>  

16.	As A/AN Shopper / Site User	I CAN view a list of tee times available for each golf course	SO THAT I CAN select a date and time to play  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Book a Tee Time | From golf club details page find the book a teetime form on the page, select a club, date and time | User is then brought to a confirmation page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-16.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-16b.PNG">
</details>  

17.	As A/AN Shopper / Site User	I CAN search for a product by name or description	SO THAT I CAN find a certain product 
 
| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Search | Search box in the navigation bar, input keyword to search such as "blue", click search | All items with the relevant keyword will be displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-17a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-17b.PNG">
</details>  

18.	As A/AN Shopper / Site User	I CAN see my search results	SO THAT I CAN only see what I am searching for  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Search | Input a keyword into the search box in the navbar and click search | All items matching the search critearia are only displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-18a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-18b.PNG">
</details>  

19.	As A/AN Shopper / Site User	I CAN sort by category SO THAT I CAN select products of a certain category  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sort | From the shop page, click a category on the side panel such as headwear | User is brought to the headwear page where only products classed as headwear are displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-19a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-19b.PNG">
</details>  

20.	As A/AN Shopper / Site User	I CAN sort by price low to high and high to low	SO THAT I CAN view products according to my budget 
 
| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sort | From the shop page, click the sort box and select price from high to low | All items will be sorted from the highest price to the lowest price | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-20.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-20b.PNG">
</details>  

21.	As A/AN Shopper / Site User	I CAN select only available dates/times	SO THAT I CAN I can only purchase available tee slots  

- The format used was unique together which checks that the selected date, time and club booking is unique, if the user selects a date, time and club already booked they will get a message asking them to select another time/date. Ideally I plan to remove the unavailable times from the dropdown to avoid the user clicking and going through the process to be told to select another time/date. Time constraints was the main isssue.

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Book a tee time | From golf club detail page, select a date and time for selected club | If time is available a confirmation page will appear, if the time is already booked an error message will appear asking the user to select another time. | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-21.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-21b.PNG">
</details>  

22.	As A/AN Shopper / Site User	I CAN use a card as the payment method SO THAT I CAN complete my purchase  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Checkout | From the basket select secure checkout | Input user information, input card number 4242 4242 4242 4242 04/24 424 24242, payment is successful | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-22.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-22b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-22c.PNG">
</details>  

23.	As A/AN Shopper / Site User	I CAN select the size and quantity of a product	SO THAT I CAN select a size and quantity to my needs  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Product Details | From Product details page select a size for the product in the size box, increase or decrease quantity from the quantity box | Sizes will be selected and quantity adjusted | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-23.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-23b.PNG">
</details>  

24.	As A/AN Shopper / Site User	I CAN view items in my basket	SO THAT I CAN be aware of what I am buying and it's cost  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Basket | Click the basket icon in the navbar | The basket page will appear and display all items in the basket and their cost alongside total price for all items | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-24a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-24b.PNG">
</details>  

25.	As A/AN Shopper / Site User	I CAN adjust item quantity in my basket	SO THAT I CAN increase or reduce item count according to my needs  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Basket | From the basket press the increase/ decrease button to desired number, click update | The basket will update with the desired quantity | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-24b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-25b.PNG">
</details>  

26.	As A/AN Shopper / Site User	I CAN receive order confirmation SO THAT I CAN be notified of a successful order  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Alert Box | Upon a successful checkout an alert box will be visible to the user | Alert box pops up with the order details | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-25b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-26.PNG">
</details>  

27.	As A/AN Shopper / Site User	I CAN receive email confirmation SO THAT I CAN have a record of my purchased28	Store Owner / Admin	add a product	add new products to the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Email Confirmation | Upon a successful checkout a confirmation email will be sent to the provided email address which contains the details of the order |     Email confirmation arrives into inbox | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-27.PNG">
</details>  

28.	As A/AN Store Owner / Admin	I CAN add a product SO THAT I CAN add new products to the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Add Product | From the navbar select the profile button as an admin logged in, click add product from the dropdown | The add product page will appear allowing the addition of a new product via the add product form | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-28a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-28b.PNG">
</details>  

29.	As A/AN Store Owner / Admin	I CAN edit a product SO THAT I CAN edit existing products in the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Edit Product | From product detail as an admin account, find a edit button on the page, click edit | Admin is brought to the edit product page where they can adjust any part of the product | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-29a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-29b.PNG">
</details>  

30.	As A/AN Store Owner / Admin	I CAN delete a product SO THAT I CAN delete existing products from the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Delete Product  | From product detail as an admin account, find a delete button on the page, click delete | A modal pops up and asks the admin to confirm they wish to delete the product | Works as expected |  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-29a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-30b.PNG">
</details>  

31.	As A/AN Store Owner / Admin	I CAN add a golf club	SO THAT I CAN add a golf club to the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs | In the url address go to https://ci-pp5-teetime.herokuapp.com/admin/, log in as admin and select clubs in the side panel to the left, the clubs screen will appear and then click add club button on the top right of the screen. Add club page will appear | Add club page will appear and the user can then add information for a new golf club | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-admin-login.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31c.PNG">
</details>  

32.	As A/AN Store Owner / Admin	I CAN edit a golf club SO THAT I CAN edit an existing golf club on the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs | In the url address go to https://ci-pp5-teetime.herokuapp.com/admin/, log in as admin and select clubs in the side panel to the left, the clubs screen will appear and then click a club that you desire to edit. The club page will appear allowing the user to edit information | The club page will appear and the user can then edit information for the golf club             | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-admin-login.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-32b.PNG">
</details>  

33.	As A/AN Store Owner / Admin	I CAN delete a golf club SO THAT I CAN delete existing golf club from the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs | In the url address go to https://ci-pp5-teetime.herokuapp.com/admin/, log in as admin and select clubs in the side panel to the left, the clubs screen will appear, select the club using the checkbox and cick the action dropdown above, choose delete selected clubs and press go | The club will be deleted | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-admin-login.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-33b.PNG">
</details>  

34.	As A/AN Store Owner / Admin	I CAN add a tee time SO THAT I CAN add a tee time to a golf club  
- Time constraints did not allow this to happen, the path chosen was to preload the standard tee times for golf clubs to cover all times during the year.

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Future Feature | N/A | N/A |

35.	As A/AN Store Owner / Admin	I CAN edit a tee time	SO THAT I CAN edit an existing tea time on a golf club 
- Time constraints did not allow this to happen, the path chosen was to preload the standard tee times for golf clubs to cover all times during the year. 

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Future Feature | N/A | N/A |

36.	As A/AN Store Owner / Admin	I CAN delete a tee time	SO THAT I CAN delete a tee time from a golf club  
- Time constraints did not allow this to happen, the path chosen was to preload the standard tee times for golf clubs to cover all times during the year.

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Future Feature | N/A | N/A |


### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report


<details><summary> Basket, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-basket-test-views.PNG">
</details>

<details><summary> Bookings, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-bookings-test-views.PNG">
</details>

<details><summary> Bookings, test-models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-bookings-test-models.PNG">
</details>

<details><summary> Bookings, Test-urls</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-bookings-test-urls.PNG">
</details>  
<details><summary> Checkout, test-forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-checkout-test-forms.PNG">
</details>

<details><summary> Checkout, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-checkout-test-models.PNG">
</details>

<details><summary> Checkout, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-checkout-test-views.PNG">
</details>

<details><summary> contact, forms</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-contact-test-forms.PNG">
</details>  
<details><summary> Contact, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-contact-test-models.PNG">
</details>

<details><summary> Contact, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-contact-test-models.PNG">
</details>

<details><summary> Products, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-products-test-models.PNG">
</details>

<details><summary> Products, test-views</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-products-test-views.PNG">
</details>  

### Coverage  
A Python test plugin called coverage was used to generate the following results and display how much of the code was covered by the unittest module.

<details><summary> Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-coverage-01.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-coverage-02.PNG">
</details>


### Device Testing & Browser compatibility

The site uses to test on various real world devices was [BrowserStack](https://www.browserstack.com/)  

This allowed me to test on real devices and not just device emulators.

The following devices were used to test my site:

<details><summary>Apple iPhone 12</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-iphone-12.PNG">
</details>

<details><summary>Samsung Galaxy S21</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-galaxy-s21.PNG">
</details>

<details><summary>Mozilla Firefox (v105 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-firefox.PNG">
</details>

<details><summary>Google Chrome (v106 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-chrome.PNG">
</details>

<details><summary>Safari (Monteray v15.3 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-safari.PNG">
</details>

<details><summary>Microsoft Edge</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-edge.PNG">
</details>


##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| Bookings made for same club, date and time | UniqueTogether was used to ensure no double bookings could be made |
| Increment and decrement product queantity in basket not working | Increment and decrement buttons being linked to jQuery script solved this |
| Webhooks not working | Endpoint was not fully configured, adding the correct settings resolved this |
| Payment intent not being created | Both local and deployed endpoints had incorrect initial settings which was corrected and allowed the payment intent to succeed |



##### Back to [top](#table-of-contents)<hr>

## Deployment  
### AWS S3 Bucket Setup  

To set up an AWS S3 bucket:

1. Sign in to the AWS Management Console and open the Amazon S3 console.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-01b.PNG">
</details>

2. Click on the "Create Bucket" button.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-02.PNG">
</details>

3. Enter a unique name for your bucket, and select the region where you want the bucket to be located.
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-03a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-03b.PNG">
</details>

4. Configure any additional options, such as versioning, object-level logging, and object tagging, as needed.  

5. Click on the "Create" button to create the bucket.

6. Set up the appropriate permissions for the bucket, such as access control lists (ACLs) and bucket policies, to control who can access the data in the bucket.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-06a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-06b.PNG">
</details>

7. Upload files to the bucket using the AWS S3 console, the AWS S3 CLI, or the AWS S3 SDK.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-07a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-07b.PNG">
</details>

8. Access your files through the AWS S3 Console, AWS S3 CLI, or the AWS S3 SDK.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-08.PNG">
</details>  

### Stripe Endpoint

1. Register for a Stripe account at stripe.com
2. Log into your Stripe account and navigate to the Developers section  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-02a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-02b.PNG">
</details>  

3. In the Developers section, locate the API keys section and take note of the publishable and secret keys  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-03a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-03b.PNG">
</details> 

4. Create environment variables in your local environment and on Heroku, such as STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY, with the values of the publishable and secret keys  

5. Return to the Developers section of your Stripe account and click on the Webhooks tab  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-05a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-05b.PNG">
</details> 

6. Create a webhook with the URL of your website, such as https://example.com/checkout/wh/  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-06a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-06b.PNG">
</details> 

7. Choose the events you want to receive, such as payment_intent.payment_failed and payment_intent.succeeded  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-07a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-07b.PNG">
</details> 

8. Take note of the key generated for this webhook  

9. Create an environment variable, such as STRIPE_WH_SECRET, with the value of the webhook secret key on your local environment and Heroku  

10. Test the webhook to ensure it is working properly and troubleshoot any issues that may arise.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-10.PNG">
</details> 

### Heroku  

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-01.PNG">
</details>

2. Create an app, give it a name for such as ci-pp4-the-diplomat, and select a region
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-02.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-03.PNG">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-04.PNG">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-18.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-17.PNG">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-05.PNG">
</details>

4. Create a Procfile with the text: web: gunicorn the_diplomat.wsgi
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-06.PNG">
</details>

5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a seperate test database.
I store mine in env.py
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-07.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-08.PNG">
</details>

6. Ensure debug is set to false in the settings.py file
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-09.PNG">
</details>

7. Add localhost, and ci-pp4-the-diplomat.herokuapp.com to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-pp4-the-diplomat
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-19.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-10.PNG">
</details>


15. Ensure the following environment variables are set in Heroku
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-11.PNG">
</details>

16. Connect the app to GitHub, and enable automatic deploys from main if you wish
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-13.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-14.PNG">
</details>

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>


## Credits

### Code  
- Code Institute for the bag and checkout app as a basis for my checkout and basket apps
- Code Institute Slack community for guidance on many of my bug fixes.

### Media
[Pexels](https://www.pexels.com/)

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- My Mentor Mo Shami for his excellent guidance and valuable advice  
- Code Institute Slack Community
- Code Institute Tutor Support