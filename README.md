#  Granite Tap

Granite Tap is a B2C e-commerce store selling locally sourced beer from breweries located in Aberdeen and Aberdeenshire, Scotland.

Granite Tap is your go-to online platform for discovering and enjoying an exquisite selection of locally brewed beers from the vibrant and thriving beer scene in Aberdeen and Aberdeenshire, Scotland. We take pride in connecting beer enthusiasts with the finest creations of local breweries, offering a unique taste of the region's craft beer culture.

The site is aimed at users who are looking to expand on their beer tastes. Rather than buying the same old, run of the mill beer from the supermarkets, users can experience a whole new world of beer and see what the North East of Scotland has to offer.

The site name "Granite Tap" is a nod to Aberdeen's nickname. Due to Aberdeen's locality to natural granite deposits and the use of Granite throughout the city's buildings, Aberdeen is also know as "The Granite City". 

Users can view different types of beer from different breweries, get information on each product and make purchases through an easy to use payment system.

The payment system uses [Stripe](https://stripe.com/gb). 

***As this site is for educational purposes, please do not use real debit/credit card details whilst using the site.***

Take a look though the live project - [Granite Tap](https://granite-tap-d7fc252cb5b2.herokuapp.com/)

![Image of Am I Responsive](static/screenshots/0_amiresponsive.png)

---

- [Granite Tap](#granite-tap)
  * [Features](#features)
    + [Header](#header)
    + [Main Navigation](#main-navigation)
    + [Delivery Banner](#delivery-banner)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [Products Page](#products-page)
    + [Product Detail Page](#product-detail-page)
    + [Shopping Bag](#shopping-bag)
    + [Checkout](#checkout)
    + [Order Confirmation](#order-confirmation)
    + [My Profile](#my-profile)
    + [Wishlist](#wishlist)
    + [About Page](#about-page)
    + [Product Management](#product-management)
  * [User Experience (UX)](#user-experience--ux-)
    + [User Stories](#user-stories)
    + [Agile Methodology](#agile-methodology)
    + [Design](#design)
    + [WireFrames](#wireframes)
    + [Database Schema](#database-schema)
    + [Defensive Design](#defensive-design)
  * [Business Model](#business-model)
    + [Marketing Strategy](#marketing-strategy)
      - [SEO](#seo)
      - [Email marketing](#email-marketing)
      - [Content Marketing](#content-marketing)
      - [Social Media Marketing](#social-media-marketing)
  * [Testing](#testing)
    + [Manual Testing](#manual-testing)
    + [Code Validation](#code-validation)
    + [Device Testing](#device-testing)
    + [Browser Tesing](#browser-tesing)
    + [Bug Fixes](#bug-fixes)
  * [Project Set Up and Deployment](#project-set-up-and-deployment)
    + [Project Set Up](#project-set-up)
    + [Deployment](#deployment)
  * [Languages](#languages)
  * [Credits/References](#credits-references)
    + [Code](#code)
    + [Frameworks, Libraries and Technologies](#frameworks--libraries-and-technologies)
    + [Images](#images-1)
    + [General](#general)
    + [ReadMe Documentation](#readme-documentation)
    + [Acknowledgements](#acknowledgements)

---

## Features

### Header

![This is an image of the site header](static/screenshots/2_header.png)
- The header is present on every page of the site giving users full navigation at all times.

#### Logo

![This is an image of the site logo](static/screenshots/3_logo.png)

- The logo for the site is a simple text logo generated within the html using the Victor Mono google font.
- The logo  links to the home page and is situated in the top left corner of the header.

#### Search Bar

![This is an image of the searchbar](static/screenshots/4_searchbar.png)

- The search bar is displayed at the top of the page, always accessible to the user.
- When a user inputs a peice of text, the results will return any product in which the product title or description holds.

#### About Icon

![this is anm image of the about icon in the header](static/screenshots/5_about_icon.png)

- The About icon links to the About Us page where the user can find information on Granite Tap, FAQs, newsletter sign up and a contact form.

#### My Account Icon

##### Unauthenticated Users

![This is an image of the My Account icon in the header](static/screenshots/6_my_account_icon.png)

- The My Account icon, when clicked, will reveal a dropdown menu consisting of two options.
  - Register
  - Login

![This is an image of the My Account dropdown menu in the header](static/screenshots/7_my_account_dropdown.png)

##### Authenticated Users

![This is an image of my account icon in the header](static/screenshots/8_my_account_icon_testuser.png)

- If the user is authenticated, "My Account" text will be replaced by the users username they chose when registering for the site.
- This gives the user a visual indication that they are logged in to their account.
- When clicked, a dropdown menu is revealed to the user, consisting of links to My Profile, Wishlist and Logout.

![This is an image of the authenticated users My account dropwdown menu](static/screenshots/9_my_account_testuser_dropdown.png)

#### Shopping Bag Icon

![This is an image of the shoppping bag icon in the header](static/screenshots/10_shopping_bag_empty.png)

- The Shopping Bag icon links the users to the shopping bag page where users can view what products, if any are in there ready to be purchased.
- Beneath the Shopping Bag icon displays the total cost of their shopping bag and can be seen at all times so users can keep track of how much they are spending.

---

### Main Navigation

![This is an image of the Main Navigation bar used in the site](static/screenshots/11_main_nav.png)

- The Main Navigation bar consists of three dropdown menus for the users to access the products list.

#### All Products

![This is an image of the All Products dropdown menu](static/screenshots/12_all_products_dropdown.png)

- The All Products dropdown menu displays four options for the user to filter the site products by:
    - By Price
    - By Rating
    - By Category
    - All Products

##### By Price

- The By Price option returns to the user the full product list in ascending order of price (lowest to highest).

##### By Rating

- The By Rating option will return to the user the full product list in descending order (highest to lowest).

##### By Category

- The By Category option will return to the user the full product list of beer type in alphabetical order.

##### All Products

- The All Products option will return to the user the full product list.


#### Beer Types

![This is an image of the beer types dropdown menu in the main nav](static/screenshots/13_beer_types_dropdown.png)

- The Beer Types dropdown menu displays four options for the user to filter the products by their beer type:
    - Lager
    - Ale
    - Stout
    - Sour

##### Lager

- The Lager option will return to the user all the different type of Lager in the product list.

##### Ale

- The Ale option will return to the user all the different type of Ale in the product list.

##### Stout

- The Stout option will return to the user all the different type of Stout in the product list.

##### Sour

- The Sour option will return to the user all the different type of Sour in the product list.

#### Breweries

![This is an image of the Breweries dropdown menu](static/screenshots/14_breweries_dropdown.png)

- The Breweries dropdown menu displays four options for the user to filter the products by their brewery:
    - Brewdog
    - Brew Toon
    - Fierce
    - Six° North


##### Brewdog

- The Brewdog option will return to the user all the different beer produced by Brewdog in the product list.

##### Brew Toon

- The Brew Toon option will return to the user all the different beer produced by Brew Toon in the product list.

##### Fierce

- The Fierce option will return to the user all the different beer produced by Fierce in the product list.

##### Six° North

- The Six° North option will return to the user all the different beer produced by Six° North in the product list.

---
### Delivery Banner

![This is an image of the delivery banner](static/screenshots/16_delivery_banner.png)

- The delivery banner is located beneath the main navigation.
- The delivery banner indicates to users that if they spend more than £30 on their order, the delivery is free.

---

### Footer

![This is an image of the footer](static/screenshots/15_footer.png)

- The footer is displayed on all pages of the site.
- The footer contains links to various features on the site.

#### Contact Us

- The Contact Us link will direct the user to the contact for on the About Page

#### Subscribe to our Newsletter

- The Subscibe to our Newsletter link will direct the user to the newsletter sign up on the about page

#### Visit us on Facebook

- The Visit us on Facebook link will direct the user to Facebook Login page on a new tab.
- As the Granite Tap site is for educational purposes, the Granite Tap Facebook buisness page has been deactivated.
- To view screenshots of the Granite Tap Facebook business page, please see the Granite Tap Web Marketing section.

#### Privacy Policy

- The Privacy Policy link will direct users to the [Granite Tap Privacy Policy](https://www.termsfeed.com/live/6ce57fb3-3e55-4587-9ed0-703fd41df7f0) on a new tab.

---

### Home Page

![This is an image of the home page](static/screenshots/1_homepage.png)

- The background image of the home page is a of a hand holding a glass whilst pouring a beer from a bar tap.
- When entering the site, the user will be greeted with a simple message indicating that they are about to begin an exploration of the beer from the Northeast of Scotland.
- Beneath the welcome message, is a "Shop Now" button alllowing users to jump straight into exploring the products list.

---

### Products Page

- Users can access the products page from the main nav or the "Shop Now" button as documented above.

![This is an image of the products page](static/screenshots/17_products_page.png)

- When a users enters the product page, displayed will be the beer products they have filtered.

#### Product Count

![This is an image of the product count on the product page](static/screenshots/20_product_count.png)

- The product page displays a product count of how many products come under any specific filter. This gives the user an indication of how many products of that type there are.

#### Product Page Filtering

![This is an image of the sorting dropdown menu](static/screenshots/21_sorting_dropdown.png)

- Much like the All Products dropdown menu in the Main Navigation, users can also use the "Sort by..." dropdown menu to filter the results as they see fit.

![This sia an image of the Sort By dropdown menu](static/screenshots/22_sortby_dropdown.png)

- Users can filter the products page using various options.

##### Filtering options

- Price (Low to High)
- Price (High to Low)
- Rating (Low to High)
- Rating (High to Low)
- Name (A-Z)
- Name (Z-A)
- Category (A-Z)
- Category (Z-A)

#### Product Page Details

![This is an image of the product list with its details](static/screenshots/18_product_list_details.png)

- Users will be able to see various details around each product.

![This is an image of a single product within the product list](static/screenshots/19_product_list_single_product.png)

- Each product has specific information attached:
    - Product Image
        - The product image is a link to the product details page
    - Product Price
    - Product ABV percentage
    - The Brewery that manufactures the product.
        - This is a link to the brewery product list
    - The Beer Type
        - This is a link to the beer type product list
    - Product Rating

---

### Product Detail Page

- When a user clicks on a product from the product page they are directed to the Product Detail page.

#### Product Specific Details

![This is an image of the product detail page](static/screenshots/23_product_detail_page.png)

- Within the product detail page, users can find product specific details:
    - Product Image
    - Product Name
    - Product Price
    - Brewery
    - Beer Type
    - Product Rating
    - Product Description
    - Volume of Conatiner
    - ABV percentage

#### Wishlist Button

![This is an image of the wishlist button](static/screenshots/24_product_detail_wishlist_button.png)

- Users can add products to a wishlist and come back to purchasing them at a later date.

#### Quantity

![This is an image of the quantity button in the product detail page](static/screenshots/25_product_detail_quantity_button.png)

- Users can adjust the quantity of the product they want to add to their shopping bag.
- This can be done by either manually typing in the quantity or using the +/- buttons on either side of the input.

#### Adding Products to the Shopping Bag

![This is an image of the Add to Bag button](static/screenshots/26_product_detail_add_to_bag.png)

- When users have decided they want to add the product to their shopping bag, they can click the "Add to Bag" button.

##### Add to Bag Success Message

![This is an image of the add to bag success message](static/screenshots/27_add_to_bag_toast_message.png)

- Once a product has been added to the shoppping bag, a success message is displayed.
- This message contains: 
    - A message confirming which product has been added.
    - The bag content which is scrollable.
    - The bag total.
    - A message informing the user how much more they need to spend if they want to take advantage of free delivery.
    - A button directing the user to the shopping bag.

#### Keeping Shopping Button

![This is an image of the keep shopping button](static/screenshots/28_product_detail_keep_shopping_button.png)

- Within the Products Detail page, there is also a "Keep Shopping" button. 
- If the user want to continue shopping, they can click the "Keep shoppping" button and be redirected back to the products page.

#### You May Also Like...

![This is an image of the you may also like section](static/screenshots/29_product_detail_ymal.png)

- Beneath the product details section, a related products section has been implemented.
- This gives users the chance to view products of the same beer type and explore other breweries.
- The selection has has been randomised so everytime a user views a product, the related products will display random products of the same beer type.

---

### Shopping Bag

- Once users have completed viewing products and adding them to the bag, they can view their selections in full by clicking on the shopping bag icon or via the add to bag success message as documented above.

![This is an image os the shopping bag](static/screenshots/30_shopping_bag.png)

- In the shopping bag, users will have a view of the products they have added.
- Included information:
    - Product Info
        - Product Image
        - Product Name
        - Product SKU Code
    - Product Price
    - Quantity
    - Subtotal

#### Product Info

![This is an image of the product info in the shopping bag](static/screenshots/31_shopping_bag_product_info.png)

#### Product Price

![This is an image of the product price in the shopping bag](static/screenshots/32_shopping_bag_product_price.png)

#### Quantity

![This is an image of the Quantity input in the shopping bag](static/screenshots/33_shopping_bag_quantity.png)

- When in the shopping bag, users have the oppotunity to adjust the quantity of the number of each product in the shopping bag.
- Once the user has changed the quantity in the Quantity input, the "Update" button will action this change.
- If the user wishes, they can also remove the product from the basket entirely by using the "Remove" button.

#### SubTotal

![This is an image of the product subtotal in the shopping bag](static/screenshots/34_shopping_bag_lineitem_subtotal.png)

- The subtotal details the total of the specific line item.

#### Grand Total Details

![this is an image of the grandtotl details in the shopping bag](static/screenshots/35_shopping_bag_grand_total.png)

- At the bottom of the shopping bag, information display to the user:
    - Bag Total
    - Delivery Cost
    - Grand Total
    - A message informing the user how much more they need to spend if they want to take advantage of free delivery.

##### Keep Shopping Button

- The keep shopping button will redirect the user back to the products page if they wish to continue to browse before checking out.

##### Secure Checkout

- The Secure Checkout button will direct the user to the Checkout page to complete their purchase.

----

### Checkout

![Image of the chekout page](static/screenshots/36_checkout_page.png)

- Completing a purchases can be made through the checkout page. 
- The checkout page consists of two main features:
    - User Details
    - Order Summary

#### User Details

![image of the users details form in checkout page](static/screenshots/37_checkout_user_details.png)

- In this form, users will enter their own personal information:
    - Name
    - Email
    - Address
- Input fields marked with an asterisk are required and the user will not be able to complete their order without these fields being complete.

![image of the save info check box](static/screenshots/39_checkout_save_Info.png)

- Beneath the user details form is a checkbox to allow the user to opt to save their personal information

#### Order Summary

![image of the order summary on the checkout page](static/screenshots/38_checkout_order_summary.png)

- The order summary displays:
    - Product count
    - Item information 
    - Sub Total
    - Order Total
    - Delivery Cost
    - Grand Total


#### Payment - Stripe

![image of the stripe payment input](static/screenshots/40_checkout_payment_input.png)

- The card payment is handled by Stripe.
- This ensures a secure payment.

![image of invalid card details](static/screenshots/42_checkout_invalid_card.png)
- Invalid card details will automatically display an error message beneath the card details input.

![image of the complete order button](static/screenshots/41_checkout_complete_order_button.png)

- A warning message appear below the complete order button giving the user one final confimation before completing the order.
- Once payment details have been entered and the users completes the order, a loading screen overlay will appear indicating to the user that the payment is being processed.
- Once the payment is complete the Stripe webhook will search the database for the order and confirm that it exists.

***As this site is for eduactional purposes only, please do not enter real debit/credit card details***

***To find out more about stripe payment and how to test, please see [the Stripe documentation](https://stripe.com/docs?locale=en-GB).***

---

### Order Confirmation

![image of the checkout success page](static/screenshots/43_checkout_success.png)

- Upon completion of a successful checkout, the user is redirected to an order confirmation.
- Here, users will be able to review their order.
- Once orders are completed, it will be assigned an order number to allow users to identify one order from the other. 
- Users will also receive a confirmation email that is automaticaly generated using Django mail.

---

### My Profile

![image of the my profile page](static/screenshots/44_my_profile.png)

- Users who have signed up to the site will be able view their own profiles via the my account dropdown in the site header as documented above.
- The My Profile page consists of two main features:
    - Default Delivery Infomation
    - Order History

#### Default Delivery Information

![image of the default delivery informartion](static/screenshots/45_my_profile_delivery_info.png)

- Here, users can enter and update their own delivery information. Unlike in the checkout page, the form consists of only the users delivery details:
    - Phone Number
    - Street Address
    - Town/City
    - County
    - Postal Code
    - Country

- Users can edit this information at anytime and update using the "Update Information" button below the form.

#### Order History

![image of the order history coloumn](static/screenshots/46_order_history.png)

- The order history section gives users a short overview of any previous orders made.
- Detailed in this overview is:
    - Order Number
        - Clickable link to the order summary.
    - Date the iorder was created.
    - Items in the order.

![image of previous order page](static/screenshots/47_order_history_order_confirmation.png)

- When the user clicks the order number on the order history section of the profile page, they are redirected to the order confirmation. 
- There is also a alert messagwe displayed automatically informing the user that this is a past confirmation.
- Below the order confirmation is a "Back to Profile" button which will redirect the user bcak to the profile page.

### Wishlist

![image of the wishlist page](static/screenshots/48_wishlist.png)

- Users also have access to their own wishlist via the link in the account dropdown.
- Users can add items to their wishlist via the product detail page as documented above.
- Within the wishlist page, users can view which items they have added.
- If the user wishes to purchase the wihslist item, like the products page, the image is a clickable link to the product detail and they can add the item to the shopping bag as normal.

![image of the wishlist items details](static/screenshots/49_wishlist_detail.png)

- Much like the products page, the items within the wishlist have an overview of the product:
    - Name
    - Price
    - ABV
    - Brewery
    - Lager
    - Rating
- Below the product overview is a "Remove from Wishlist" button. This allows users to remove items from the wishlist if they no longer want or need it in there.

---

### About Page

![image of the about page](static/screenshots/50_about_page.png)

- The About page has been implemented to host several features:
    - About Us
    - FAQs
    - Newsletter Sign Up
    - Contact Us

#### About Us

- The About Us section gives users more indepth information on what the site is about.
-  This section includes small paragraphs:
    - Who We Are?
    - Our Mission
    - Join Us on This Tasting Journey
    - Explore Local Flavours
    - Convenient Home Delivery

#### FAQs

![image of the FAQs](static/screenshots/51_about_faqs.png)

- The FAQs section gives users a views of answers to common questions they may have.

![iage of the FAQs answer on display](static/screenshots/52_about_faqs_answer.png)

- The FAQs section has been styled using a Bootstrap accordian dropdown, allowing users to reveal and collapse answers as they wish.

#### Sign Up to our Newsletter

![image of the newsletter section](static/screenshots/53_about_newsletter.png)

- A newsletter sign up for has been implemented into the about page.
- This gives users an opportunity to sign up to the Granite Tap Newsletter so they can receive the latest news regarding Granite Tap and any special offers on.
- The Newsletter has been implemented using [Mailchimp](https://mailchimp.com/).

#### Contact Us

![image of the contact form](static/screenshots/54_about_contact_form.png)

- A contact form has been included in the about page.
- Users can submit details such as:
    - Name
    - Email
    - Phone Number (optional)
    - Their message, question or query
- If users have any questions or issues, they can submit the contact form which is them posted and stored in the database.
- Contact queries can be veiwed by the site admin in the Django admin.

---

### Product Management

![image of the product management page](static/screenshots/55_product_management_dropdown.png)

- Site Admin have extra access to certain features on the site. 
- One of which is Product Management. 
- Product management can be accessed by site admin users via the "My account" dropdown in the header.

#### Adding a Product

![image iof the product management page](static/screenshots/56_product_management_page.png)

- Here, Site Admin users can add products to the site database and display in the products page.. 
- Site Admin can add all relevant product imformation:
    - Product category
    - SKU Code
    - Name
    - Brewery
    - ABV
    - Description
    - Volume
    - Price
    - Rating
    - Product Image
- Once alll reelvant information has been input, Site admin users can can add the new product using the "Add Product" button.

![image of a product being added](static/screenshots/57_product_management_adding_product.png)

- Once the product is added to the site, the Site Admin user is redirected to the product detail page of the newly added product.

#### Editing/Deleting a Product

- Site Admin users can also edit and delete products.
- These buttons can be found in the product list below each product or in the product detail page of the product

![image of the edit and delete buttons](static/screenshots/58_edit_delete_button.png)

##### Editing a product

- If a Site Admin user wishes to edit a product, they can do so by clicking on the "Edit" button.
- Once clicked, the Site Admin user will be redirected to the Product management page, "Edit a product".

![image of the dit a product page](static/screenshots/59_editing_page.png)

- Much like the "Add a product" page, the form is the same except that the information is prepopulated with its information. 

- Here, Site Admin users can edit whatever pice of information they wish. 
- Once completed, The Site Admin user can click the "Edit Product" button and will be redirected back to the product detail page where the updated information is being displayed.

##### Deleting a Product

- If the Site Admin user wants to remove a product entirely from the site and database, they can click on the "Delete" button. 
- Once clicked, the item is removed from the site and the database.

#### User Accounts

##### Register/Sign Up

- The site has a sign up page for users to register for a site account.
- Users can navigate to the Sign Up page via the My Account icon in the header as documented above

![image of the sign up page](static/screenshots/86_sign_up.png)

- Here, users can enter their personal information to craete a user account.
- In order to create the account, the user will be given instructions and sent an email to their personal email account asking them to follow a link back to Granite Tap, asking them to confirm their email.

##### Login

- If Users have signed up for an account, they can login via the My Account icon in the header as documented above

![image of the login page](static/screenshots/87_login.png)

##### Logout

- Users can logout of their account via the My Account icon in the header as documented above. 
- Once logged out, users will be redirected to the Home Page.

![image of the logout page](static/screenshots/88_logout.png)

---

## User Experience (UX)

This who visit the Granite Tap will most likely those interested in purchasing beer products from the Aberdeen/Aberdeenshire area.

### User Stories

#### EPIC | Viewing Products

- As a **SITE USER** I can **VIEW A LIST OF PRODUCTS** so that **I CAN SELECT WHICH ITEM I WANT TO TO BUY**
- As a **SITE USER** I can **VIEW INDIVIDUAL BEER PRODUCT DETAILS** so that **I IDENTIFY AND UNDERSTAND WHAT THE PRODUCT IS AND IF IT IS SUITABLE FOR ME**
- As a **SITE USER** I can **VIEW THE PRODUCT IMAGE** so that **I CAN DIFFERENTIATE BETWEEN PRODUCTS**

#### EPIC | Registration and User Accounts

- As a **SITE USER** I can **REGISTER FOR AN ACCOUNT** so that **I CAN HAVE A PERSONAL ACCOUNT AND VIEW MY PROFILE**
- As a **SITE USER** I can **LOGIN/LOGOUT OF MY ACCOUNT** so that **I CAN ACCESS MY PERSONAL INFORMATION**
- As a **SITE USER** I can **HAVE A PERSONAL USER PROFILE** so that **I CAN VIEW MY PERSONAL INFORMATION AND ORDER HISTORY**
- As a **SITE USER** I can **RECEIVE AN EMAIL CONFIRMING MY REGISTRY OF MY SITE ACCOUNT** so that **I CAN VERIFY MY ACCOUNT HAS BEEN CREATED**
- As a **SITE USER** I can **RECOVER MY PASSWORD INCASE I FORGET** so that **I CAN ACCESS MY ACCOUNT**


#### EPIC | Sorting and Filtering

- As a **SITE USER** I can **SORT THROUGH A LIST OF AVAILABLE PRODUCTS** so that **I CAN IDENTIFY THE BEST RATED, BEST PRICED PRODUCTS IN A SPECIFIC CATEGORY**
- As a **SITE USER** I can **SEARCH FOR A PRODUCT BY NAME** so that **I CAN FIND A SPECIFIC PRODUCT I WOULD LIKE TO VIEW/PURCHASE**
- As a **SITE USER** I can **SEE WHAT I HAVE SEARCHED FOR AND THE NUMBER OF RESULTS** so that **I QUICKLY DECIDE WHETHER THE PRODUCT IS AVAILABLE**
- As a **SITE USER** I can **SORT THE SPECIFIC CATEGORY OF PRODUCTS** so that **I CAN FIND THE BEST RATED OR BEST PRICED PRODUCT IN A SPECIFIC CATEGORY, OR SORT THE PRODUCTS IN THAT CATEGORY BY NAME**
- As a **SITE USER** I can **SORT MULTIPLE CATEGORIES OF PRODUCTS SIMOULTANIOUSLY** so that **I CAN FIND THE BEST RATED AND BEST PRICED PRODUCTS ACROSS A BROAD RANGE OF CATEGORIES**

#### EPIC | Purchasing and checkout
- As a **SITE USER** I can **VIEW THE ITEMS IN MY BASKET** so that **I CAN IDENTIFY WHAT ITEMS ARE IN THE BASKET, HOW MANY THEIR ARE AND WHAT THE TOTAL COST IS**
- As a **SITE USER** I can **ADJUST THE QUANTITY OF ITEMS IN THE BASKET** so that **I CAN MAKE CHANGES BEFORE PURCHASE IS COMPLETE**
- As a **SITE USER** I can **SELECT THE NUMBER OF PRODUCTS I WANT TO PURCHASE** so that **I DO NOT SELECT THE INCORRECT NUMBER OF ITEMS**
- As a **SITE USER** I can **VIEW HOW MUCH THE TOTAL COST OF MY PURCHASES WILL BE** so that **I CAN KEEP TRACK OF HOW MUCH I AM SPENDING**
- As a **SITE USER** I can **ENTER MY PAYMENT DETAILS EASILY AND QUICKLY** so that **I CAN COMPLETE MY PURCHASES WITH NO HASSLE**
- As a **SITE USER** I can **FEEL THAT MY PERSONAL AND PAYMENT DETAILS ARE BEING HANDLED WITH CARE** so that **I CAN CONFIDENTLY PROVIDE THE CORRECT INFORMATION NEEDED TO COMPLETE THE PURCHASE**
- As a **SITE USER** I can **VIEW AN ORDER CONFIRMATION AFTER CHECKOUT IS COMPLETE** so that **I CAN VERIFY I HAVENT MADE ANY ERRORS**

#### EPIC | About
- As a **SITE USER** I can **FIND INFORMATION ON THE COMPANY AND WHAT PRODUCTS THEY SELL** so that **I CAN DECIDE IF I WANT TO GIVE THEM MY BUSINESS**

#### EPIC | Delivery
- As a **SITE USER** I can **VIEW THE DELIVERY COST OF MY ORDERS** so that **I CAN KEEP TRACK OF HOW MUCH I AM SPENDING**
- As a **SITE USER** I can **VIEW FAQS REGARDING DELIVERY** so that **I CAN UNDERSTAND IF THE SITE WILL BE ABLE TO DELIVERY MY ORDER**

#### EPIC | Site Admin
- As a **SITE ADMIN** I can **ADD A PRODUCT TO THE SITE** so that **I CAN UPDATE THE SITE WITH NEW AND DIFFERENT PRODUCTS**
- As a **SITE ADMIN** I can **EDIT AND UPDATE PRODUCTS** so that **CHANGE PRICES, DESCRIPTIONS, IMAGES AND OTHER PRODUCT DETAILS**
- As a **SITE ADMIN** I can **DELETE PRODUCTS FROM THE STORE SITE** so that **I CAN REMOVE ITEMS THAT ARE NO LONGER REQUIRED**
- As a **SITE ADMIN** I can **HAVE A FACEBOOK BUSINESS PAGE** so that **I CAN EXTEND MY POTENTIAL BUSINESS FURTHER**
- As a **SITE USER** I can **SIGN UP TO A NEWSLETTER** so that **I CAN KEEP UP TO DAYTE WITH THE LATEST PRODUCTS AND INFORMATION FROM THE SITE**



### Agile Methodology

- To implement Agile Methodology during this project, GitHub Projects was used. Epics were attached to each User Story and within each User Story, an Acceptance Criteria was given to make clear when the User Story had been completed. Each User Story was also given Labels using the MoSCoW method. Most User Stories were given a "Must Have" label, while only a few contained "Should Have" or "Could Have". 
- To view the Project kanban board, please click here - [Project Board](https://github.com/users/donald-macritchie/projects/9/views/1)



### Design

#### Colour Scheme

- The site uses a simple colour scheme of monochromatic colours throught.
- Outside of the monochronme colours are bootstrap message colours
    - Red = Danger
    - Yellow = Warning
    - Blue  = Info
    - Green = Success

#### Images

- There is one main image on the site of the home page. Again using mainly monochromtaic colours with a hint of amber/orange.
- This image was used to give users an immediate indication of what the site is about. 
- The remaining images are all product images. 

#### Font

- The font used throughout the site is [Victor Mono](https://fonts.google.com/specimen/Victor+Mono). This was imported from Google fonts. Sans-serif has been used as a back up font incase of any import issues. This font was used as while it is still clear to read for the user, it holds a "edgier" and modern look that is used throughout craft beer websites. 


### WireFrames

Wireframes were created using [Figma's](https://www.figma.com/) online wireframe service.

<details>
<summary>Home </summary>

![homepage wireframe](static/screenshots/60_WF_home.png)
</details>

<details>
<summary>Products Page</summary>

![products page wireframe](static/screenshots/61_WF_products_page.png)
</details>

<details>
<summary>Product Detail</summary>

![products details wireframe](static/screenshots/62_WF_product_detail.png)
</details>

<details>
<summary>About Page</summary>

![about page wireframe](static/screenshots/63_WF_about.png)
</details>

<details>
<summary>Shopping Bag</summary>

![shopping bag page wireframe](static/screenshots/64_WF_shopping_bag.png)
</details>

<details>
<summary>Checkout</summary>

![checkout page wireframe](static/screenshots/65_WF_checkout.png)
</details>

<details>
<summary>Order Confirmation</summary>

![order confirmation page wireframe](static/screenshots/66_WF_order_confirmation.png)
</details>

<details>
<summary>Profile</summary>

![profile page wireframe](static/screenshots/67_WF_profile.png)
</details>

<details>
<summary>Wishlist</summary>

![wishlist page wireframe](static/screenshots/68_WF_wishlist.png)
</details>

### Database Schema

- During developoment, the SQLite database was used. The deployed site uses Postgres.

![image of the database schema](static/screenshots/97_database_schema.png)

### Defensive Design

#### User Authentication

- Using Django allauth, user authentication has been implemented across the site. 
- Site users can log in and out by using either their username or email address and password they create at the sign up stage.
- Site Admin users have full site access.
- Site Admin users can access the admin panels as well as adding, editing and deleting products. 
- To limit non admin users from accessing unauthorised areas of the site, toast messagea have been implemented.

![image of unautorised action](static/screenshots/70_unauthorised_action.png)

#### Custom 404

- A custom 404 page has been created for non-existent content

![image of custom 404 page](static/screenshots/69_404_page.png)

#### Form Validation

- All forms across the site have required fields as appropriate and are marked with an asterisk
- Any incorrect/invalid entries are flagged to the user with an error message.

---

## Business Model

Granite Tap's business model is Buisness to Customer (B2C). Products are sold directly from Granite Tap to the customer. 

### Marketing Strategy

Granite Tap has numerous marketing strategies. These include:
- Optimised SEO
- Email Marketing
- Content marketing
- Social Media Marketing

#### SEO

Search Engine Optimisation (SEO) has been implemented across the site to ensure high search engine ranking.

##### Keywords

- In order to optimize the visibility of Granite Tap and connect with our target audience effectively, we conducted thorough keyword research. This process involved identifying and analyzing the keywords and phrases that potential customers are likely to use when searching for craft beers, particularly those produced by local breweries in Aberdeen and Aberdeenshire, Scotland.
    - Local Craft Beer Emphasis: Emphasizing keywords related to "local craft beer" and "Aberdeen Aberdeenshire breweries" to highlight the regional aspect of our offerings.
    - Beer Variety and Quality: Targeting keywords associated with different beer varieties, brewing techniques, and quality indicators to showcase the diversity and excellence of our beer selection.
    - Granite Tap Unique Selling Points: Focusing on keywords that align with Granite Tap's unique selling points, such as "rich and flavourful brews", "variety of beer styles" and "local beer experience".

- To leverage these keywords effectively, we have integrated them into our website content, product descriptions, and meta tags and `<strong></strong>` tags. This strategic approach aims to enhance our search engine ranking and ensure that Granite Tap appears prominently when potential customers search for craft beers in our region.

- By aligning our content with the language and terms commonly used by our target audience, we aim to attract organic traffic, increase brand visibility, and ultimately drive engagement with our unique and locally brewed beer offerings.

![image of keyword research](static/screenshots/71_gt_keyword_research_table.png)

##### Google Search suggestions

<details>
<summary>Beer</summary>

![google search suggestion "beer"](static/screenshots/72_beer_google_search.png)
</details>

<details>
<summary>Ale</summary>

![google search suggestion "ale"](static/screenshots/73_ale_google_search.png)
</details>

<details>
<summary>IPA</summary>

![google search suggestion "ipa"](static/screenshots/74_IPA_google_search.png)
</details>

<details>
<summary>Brewery</summary>

![google search suggestion "brewery"](static/screenshots/75_brewery_google_search.png)
</details>

<details>
<summary>Craft Beer</summary>

![google search suggestion "craft beer"](static/screenshots/76_craft_beer_google_search.png)
</details>

<details>
<summary>New Beer</summary>

![google search suggestion "new beer"](static/screenshots/77_new_beer_google_search.png)
</details>

<details>
<summary>Different Beer</summary>

![google search suggestion "different beer"](static/screenshots/78_different_beer_google_search.png)
</details>

<details>
<summary>Local Beer Near Me</summary>

![google search suggestion "local beer near me"](static/screenshots/79_local_beer_near_me_google_search.png)
</details>

<details>
<summary>Buy Local Craft Beer Near Me</summary>

![google search suggestion "buy local craft beer near me"](static/screenshots/80_buy_local_craft_beer_near_me_google_search.png)
</details>

<details>
<summary>Aberdeen Beer</summary>

![google search suggestion "aberdeen beer"](static/screenshots/81_aberdeen_beer.png)
</details>

<details>
<summary>Aberdeenshire Beer</summary>

![google search suggestion "aberdeenshire beer"](static/screenshots/81_aberdeen_beer.png)
</details>

##### Sitemap

- A site map has been included in the site with a list of the URLs to make sure that search engines are able to understand and navigate the site's structure.
- The site map was created using [XML-Sitemaps.com](https://www.xml-sitemaps.com/)

##### Robots.txt

To increase the quality of the site and improve SEO, a robots.txt file has been created to tell the search engine where it is not allowed to go.

#### Email marketing

At Granite Tap, we recognize the importance of building and nurturing a strong connection with our audience. Email marketing serves as a powerful tool to keep our customers informed, engaged, and excited about our latest offerings. Our email marketing strategy, powered by [Mailchimp](https://mailchimp.com/), is designed to create meaningful interactions and drive customer loyalty.

##### Campaign Objectives

- Newsletter Updates: Regularly share updates on new beer releases, brewery collaborations, and exclusive offers through our engaging newsletter.
- Exclusive Promotions: Provide our subscribers with exclusive promotions, discounts, and early access to limited-edition brews to reward their loyalty.

##### Using Mailchimp

- Mailchimp enables Granite Tap to view the number of subscribers to the newsletter and from there can gauge subscriber growth over a period of time. This allows analysis of Newsletter content against product sales.


#### Content Marketing

- Granite Tap uses high quality product images to ensure user engagement. All product images have been used in small file sizes to minimise image loading times on the site.

#### Social Media Marketing

- At Granite Tap, our social media marketing strategy revolves around leveraging the power of Facebook to connect with our audience, build brand awareness, and foster engagement within the vibrant beer community. Here's an overview of our Facebook-focused social media page:

![image of facebook business page](static/screenshots/83_fb_header.png)

- Sharing visually appealing content, including high-quality images and videos that showcase our beers, brewery events, and behind-the-scenes moments.

![image of facebook post image](static/screenshots/84_fb_image_post.png)

- Fostering a sense of community by encouraging conversations, sharing experiences, and celebrating the craft brewing culture.

![image of facebook post](static/screenshots/85_fb_text_post.png)

- A link to the Granite Tap Facebook page is located in the footer of the site

***As this site is for educational purposes, the Granite Tap Facebook page has been deactivated and the link in the footer will open a new tab to the Facebook login page***

---

## Testing 

A variety of testing methods have been carried out on the Granite Tap site:
- Manual Testing
- Automated Testing
- Code Validation
- Device testing
- Browser Testing
- Bug Fixes

### Manual Testing

#### NavBar

- The following tests are carried out when the user is **unauthenticated**.

| Feature | Expect | Action | Result |
| --| --| --| --|
| Logo  | When clicked, the home page will open | Clicked on the Granite Tap Logo | Home Page opened |
| Search Bar button | Once a search term is entered into the input field, a products list will be generated in the products page with all products relating to the search term | Entered a search term and clicked search button | Products page opens with a list of products related to the search term |
| About Link | When clicked, the about page will open | Clicked the about link | About page opened |
| My Account Icon (when unauthenticated) | When clicked, a dropdown menu consisting of two options, "Register" and "Login" will appear | Clicked the My Account icon | Dropdown menu consisting of two options, "Register" and "Login" appears |
| My Account - Register link | When clicked, the sign up page will open | Clicked the register link | Sign up page opened |
| My Account - Login | When clicked, the login page will open | Clicked the login link | Login page opened |
| Shopping Bag icon | When clicked the shopping bag page will open | Clicked the shopping bag icon | Shopping bag page opens |

- The following tests are carried out when the user is **authenticated**

| Feature | Expect | Action | Result |
| --| --| --| --|
| My Account - My Profile | When clicked, the users profile page will open | Clicked the My Profile link | The users profile page opened |
| My Account - Wishlist | When clicked, the users wishlist page will open | Clicked the wishlist link | The users wishlist page opens | 
| My Account - Logout | When clicked, the logout page will open | Clicked the logout link | 

- The following tests ar ecarried out when the user is a **store admin/superuser**

| Feature | Expect | Action | Result |
| --| --| --| --|
| My Account - Product Management | When clicked, the product management - add a product page will open | Clicked the Product Management link | The product management - add a product page opens |

#### Product Menus

##### All Products

| Feature | Expect | Action | Result |
| --| --| --| --|
| By Price | When clicked, the products page will open in ascending order of price | Clicked the By Price link | Products page opens in order of ascending order| 
| By Rating | When clicked, the products page will open in descending order of rating | Clicked the By Rating link | Products page opens in descending order of rating
| By Category | When clicked, the products page will open in alphabetical order of product category (beer type) | Clicked the By Category link | Products page opens in alphabetical order of product category (beer type) |
| All Products | When clicked, the products page will open | Clicked the All Products link | Products page opens |

##### Beer Types

| Feature | Expect | Action | Result |
| --| --| --| --|
| Lager | When clicked, the products page will open displaying only Lager products | Clicked Lager link | Products page opens displaying only Lager products |
| Ale | When clicked, the products page will open displaing only Ale products | Clicked Ale link | Products page opens displaying only Ale products |
| Stout | When clicked, the products page will open displaing only Stout products | Clicked Stout link | Products page opens displaying only Stout products |
| Sour | When clicked, the products page will open displaing only Sour products | Clicked Sour link | Products page opens displaying only Sour products |

##### Breweries

| Feature | Expect | Action | Result |
| --| --| --| --|
| Brewdog | When clicked, the products page will open displaying only Brewdog products | Clicked Brewdog link | Products page opens displaying only Brewdog products |
| Brew Toon | When clicked, the products page will open displaying only Brew Toon products | Clicked Brew Toon link | Products page opens displaying only Brew Toon products |
| Fierce | When clicked, the products page will open displaying only Fierce products | Clicked Fierce link | Products page opens displaying only Fierce products |
| Six° North | When clicked, the products page will open displaying only Six° North products | Clicked Six° North link | Products page opens displaying only Six° North products |

#### Footer

| Feature | Expect | Action | Result |
| --| --| --| --|
| Contact Us link | When clicked, the About page will open at the Contact form | Clicked on the Contact link | About page opened at the Contact form |
| Subscribe to our Newsletter Link | When clicked, the About page will open at the Newsletter sign up section | Clicked the Sign Up to our Newsletter link | About page opened at the newsletter sign up section |
| Visit us on Facebook link | When clicked, a new tab will will open at the Facebook login page | Clicked the Visit us on Facebook link | Facebook login page opened in a new tab |
Privacy Policy link | When clicked, the Granite Tap privacy policy document will open in a new tab | Clicked the Privacy Policy link | The Granite Tap privacy policy opened in a new tab |


#### Home Page
| Feature | Expect | Action | Result |
| --| --| --| --|
| Shop Now button | When clicked, the all products page will open | Clicked the Shop Now button | The All Products page opened | 

#### Products Page

- When the user has filtered the product list to the product category or brewery

| Feature | Expect | Action | Result |
| --| --| --| --|
| Products Home link | When clicked, the All Products page will open | Clicked the Products Home link | All Products page opened |

##### Sort By... Filtering

| Feature | Expect | Action | Result |
| --| --| --| --|
| Price (low to high) | When clicked, the products page will open with products listed in ascending order of price | Clicked Price (low to high) | Products page opened with products listed in ascending order of price |
| Price (high to low) | When clicked, the products page will open with products listed in descending order of price | Clicked Price (high to low) | Products page opened with products listed in descending order of price |
| Rating (low to high) | When clicked, the products page will open with products listed in ascending order of rating | Clicked Rating (low to high) | Products page opened with products listed in ascending order of rating |
| Rating (high to low) | When clicked, the products page will open with products listed in descending order of rating | Clicked raing (high to low) | Products page opened with products listed in descending order of rating |
| Name (A-Z) | When clicked, the products page will open with products listed in alphabetical order | Clicked Name (A-Z) | The products page opened with products listed in alphabetical order |
| Name (Z-A) | When clicked, the products page will open with products listed in reverse alphabetical order | Clicked Name (Z-A) | The products page opened with products listed in reverse alphabetical order |
| Category (A-Z) | When clicked, the products page will open with products listed in alphabetical order of category (beer type) | Clicked Category (A-Z) | The products page opened with products listed in alphabetical order of category (beer type) |
| Category (Z-A) | When clicked, the products page will open with products listed in reverse alphabetical order of category (beer type) | Clicked Category (Z-A) | The products page opened with products listed in reverse alphabetical order of category (beer type) |


##### Product card

| Feature | Expect | Action | Result |
| --| --| --| --|
| Product Image | When clicked, the product detail page will open | Clicked the product image | The product detail page opened | 
| Brewery Link | When clicked, the brewery product list will open | Clicked the brewery link | The brewery product list opened |
| Category (beer type) link | When clicked, the category product page will open | Clicked the Category (beer type) link | The Category product page opened |

- The following tests ar ecarried out when the user is a **store admin/superuser**

| Feature | Expect | Action | Result |
| --| --| --| --|
| Edit link | When clicked, the Product management - Edit a Product page will open | Clicked the Edit link | The Product Management - Edit a Product page opened | 
| Delete button | When clicked, the product will be removed from the product list database | Clicked the delete button | The Product is removed from the product list and database | 

**If you wish to test this functionality, please do not edit or delete existing products. Create a test product first then test the edit and delete functionality. Please see the Product management testing section for more detail**

#### Product Detail Page

##### Product details and quantity selection

| Feature | Expect | Action | Result |
| --| --| --| --|
| Product Image | When clicked, the product image page will open in a new tab | Clicked the product image | The product image page opened in a new tab | 
| Brewery Link | When clicked, the brewery product list will open | Clicked the brewery link | The brewery product list opened |
| Category (beer type) link | When clicked, the category product page will open | Clicked the Category (beer type) link | The Category product page opened |
| Quantity - Integer Input | When an integer is entered into the input box, a quantity integer is displayed | Entered a quantity intger into the input box | Quantity integer is displayed |
| Quantity -  "+" button | When clicked the quantity integer in the input box will increase | Clicked the Quantity "+" button | The quantity integer increased | 
| Quantity -  "-" button | When clicked the quantity integer in the input box will decrease | Clicked the Quantity "-" button | The quantity integer decreased | 
| Add to bag button | When clicked, the product and selected quantity will be added to the shopping bag | Clicked the Add to Bag button | The product and selected quantity is added to the shopping bag |
| Keep Shopping Button | When clicked, the All Products page will open | Clicked the Keep Shopping button | The All Products page opened |

- The following tests are carried out when the user is **authenticated**

| Feature | Expect | Action | Result |
| --| --| --| --|
| Add to Wishlist button | When clicked, the product will be added to the users wishlist | Clicked the Add to Wishlist button | the product is added to the users wishlist |

- The following tests ar ecarried out when the user is a **store admin/superuser**

| Feature | Expect | Action | Result |
| --| --| --| --|
| Edit link | When clicked, the Product Management - Edit a Product page will open | Clicked the Edit link | The Product Management - Edit a Product page opened | 
| Delete button | When clicked, the product will be removed from the product list database | Clicked the delete button | The Product is removed from the product list and database | 

##### You May Also Like...

| Feature | Expect | Action | Result |
| --| --| --| --|
| Product Image | When clicked, the product detail page will open | Clicked the product image | The product detail page opened | 
| Brewery Link | When clicked, the brewery product list will open | Clicked the brewery link | The brewery product list opened |
| Category (beer type) link | When clicked, the category product page will open | Clicked the Category (beer type) link | The Category product page opened |


#### Shopping Bag 

| Feature | Expect | Action | Result |
| --| --| --| --|
| Quantity - Integer Input | When an integer is entered into the input box, a quantity integer is displayed | Entered a quantity intger into the input box | Quantity integer is displayed |
| Quantity -  "+" button | When clicked the quantity integer in the input box will increase | Clicked the Quantity "+" button | The quantity integer increased | 
| Quantity -  "-" button | When clicked the quantity integer in the input box will decrease | Clicked the Quantity "-" button | The quantity integer decreased | 
| Update button | When clicked, the quantity of the product will update to the quantity specified | Clicked the Update button | The quantity updated to the spcified quantity |
| Remove button | When clicked the product will be removed from the shopping bag | Clicked the Remove button | The product was removed from the bag |
| Keep Shopping Button | When clicked, the All Products page will open | Clicked the Keep Shopping button | The All Products page opened |
| Secure Checkout button | When clicked, the checkout page will open | Clicked the Secure Checkout button | The Checkout page opened |

#### Checkout 
| Feature | Expect | Action | Result |
| --| --| --| --|
| Country Field selection | When clicked, the Country list will open allowing for user selection | Clicked the Country field | Country list opened allowing for user selection |
| Save Delivery Info checkbox | When checked and the order is completed, the users delivery infomation will be saved to the users profile | Checked the save delivery checkbox | In the user profile, the saved delivery information prepopulated the default delivery form |
| Payment field - Invalid Input | When the payment field is populated with an invalid card number, an error message stating "Your Card Number is Invalid", will appear below the payment field | Input an invalid card number | Error message appeared stating " Card Number is Invalid |
| Adjust Bag button | When clicked, the Shopping Bag page will open | Clicked the Adjust Bag button | The Shopping Bag page opened |

##### Completing an Order

| Feature | Expect | Action | Result |
| --| --| --| --|
| Complete Order button - Valid | When all required user information is entered into the form fields and the Complete order button is clicked, a pop up overlay will appear. The Order Confirmation page will then open | Entered valid user information and clicked Complete Order button | Loading overlay appeared and Confirmation page opened |
| Complete Order button - invalid | When invalid information is entered into the form fields and the Complete Order button is clicked, an error message will appear next to the invalid field | Entered invalid information and clicked Complete Order button | Error message appeared next to the invalid field | 

#### Order Confirmation page


| Feature | Expect | Action | Result |
| --| --| --| --|
| Have a look back at more of our beers button | When clicked, the All Products page will open | Clicked the Have a look back at our beers button | The All Products page opened | 

#### Profile Page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Update information button | Once new information has been entered into the Default Delivery Information form, when clicked, the new information will populate the form | Input new informtion into Default Delivery Information form and clicked Update Information button | New information populated the Default Delivery Information form |
| Order History - Order Number Link | When clicked, the Order Confirmation page will open | Clicked the Order Nunber link | Order Confirmation page opened |

#### Order History page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Back to Profile button | When clicked, the users profile page will open | Clicked the Bcak to Profile button | The Users profile page opened |

#### Wishlist Page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Product Card - Product Image | When clicked the product's Product detail page will open | Clicked the Prodduct Image | The product's Product detail page opened | 
| Product Card - Brewery Link | When clicked, the brewery product list will open | Clicked the brewery link | The brewery product list opened |
| Product Card - Category (beer type) link | When clicked, the category product page will open | Clicked the Category (beer type) link | The Category product page opened |
| Remove form Wishlist button | When clicked, the product will be removed from the wishlist | Clicked teh Remove from Wishlist button | The product was removed from the Wishlist | 

#### Register/Sign Up Page

- The following test has been carried out by an unregistered/logged out user

| Feature | Expect | Action | Result |
| --| --| --| --|
| Sign In link | When clicked, the login/sign in page will open | Clicked the sign in link | The login/sign in page opened |
| Sign Up button - Valid | When the input fields have valid information, when clicked, the Verify Your Email page will open | Enter Valid information into the input fields | The Verify your Email page opened | 
| Once Email Has been verified | Once the users email has been verified from the users email account, the Confirm Email page will open | Verified Email from users email account | Confirm Email page opened | 

#### Confirm Email Page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Confirm button | When clicked, the login/Sign in page will open | Clicked the Confirm button | The login/sign in page opened | 

#### Login/Sign In page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Sign Up link | When clicked, the Sign Up page will open | Clicked the Sign Up link | The Sign Up Page opened |
| Sign In button | Once the user has entered their account information and password, when clicked, the home page will open | Entered user information and password, clicked sign in button | Home page opened | 
| Home Button | When clicked the Home Page will open | Clicked the Home button | The Home Page opened | 
| Forgot your Password? link | When clicked, the password reset page will open | Clicked the Forgot your Password? link | The password reset page opened | 

#### Logout Page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Sign Out button | When clicked, the Home page will open | Clicked the Sign Out button | The Home Page opened |
| Cancel button | When clicked, the Home Page will open | Clicked the cancel button | Home Page opened | 

#### Password Reset page

| Feature | Expect | Action | Result |
| --| --| --| --|
| Reset my Password | Once the user has input their email into the input field, when clicked, the Password Reset Done page will open | Entered user email into input field and clicked Reset my Password button | The Password Reset Done page opened | 

#### Change Password 

| Feature | Expect | Action | Result |
| --| --| --| --|
| Change Password button | Once the user enters a new password and confirms it in both input fields, when clicked, Password Reset Key Done page will open | Entered new password and confirmed then clicked Change password button | Password Reset Key Done page opened | 
Back to login button | When clicked, the Login/SignIn page will open | Clicked the Back to Login button | The Login/SignIn page opened | 

#### About Page

##### FAQs

| Feature | Expect | Action | Result |
| --| --| --| --|
| FAQs to open Bootstrap Accordian | When clicked, the answer will dropdown from the question | Clicked the FAQ | The Answer dropped down | 
| FAQs to close Bootstrap Accordian | When clicked, the answer will collapse back into the question | Clicked the FAQ | The Answer collapsed back into the question | 

##### Newsletter

| Feature | Expect | Action | Result |
| --| --| --| --|
| Newsletter subscribe button | Once a user has entered an email address into the input field, when clicked, a new tab will open with the newsletter subscription confirmation | Entered email address | A new tab opened with the newsletter subscription confirmation | 

##### Contact Us

| Feature | Expect | Action | Result |
| --| --| --| --|
| Submit button | Once the user has input all their information into the required fields, when clicked, the form data will be stored in the admin and the user is redirected back to the about page | Entered information into the required fields and clicked submit | Redirect to about page. Form data stored in the admin | 


### Code Validation

#### HTML

- Validation was carried out using [W3C HTML Validator](https://www.w3.org/)

| Page | | | Errors |
| --| --| --| --|
| Home | | | No Errors |
| All Products | | | No Errors |
| By Category | | | No Errors |
| By Rating | | | No Errors |
| By Price | | | No Errors |
| Lager | | | No Errors |
| Ale | | | No Errors |
| Stout | | | No Errors |
| Sour | | | No Errors |
| Product Detail | | | No Errors |
| Shopping Bag | | | No Errors |
| Checkout | | | No Errors |
| Order Confirmation | | | No Errors |
| About | | | No Errors |
| My Profile | | | No Errors |
| Order History | | | No Errors |
| Wishlist | | | No Errors |
| Product Management - Add a Product | | | No Errors |
| Product Management - Edit a Product | | | No Errors |
| Sign Up/Register | | | No Errors |
| Login | | | No Errors |
| Logout | | | No Errors |
| Password Reset | | | No Errors |
| Change Password | | | No Errors |
| Change Password Success | | | No Errors |

- Errors returned with duplicate ids. This is due to the mobile-top-header.html file being included. As it uses the same ids. 

#### CSS

- Validation was carried out using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

| File | | | Errors |
| --| --| --| --|
| base.css | | | No Errors |
| profiles.css | | | No Errors |
| checkout.css | | | No Errors |

#### JavaScript

- Validation was carried out using [JSHint](https://jshint.com/)

| File | | | Errors |
| --| --| --| --|
| about.html | | | No Errors |
| bag.html | | | No Errors |
| stripe_elements.js | | | No Errors |
| products.html | | | No Errors |
| add_product.html | | | No Errors |
| edit_product.html | | | No Errors |
| quantity_input_script.html | | | No Errors |
| countryfield.js | | | No Errors |
| base.html | | | No Errors |

#### Python

- Validation was carried out using [pep8 CI Pyton Linter](https://pep8ci.herokuapp.com/#)

| App | | | Errors |
| --| --| --| --|
| About | | | No Errors |
| Bag | | | No Errors |
| Checkout | | | No Errors |
| Granite Tap (project) | | | No Errors |
| Home | | | No Errors |
| Products | | | No Errors |
| Profiles | | | No Errors |
| Wishlist | | | No Errors |


### Device Testing 

- The site has been tested on a variety of device sizes using Chromes devtools.
- Devices tested:
    - Desktop
    - Laptop
    - Tablet
    - Phone

### Browser Tesing

- The site has been tested on Google Chrome, Safari and Firefox. 
- No issues have been identified while using these browsers

### Bug Fixes

#### Stripe Webhooks
- Having tested the site in the development environment, processing orders were working. However when testing the payment process in the live environment didn't give positive results. I initially thought there was an issue with the webhook code in the checkout app. All environment variables were correct as well as the Heroku Config Vars. After some Investigation, I realised that the endpoint generated in the Stripe dashboard was being used for the development environment and not the Live environment. This was a fairly easy fix. I generated a new webhook endpoint in Stripe and applied the new environment keys required.


#### Django emails
- When testing in the Live environment, Emails were not being automatically sent when they should have. I discovered this bug when registering a user account and no confirmation email was being sent. The issue was due to a recent change on Heroku where Heroku will build everything on Python 3.12, which isn't compatable with smtplib. The solution was to create a new file `runtime.txt` in the root directory of the project and add `python-3.9.18`. This tells Heroku what version to build the project with

---

## Project Set Up and Deployment

### Project Set Up

In order to set up this project, these steps were taken:

- In GitHub:
    - Set up a new repository using the Code Institute template.
    - Give it a unique name.
- In Gitpod (or a IDE of your choice):
    - Click "New Workspace"
    - Paste the repositiory URL into the new workspace and click "Continue"
    - After a minute or two, the workspace will open.
- In the Workspace Terminal:
    - Install Django using the command
    ```text
    pip3 install 'django<4'
    ```
    - Create the project:
    ```text
    django-admin startproject granite_tap .
    ```
    - Run the project:
    ```text
    python3 manage.py runserver
    ```
    - If required, add the development server URL to the ```ALLOWED_HOSTS``` in order to view in the browser.
    - Run the initail migrations:
    ```text
    python3 manage.py migrate
    ```
    - To be able to login to the django admin, create a superuser:
    ```text
    python3 manage.py createsuperuser
    ```
    - Enter a Username, email and password.
    - Initial commit:
    ```text
    git add .
    git commit -m "initail commit"
    git push
    ```

### Deployment

In order to deploy the project to host the site on heroku, these steps were taken.

#### Create PostgreSQL database

- Login to [ElephantSQL](https://www.elephantsql.com/)
- On the dashboard click "Create New Instance"
- Set up your plan:
    - Give it a name.
    - Select the "Tiny Turtle (Free) plan.
    - Tags can be left blank.
- Select your region.
- Select a data center near you.
- Click "Review".
- Check the detail are correct and click "Create Instance"
- Return to the ElephantSQL dashboard and click on the database instance name for the project.
- In the URL section, click the copy icon and the database URL will be copied to your clipboard.

#### Create a New Heroku App

- In [Heroku](https://id.heroku.com/login) click "New" to create a new app.
- Give it a name and select a region closest to you.
- Click "Create App"
- Open the settings tab.
    - In the settings tab, click "Reveal Config Vars"
    -  Add the config var "DATABASE_URL" for the key and paste in the ElephantSQL database url into the value and click "Add".

#### In the workspace terminal

- Install dj_database_url and psycopg2:
```text
    pip3 install dj_database_url==0.5.0 psycopg2
```
- Update the requirements.txt file:
```text
    pip3 freeze > requirements.txt
```

#### In settings.py

- Import dj_database_url underneath the import for os:
```python
    import os
    import dj_database_url
```
- Scroll to the DATABASES section:
    - Update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated
```python
     # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
     
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```
**DO NOT commit this file with your database string in the code, this is temporary so that we can connect to the new database and make migrations. We will remove it in a moment.**

#### In the Terminal:

- Run the showmigrations command to ensure you are connected to the external database
```text
    python3 manage.py showmigrations
```

- Migrate your database models to your new database:
```text
    python3 manage.py migrate
```

- Load your categories fixture:
```text
    python3 manage.py loaddata categories
```

- Load your products fixture:
```text
    python3 manage.py loaddata products
```

- Create a new superuser for your database:
```text
    python3 manage.py createsuperuser
```

- In order to prevent exposing the database when pushed to github, it will be deleted again from settings.py

#### In settings.py

- For the time being, reconnect to the local sqlite database
- your DATABASES section should look like this:
```python
    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
 }
```

#### In ElephantSQL

- To confirm the data in the database has been created, navigate to the "Browser" tab in the ElephantSQL dashboard.
- Click "Table queries" button
- Select "auth_user"
- Click "Execute"
- You should now see the newly created superuser details being displayed. This confirms that you can add data to your database.

#### In settings.py

- In the DATABASE section create an "if" statement so when the app is running on Heroku the database URL environment will be connected to the Postgres database.
- In the "else" block, it will use the default database.
```python
    if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

#### In the terminal

- Install gunicorn:
```text
    pip3 install gunicorn
```
- Freeze into requirements.txt:
```text
    pip3 freeze > requirements.txt
```

#### In the Root directory

- Create a Procfile. This tells Heroku to run a web dyno
- In the Procfile input:
```text
    web: gunicorn your_project_name_here.wsgi:application
```

#### In the terminal

- Login into Heroku:
```text
    heroku login -i
```
- Enter your heroku login username
- Enter your Heroku API key as the password
- Disable collectstatic
```text
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku_app_name_here
```
- This ensures, Heroku does not collect static files when you initially deploy.

#### In settings.py

- Add Heroku host name (deployed URL) into ```ALLOWED_HOSTS```

#### In the terminal

- Push the changes to Github:
```text
    git add .
    git commit -m "deployment"
    git push
```
- Push Changes to Heroku
    - Initialize Heroku Git remote (if required)
    ```text
        heroku git:remote -a your_heroku_app_nanme_here
    ```
    - Push to Heroku
    ```text
        git push heroku main
    ```

#### In Heroku 

Set up automatic deployment in the "Deploy" tab.

- Connect the Github repository.
    - Click "Connect to Github"
    - Search for your repository
    - Click "Connect"
- Go to "Automatic deploys"
    - Click " Enable Automatic Deploys"
- With this set up, everytime the cide is push to Github, the code will automatically deploy to Heroku.

#### Generate a new SECRET_KEY

- To generate a new SECRET_KEY, this cone be done with an online secret key generator such as [djecrety](https://djecrety.ir/).

#### In the Heroku Settings Tab

- In the Config vars, add "SECRET_KEY" to the key field and the newly geneerated secret key to the value field.

#### In settings.py

- Replace the SECRET_KEY value with ```os.environ.get(SECRET_KEY, '')```

#### In the terminal

- Push the changes to github
```text
    git add .
    git commit -m "Removed secret key"
    git push
```

### AWS Set Up

In order to set up AWS, these steps were taken:

- Navigate to [aws.amazon](https://aws.amazon.com/).
- Create an account by clicking on "Create AWS account" and filling in all the relevant information
- Select "Continue"
- On the "Account Type" page, fill in the required information and click "Create Account".
- On the "Payment information" page, enter payment details. Users are charged if they go above the free usage limits.
- Confirm further verification questions and create the account.
- Once signed back in, go to the "AWS Management console" page.

### S3 Bucket

- In the "AWS Management Console" page, search for "S3" in the search bar.
- Open "S3".
- To Create anew bucket, click "Create Bucket" 
- Give the bucket a name (preferabley the same or similar to the heroku app name).
- Select a region.
- In "Object Ownership", click "ACL's Enabled" and "Bucket owner preferred"
- Uncheck the "Block all public access" to acknowledge that the bucket will be public.
- Click "Create bucket"

#### In the new Bucket

- Go to the "Properties" tab. Scroll to the bottom and under "Static website hosting" click "edit" and change the "Static website hosting" option to "enabled". Copy the default values for the index and error documents and click "save changes".
- In the Permissons section, paste this code into the CORS section:
```text
    [
        {
            "AllowedHeaders": [
            "Authorization"
        ],
            "AllowedMethods": [
            "GET"
        ],
            "AllowedOrigins": [
            "*"
        ],
            "ExposeHeaders": []
        }
]
```
- In the "Bucket Policy" tab, select "Policy Generater".
- Select "S3 Bucket Policy" from the dropdown.
- Add an asterisk "*" to the Principal field to allow all principals.
- In the "Action" dropdown, select "GetObject".
- Copy in the ARN into the ARN input. (This can be found in the S3 Bucket page).
- Click "Add Statement" 
- Click "Generate Policy" 
- Copy the policy into the bucket policy editor.
- On the end of the resourse key, add "/*".
- Click "Save"
- In the "Access Control List" section click "edit" and under "Everyone(public access)" enable "List"

### IAM

- In the "services" menu, open "IAM".
- Once on the IAM page, click "User Groups" from the side bar, then click "Create group".
- Give the group a name and click "Create"
- Go to "Policies", click "Create New Policy". Go to the "JSON" tab and click "Import Managed Policy". 
- Search for "S3" and then import the "S3 Full Access Policy".
- Get The bucket ARN from the bucket page in S3 and paste it into the JSON policy tab in IAM:
```
"Resource": [
    "ARN-NO-HERE",
    "ARN-NO-HERE/*"
]
```
- Click "Reveiw Policy"
- Give the Policy a name and description.
- Click "Create Policy".
- Attach the policy to the Group
    - On the Side Bar, click "User Groups".
    - Select the Group
    - Go to "Permissions" dropdown.
    - Open "Add Permissions" dropdown.
    - Click "Attach Policy".
    - Select the policy and click "Add Permissions" at the bottom.
- Create a user to put into the Group. Select "Users" from the side bar and click "Add User".
- Give your user a user name and check "Programmatic Access".
- Navigate through by clicking "Next" until you reach the "Create user" button and click "Create User".

#### Retreive Access Keys

- Go to IAM
- Select the user for whom you wish to create a CSV file.
- Select the 'Security Credentials' tab
- Scroll to 'Access Keys' and click 'Create access key'
- Select 'Application running outside AWS', and click next
- On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
- Click the 'Download .csv file' button

### Connect Django and S3

#### In the Terminal

- Install Boto3:
```text
    pip3 install boto3
```
- Install Django Storages
```text
    pip3 install django-storages
```
- Freeze into requirements.txt
```text
    pip3 freeze > requirements.txt
```

#### In settings.py

- Add Storages to install apps
```python
    INSTALLED_APPS = [
    # other installed apps...

    'storages',
]
```

- Connect Django to S3
```python
    if 'USE_AWS' in os.environ:

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
    AWS_S3_REGION_NAME = 'your_region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
- Both Access Keys come from the credentials.cvs file downloaded from IAM.

**Ensure your Access Keys are kept out of version control.**

#### In Heroku settings

- Add the Access Keys to the Config Vars.
- Add "USE_AWS" Key with a value of "True"
- Remove the "DISABLE_COLLECTSTATIC" variable.

#### In the root directory

- Create a file "custom_storages.py"

#### In custom_storages.py

- Import settings and S3Boto3 Class
- Create custom Class for static and media storage:
```python
    class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
```

#### In settings.py

- For static and media file storage, add within the ```USE_AWS``` if statement:
```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Once this is pushed, The S3 bucket will have all the static and media files.

#### In settings.py

- Optional setting
- In the ```USE_AWS``` if statement, at the top, add:
```python
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```
- This will improve performance for users.

- Push to github/Heroku:
```text
    git add .
    git commit -m " add cache control"
    git push
```

#### Adding Media Files to S3

- In the S3 Bucket:
    - Create a new folder called "Media"
    - Inside the "media" folder, click "Upload"
    - Click "Add Files"
    - Select all product images.
    - Click "Next".
    - Under the "Manage public permissions" select "Grant Public read access to this object(s).
    - Click "Next" through to the end
    - Click "Upload".

#### In Heroku Settings

- In the Config Vars:
    - Add Stripe public key
    - Add Stripe secret key
    - These are retrievable from the Stripe Dashboard

#### In the Stripe Dashboard

- Add a new endpoint for the deployed site
    - Click "Developers"
    - Click "Webhooks"
    - Click "Add endpoint"
    - Enter the deployed URL followed by "/checkout/wh/" into "Endpoint URL"
    - Click "Select events"
    - Check the "Select all events" box
    - Click "Add Endpoint"
    - Reveal "Signing Secret"

#### In Heroku Settings

- Add "STRIPE_WH_SECRET" and the Stripe signing secret to the config vars.

**Ensure all Config Vars in Heroku match thise used in settings.py**

With all this complete, the site is now deployed. 

---

## Languages

The languages used in this project are:
- HTML5
- CSS3
- JavaScript
- Python

---



## Credits/References

### Code

- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
    - Inspiration was taken from The Boutique Ado Walkthrough Project created by Code Institute. 
    - Code from this repo was used in the Bag, Checkout, Products and Profiles App. 
- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- Various support from Code Institutes Tutoring team.
- [Adobe Stock](https://stock.adobe.com/uk/?gclid=Cj0KCQiAqsitBhDlARIsAGMR1RiXKFH8tRS9f5DkY8TaOUGXrEltr66HGHPyNuFcixJwztvNykhArWgaAmGeEALw_wcB&ef_id=Cj0KCQiAqsitBhDlARIsAGMR1RiXKFH8tRS9f5DkY8TaOUGXrEltr66HGHPyNuFcixJwztvNykhArWgaAmGeEALw_wcB:G:s&s_kwcid=AL!3085!3!610386024915!e!!g!!adobe%20stock!9547248708!145683474624&as_channel=sem&as_campclass=brand&as_campaign=UK|CPRO|Stock|PURCH|AS_Brand_Exact|GG||&as_source=google&mv=search&mv2=paidsearch&as_camptype=acquisition&sdid=WKRCJHQP&as_audience=core&gad_source=1)
- [Stack Overflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)

### Frameworks, Libraries and Technologies

This projects used the following frameworks and libararies:

- [Django](https://www.djangoproject.com/) - Main framework used
- [Django Allauth](https://docs.allauth.org/en/latest/) - authentication library used to create User accounts.
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Used to style html structure.
- [PostgeSQL](https://www.postgresql.org/) - Deployed Database
- [SQLite](https://www.sqlite.org/index.html) - Development Database
- [Stripe](https://stripe.com/gb) - Secure Payments. 
- [XML-Sitemaps](https://www.xml-sitemaps.com/) - Site Map Generator.
- [AWS](https://aws.amazon.com/) - Static and media file storage.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) - This backend implements the Django File Storage API for Amazon Web Services’s (AWS) Simple Storage Service (S3).
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Simple Storage Service (Amazon S3).
- [Django Countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Manages django forms
- [Github](https://github.com/) - Version Control and Agile tool. 
- [Font Awesome](https://fontawesome.com/) - Icon library and toolkit. 
- [Google Fonts](https://fonts.google.com/) - Font imports.
- [Figma](https://www.figma.com/login?is_not_gen_0=true) - Used to create wireframes.
- [Mailchimp](https://mailchimp.com/) - Newsletter signup.
- [Privacy Policy Generator](https://www.privacypolicygenerator.info/) - Used to create the sites Privacy Policy. 

### Images

<details>
<summary>Home Page Hero Image</summary>

- [Homepage Hero Image](https://stock.adobe.com/uk/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=1&filters%5Bcontent_type%3Atemplate%5D=1&filters%5Bcontent_type%3A3d%5D=1&filters%5Bcontent_type%3Aimage%5D=1&k=beer+tap&order=relevance&safe_search=1&search_page=1&search_type=autosuggest&acp=0&aco=beer+tap&get_facets=0&asset_id=358302977)
</details>
 
<details>
<summary>Product Images</summary>

- [Brewdog's Punk IPA](https://www.tesco.com/groceries/en-GB/products/308107419)
- [Brewdog's Lost Lager](https://www.tesco.com/groceries/en-GB/products/313836270)
- [Brewdog's Hazy Jane](https://www.tesco.com/groceries/en-GB/products/308109741)
- [Brewdog's Black Heart](https://www.tesco.com/groceries/en-GB/products/313952189)
- [Brewdog's Rattle and Rum](https://www.tesco.com/groceries/en-GB/products/312707091)
- [BrewToon's Weekend Hooker](https://www.brewtoon.com/item/238/BrewToon/Weekend-Hooker-440ml-Can.html) 
- [BrewToon's Wired to the Toon](https://www.brewtoon.com/item/319/BrewToon/Wired-to-the-Toon-2023.html) 
- [BrewToon's Trawlerman](https://www.brewtoon.com/item/223/BrewToon/Trawlerman-440ml-Can.html) 
- [BrewToon's M'ango Unchained](https://www.brewtoon.com/item/231/BrewToon/Mango-Unchained-440ml-Can.html) 
- [BrewToon's Sour to the People](https://www.brewtoon.com/item/233/BrewToon/Sour-to-the-People-440ml-Can.html)
- [Fierce's Cerveza](https://fiercebeer.com/products/fierce-cerveza?_pos=1&_sid=b758a7d68&_ss=r)
- [Fierce's Fierce IPA](https://fiercebeer.com/products/fierce-ipa?_pos=1&_sid=2c08ebe15&_ss=r) 
- [Fierce's Forest Ranger](https://fiercebeer.com/products/forest-ranger?_pos=9&_sid=2c08ebe15&_ss=r) 
- [Fierce's Cookie Dough](https://fiercebeer.com/products/cookie-dough-tartarus-collab-1?_pos=3&_sid=1fe7d465c&_ss=r) 
- [Fierce's Black Grape Punch](https://fiercebeer.com/products/black-grape-punch?_pos=3&_sid=2b32e43fc&_ss=r)
- [Six°North's Omniun](https://www.sixdnorth.co.uk/ipa/omnium) 
- [Six°North's Barrel Aged Moon](https://www.sixdnorth.co.uk/dark/barrelagedmoon) 
- [Six°North's Peleton](https://www.sixdnorth.co.uk/lager/peloton) 
- [Six°North's Summer Bliss](https://www.sixdnorth.co.uk/fruit/summerbliss) 
- [Six°North's Veledrome](https://www.sixdnorth.co.uk/ipa/velodrome)

</details>

### General
### ReadMe Documentation

- "Creating a Readme" - from Code Institute Diploma in Full Stack Software Development Course.
- Code Institute's [readme template](https://github.com/Code-Institute-Solutions/readme-template)
- Kera Cudmore's [readme examples](https://github.com/kera-cudmore/readme-examples)
- [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#styling-text) 
- Alison O'Keeffe's [Fresh Nest Readme Docs](https://github.com/AliOKeeffe/PP5-Fresh-Nest/blob/main/README.md)

### Acknowledgements

- A big thank you to Code Institute Mentor, Antonio Rodriguez, for all the help and support through this Project.
- Also thanks to Code Institute Tutor, Oisin Tohak for all help and support given. 

