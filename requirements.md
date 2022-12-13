## Aaron Arul 014807611
## Brandon Yu 014810185
## Michael Xiao 014115361
## Vincent Cruz 012541139

## Functional Requirements

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
11. User profiles (Vincent Cruz)
12. Visualize connections of all users (Vincent Cruz)

## Non-functional Requirements

1. Multilingual support 
2. Only expected to work on Google Chrome 
3. Return results for user after search within 10 seconds
4. User data will be stored safely through hashing 

## Use Cases

2. Like messages
- **Pre-condition:** The user is logged in, on the posts tab, and has not liked the message that they want to like

- **Trigger:** The user clicks on the like button for the post they are viewing

- **Primary Sequence:**
  1. User is on the posts tab of the application
  2. User selects the like button for the post they are viewing on the posts tab
  3. System increments like count for the post and displays updated like count to user
  4. System displays a symbol next to post indicating user liked that specific post

- **Primary Postconditions:** The user is on the posts tab of the application

- **Alternate Sequence:** 
  
  1. User likes a post that have already liked
  2. System decrements like count for the post and displays updated like count to user
  3. System displays a symbol next to post indicating user that they unliked the specific post


5. User home page
- **Pre-condition:** The user is logged in successfully. 

- **Trigger:** The user clicks the 'Home Page' button.

- **Primary Sequence:**
  
  1. System directs user to the home page and prompts user with message "Welcome to home page"
  2. User clicks ok on welcome message and is shown other options on home page
  3. User can click home page button again to redirect to page that they are on (refreshing page)
  4. User can see 'view messages' button, 'add post' button, 'settings' button
  5. User selects home page 'statistics' button 
  6. System generates statistics of user's mutual friends, liked posts, and time spent on application by user 
  7. System displays statistics window on home page
  8. User closes statistics window

- **Primary Postconditions:** The user is on the home page

- **Alternate Sequence:** 
  
  1. After logging in for the first time, user is presented with 'Welcome new friend' message on home page
  2. User selects ok on welcome message
  3. User continues to use application features via home page after logging in for the first time


6. Send message to followers

- **Pre-condition:** The user has followers

- **Trigger:** The user clicks on follower that will bring them to a message box where they can type their message

- **Primary Sequence:** 

  a. User clicks on follower
  b. User is prompted a "message" link
  c. User is redirected to a private messaging conversation with follower
  d. User clicks on messager box to input their message
  e. User presses "enter" and the message is sent to follower

- **Primary Postconditions:** The follower recieves the message and can view the message along with who it's from

- **Alternate Sequence:** 

User does not have any followers
  a. No followers appear
  b. No "message" button

User is blocked from messaging
  a. User clicks on follower
  b. User is prompted a "message" link
  c. User is redirected to a private messaging conversation with follower
  d. User clicks on messager box to input their message
  e. User presses "enter" but system blocks message from going through
  f. User is promted with system message that they cannot send messages to that follower


7. Post image with message

- **Pre-condition:** User is attempting to post a message and has an image they would like to attach to the message.

- **Trigger:** User clicks a button that allows them to upload an image.

- **Primary Sequence**
1. User writes a message to post.
2. User prompts system to attach an image through a button.
3. System prompts user to select an image.
4. User uploads an image.
5. System will save the image to post with the message.
6. User will post the message that now has an image attached.

- **Primary Postconditions:**

The message posted by the user will show both the text and image when posted. Other users will also be able to see the text and image together.

- **Alternate Sequence:**

The user uploads a file that is not an image

  a. The system will display an error message to the user

  b. The system prompts the user to submit a file with a valid type


9. Search for user

9. Search for user (Brandon Yu)
- **Pre-condition:** User wants to find another user on the site.

- **Trigger:** User clicks on a search bar that allows them to type in a prompt to find other users.

- **Primary Sequence:**
  1. User clicks on the search bar.
  2. User enters a name that they would like to search for.
  3. System finds a name that matches what was entered.
  4. System displays the page of the user that was found.

- **Primary Postconditions:** The user is now able to view the page of the user whose name was entered into the search bar.

- **Alternate Sequence:**

  The name being searched for does not exist in the database
  1. The system will display an error stating that the entered user does not exist


10. Follow user (Michael Xiao)
- **Pre-condition:** The user has an account and can see other user's account

- **Trigger:** The user click on "follow" button under a certain user's profile

- **Primary Sequence:**

  1. The user clicks on a certain user
  2. User is prompted with a "follow" button under that user
  3. User clicks "follow" and is now following user
  4. System shows a symbol indicating that the user is following
  
- **Primary Postconditions:** The user is now following another user and can see their activities

- **Alternate Sequence:**

  User is already blocked by a certain user
  1. The user clicks on a certain user
  2. User is prompted with a "blocked" sign under that user
  3. User cannot follow as that user does not permit them to follow

 11. User Profiles (Vincent Cruz)
- **Pre-condition:** The user has an account and is currently on the home page tab

- **Trigger:** User clicks on the profile button OR user clicks "save" buttom

- **Primary Sequence:**
  1. User is on home page
  2. User clicks profile button
  3. User is sent to profile tab
  4. Profile tab contains miscellaneous information such as DOB, Location, Bio, etc.
  5. User is able to input information of miscellaneuos information and save it using "save" button
    
- **Primary Postconditions:** The user is on the profile tab

- **Alternative Sequence:**
<<<<<<< HEAD

  1. After accessing the profile tab for the first time, the user is prompted with a "tutorial" (form of a pop-up or message)
  2. The tutorial goes over the different sections of the profile tab explaining what each section does
  3. Once tutorial is finished user selects "OK" 
=======
    1. After accessing the profile tab for the first time, the user is prompted with a "tutorial" (form of a pop-up or message)
    2. The tutorial goes over the different sections of the profile tab explaining what each section does
    3. Once tutorial is finished user selects "OK" 
>>>>>>> eeb821e8b9a542439f18c9cf6b7be91fdddfe209
   
   
12. Visualize connections of all users (Vincent Cruz)
- **Pre-condition:** The user is logged in already, and is on the profile tab of the application of another user

- **Trigger:**  The user clicks the "following" or "follows" button on another user's profile

- **Primary Sequence:** 
  1. User is on the profile tab of application of another user
  2. User clicks "following" or "follows" button
  3. User is sent to either the "following" or "follows" tab which shows who the other user is following or follows
    
- **Primary Postconditions:** The user is on the "following" or "follows" tab of the application of another user

- **Alternative Sequence:**
  1. User A clicks User B's profile
  2. User A receives a prompt stating User B has blocked them
  3. User A cannot access the profile tab of User B

