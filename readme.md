# Spartsapp - The blog for all SJSU students!
> The online platform where users can create an account, post messages with images and interact with other users. 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Requirements](#requirements)
* [Setup](#setup)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- This application is a social media platform where users can share their messages with each other.
- We hope to make SJSU more connected through this app exclusively for students.


## Technologies Used
- Python3.10
- Flask
- Flask WTForms
- SQLAlchemy


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
Clone this repository and navigate to myProject and run "python3 run.py" to run application

## Usage
First step to using our platform is to create an account, without an account the user cannot login to access anything beyond the base page. After creating an account, the users data will be stored into the database. The user then goes to login page to enter their login information, if it’s within the database the website will reroute them to the home page. From the home page user will be able to access all sorts of information and links, searching for users, looking at their own profile and viewing their followers and posts of the accounts they follow. To make a post, the user can click the ‘Make a post!’ option on the home page and be redirected to the post page where they can write a message for the post and attach an image for the post that they are making. If the user clicks on the search button on the sidebar, they’ll be rerouted to a page where they can search for other existing users in the database. If the username the user enters does not match a user in the database, they’ll be asked to search again. This search is case sensitive. After finding another existing user, the user can decide to follow/unfollow that user. This information will be displayed under the “View Followers” tab on the home page. The user profile page can be accessed by clicking the Profile button on the sidebar to access account details. The user can click the Feed button to view poss of all accounts in the database. Finally, if the user decides to logout, the button will be on the left column of the website, which would direct them back to the base page of our website

## Acknowledgements
- Aaron Arul (@AaronEdwinArul) (Team Lead)
- Vincent Cruz (@dominiccaoile)
- Brandon Yu (@brndonyu)
- Michael Xiao (@MichaelXiao9625)



