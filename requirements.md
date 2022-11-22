## Aaron Arul 014807611
## Brandon Yu
## Michael Xiao 014115361
## Vincent Cruz
## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login
2. Logout
3. Create new account
4. delete account
5. User home page 
6. Send message to followers 
7. Post image with message 
8. Like messages 
9. Search for user 
10. Follow user 
11. User profiles 
12. Visualize connections of all users 

## Non-functional Requirements

1. Multilingual support 
2. Only expected to work on Google Chrome 
3. Return results for user after search within 10 seconds
4. User data will be stored safely through hashing 

## Use Cases

2. Like messages
**Pre-condition:** The user is logged in, on the posts tab, and has not liked the message that they want to like

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

- **Trigger:** The user clicks the 'Home Page' button, and is also directed to the home page upon logging in.

- **Primary Sequence:**
  
  1. System prompts user with message "Welcome to home page"
  2. User clicks ok on welcome message and is shown other options on home page
  3. User can click home page button again to redirect to page that they are on (refreshing page)
  4. User can 'view messages' icon, 'add post' icon, 'settings' icon
  5. User selects home page 'statistics' button 
  6. System generates statistics of user's mutual friends, liked posts, and time spent on application by user 
  7. System displays statistics window on home page

- **Primary Postconditions:** The user is on the starting page of the application directed to them after logging in

- **Alternate Sequence:** 
  
  1. After logging in for the first time, user is presented with 'Welcome' message on home page
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

- **Pre-condition:** User wants to find another user on the site.

- **Trigger:** User clicks on a search bar that allows them to type in a prompt to find other users.

- **Primary Sequence:**
1. User clicks on the search bar.
2. User enters a name that they would like to search for.
3. System finds a name that matches what was entered.
4. System displays the page of the user that was found.

- **Primary Postconditions:**

The user is now able to view the page of the user whose name was entered into the search bar.

- **Alternate Sequence:**

The name being searched for does not exist in the database

  a. The system will display an error stating that the entered user does not exist


10. Follow user

- **Pre-condition:** The user has an account and can see other user's account

- **Trigger:** The user click on "follow" button under a certain user's profile

- **Primary Sequence:**

  a. The user clicks on a certain user
  b. User is prompted with a "follow" button under that user
  c. User clicks "follow" and is now following user
  d. System shows a symbol indicating that the user is following
  
- **Primary Postconditions:** The user is now following another user and can see their activities

- **Alternate Sequence:**

User is already blocked by a certain user
  a. The user clicks on a certain user
  b. User is prompted with a "blocked" sign under that user
  c. User cannot follow as that user does not permit them to follow
