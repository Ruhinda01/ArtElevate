# ARTELEVATE

![ArtElevate Logo](app/static/images/artelevate_logo.png)

## Introduction
### The Project

Art is the an expression of the human spirit and the many paths man has taken to become what we are today. It is a time capsule for a past, present and future. Without art, how would we ever justify our time here on this big ball called "Earth". Well, I present to you **ArtElevate**.

**ArtElevate** is a online art gallery aiming to respond to local, well known artists, collectors, art enthusiasts and the casual user indulging in everything art. Artists can create their profiles, upload their artwork on to the platform, sell their artwork on the platform and also check out works from other artists. Users can register onto the platform, add their favorite artworks to their favorites page, add artwork to cart, view artwork details and artist profiles.

Other features for artists is to delete or edit artwork uploaded onto the platform, removing artwork from the favorites page, adding and removing from cart and updating quantity of an item in the cart.

### The Context

This project is our Portfolio Project concluding the Foundations at ALX SE Program. We were able to choose what to build and produce a working MVP (Minimum Viable Product) by the end of the two and half week deadline.

### The Team

I worked on this project by myself. I am passionate about design and technology. I love to learn new things and this was actually one of the biggest challenges i have undertaken.

* Ruhinda Roderick Izooba - Graduate Architect and Aspiring Software Engineer.

### Tech Stack

![Tech_stack](/README/Tech%20stack.png)

### Architecture
#### Overview

This web application is coded mainly in python and flask as a web framework. It is a full stack application with back-end to increase functionality and front-end to build the UI and UX of the application. I designed the User Interface using HTML, and Bootstrap 5.

![Architecture](/README/artelevate.jpg)


### Flask

This project takes the use of flask to a whole other level with use of it's standard library features that is `redirect`, `url_for`, `request` and many others.

I was able to use other flask libraries that is Flask-Login (Login manager) which had amazing features such as `login_required`, `current_user` and methods such as `is_authenticated` and `get_id`(which used to get the user id) also using amazing tricks to access user details from the database in the back-end with `current_user.id/name/whatever_you_wish_to_use`.

I was able to use Flask-WTF which is amazing for creating forms that can be used in the front-end which ensures security for the form data and also amazing integration with Jinja.

I was able to utilise the power of Flask-Uploads which assists with image upload, storage and and serving image files. This simplified the workflow and ensured specifically image files were uploaded to the platform. This ensures image file extensions such as `jpg`, `jpeg`, `png` and `gif` are only added to the platform.

Finally, I was able to use Flask-Migrate which I used to monitor changes made to the database schema and this help me update changes such as adding a column to an existing table or even adding a whole new table. These are the commands used `flask db init`, `flask db migrate -m "Message"` and `flask db upgrade`.

For future features, Use of `Flask-Mail` with an email service to send emails to artists when an order is made for their works.

### Select Screenshots

Home Page
![Home Page](/README/Screenshot%202024-05-09%20035904.png)

Login and Register

![Login](/README/Screenshot%202024-05-09%20161201.png)

![Register](/README/Screenshot%202024-05-09%20161252.png)

Artist Profile and Upload Artwork page

![Profile](/README/Screenshot%202024-05-09%20162213.png)

![Upload](/README/Screenshot%202024-05-09%20162442.png)

Favorites

![Favorites](/README/Screenshot%202024-05-09%20161612.png)

Cart

![Cart](/README/Screenshot%202024-05-09%20161741.png)

Checkout

![Checkout_1](/README/Screenshot%202024-05-09%20161927.png)

![Checkout_2](/README/Screenshot%202024-05-09%20162007.png)

### Author

* Ruhinda Roderick Izooba <rickyruhinda@gmail.com>

