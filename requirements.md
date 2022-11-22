## Aaron Arul 014807611
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

