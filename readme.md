# Social Media Application
- Aaron Arul (@AaronEdwinArul) (Team Lead)
- Vincent Cruz (@dominiccaoile)
- Brandon Yu (@brndonyu)
- Michael Xiao (@MichaelXiao9625)

Ethical Implications:
- For this assigned project, we are tasked with constructing a social media platform where users can create an account to make their own posts, and share them with other users. This opens the door to fostering interactions within the community, no matter how far apart people are. 
When the project was assigned, the idea of creating a website where users could view each others’ posts emphasized the need for ensuring peoples’ ability to voice their opinions, as well as their artwork in the form of images. In order to do this, there must be ways to get peoples’ voices heard, preferably to large audiences so that they may be valued in society. This can be done through the construction of a web application that can showcase different stories and pictures from around the world in the form of posts. This leads to a focus in strengthening our ethical responsibilities of making sure user’s posts are shared with their audience. In order to complete this task, we learned how to build a framework for a website to house these aspects of a social media platform. Therefore, it is necessary to work on our professional responsibilities of making a website that is reliable, easy-to-use, and convenient for users to create and access other users’ posts. The impact of engineering these solutions on a global scale would be to connect different groups of people by their interests and culture. This would help communicate messages enclosed in posts at a faster rate of time, and in turn can even help boost the economy when it comes to guiding peoples’ financial decisions. Creating a social media platform may also help the environment, in cases where people bring awareness for preserving the natural state of ecosystems through posts with thoughtful messages, and images of wildlife and nature; these can be created and shared by the social media platform to spread the message among many. Overall, making a social media platform as a web application would help society progress, as well as make it more connected and help its members become more up to date.

Implementation:
- First step to using our platform is to create an account, without an account the user cannot login to access anything beyond the base page
- After creating an account, the users data will be stored into the database
- The user then goes to login page to enter their login information, if it’s within the database the website will reroute them to the home page
- From the home page user will be able to access all sorts of information and links, such as posting on their blog, searching for users, looking at their own profile     and statistics, and viewing their followers and liked posts
- To make a post, the user can click the ‘Make a post’ option on the home page and be redirected to the post page where they can write a message for the post and      
  attach an image for the post that they are making.
- If the user clicks on the search button, they’ll be rerouted to a page where they can search for other existing users in the database. If the username the user 
  enters does not match a user in the database, they’ll be asked to search again. This search is case sensitive. After finding another existing user, the user can   
  decide to follow/unfollow that user. This information will be displayed under the “View Followers” tab on the home page
- The user profile page can be accessed by clicking the Profile button on the sidebar to access account details.
- The user can click the posts page to see a list of posts that they made.
- Finally, if the user decides to logout, the button will be on the left column of the website, which would direct them back to the base page of our website


Necessary libraries to run project:
- flask, flask_login, flask_wtf, wtforms, werkzeug.security, bootstrap (for styling)


Requirements implemented for Milestone 2:
1. Login (Michael Xiao)
2. Logout (Aaron Arul)
3. Create new account (Brandon Yu)
4. delete account (Vincent Cruz)
5. User home page (Aaron Arul)
6. Send message to followers (Brandon Yu)
7. Post image with message (Brandon Yu)
8. Like messages (Aaron Arul)
9. Search for user (Michael Xiao)
10. Follow user (Michael Xiao)
