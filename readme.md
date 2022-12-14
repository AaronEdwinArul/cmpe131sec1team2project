# Spartsapp - The blog for all SJSU students!
> The online platform where users can create an account, post messages with images and interact with other users. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-and-libraries-used)
* [Requirements](#requirements)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- This application is a social media platform where users can share their messages with each other.
- We hope to make SJSU more connected through this app exclusively for students.


## Technologies and Libraries Used
- IDE such as Ubuntu(WSL) or VSCode
- Python3.10
- Flask
- SQLAlchemy
- flask-wtf
- flask-login
- flask-sqlalchemy


## Requirements
- Login (Michael Xiao)
- Logout (Aaron Arul)
- Create new account (Brandon Yu)
- Delete account (Vincent Cruz)
- User home page (user can see messages of users they follow) (Aaron Arul)
- Send message to followers (Brandon Yu)
- Post image with message (Brandon Yu)
- Like messages (Aaron Arul)
- Search for user (Michael Xiao)
- Follow user (Michael Xiao)


## Setup
Clone this repository by copying the link to this repository and pasting it into the terminal when running git clone, and navigate to myProject and run "python3 run.py" to run application

## Usage
The first step to using our platform is to create an account, without an account the user cannot login to access anything beyond the base page. The password and e-mail must satisify certain guidelines in order for the account creation to be successful. After creating an account, the user's data will be stored into the database. The user then goes to login page to enter their login information, if it’s within the database the website will reroute them to the home page. From the home page user will be able to access all sorts of information and links, searching for users, looking at their own profile, making a new post w/image, viewing followers, and also the feed of all posts of users in the database. To make a post, the user can click the ‘Make a post!’ option on the home page and be redirected to the post page where they can write a message for the post and attach an image for the post that they are making. As soon as the user posts this message, they will be sent to the feed page with all users' posts. If the user clicks on the search button on the sidebar, they’ll be rerouted to a page where they can search for other existing users in the database. If the username the user enters does not match a user in the database, they’ll be asked to search again. This search is case sensitive. After finding another existing user, the user can decide to follow/unfollow that user. This information will be displayed under the “View Followers” tab on the home page. The user profile page can be accessed by clicking the Profile button on the sidebar to access account details. The user can click the Feed button to view posts of all users accounts in the database. The user can choose to update their bio and other user account information on the profile page, where the bio must adhere to certain guidelines. The user can choose to delete their account on their profile page by clicking the Delete Account option, followed by entering their password to ensure their removal from the database. Finally, if the user decides to logout, the button will be on the left column of the website, which would direct them back to the base page of our website.

## Acknowledgements
- Aaron Arul (@AaronEdwinArul) (Team Lead)
- Vincent Cruz (@dominiccaoile)
- Brandon Yu (@brndonyu)
- Michael Xiao (@MichaelXiao9625)



