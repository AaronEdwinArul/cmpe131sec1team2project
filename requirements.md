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

6. Send message to followers

Precondition: The user has followers

Trigger: The user clicks on follower that will bring them to a message box where they can type their message

Primary Sequence: 

  a. User clicks on follower
  b. User is prompted a "message" link
  c. User is redirected to a private messaging conversation with follower
  d. User clicks on messager box to input their message
  e. User presses "enter" and the message is sent to follower

Primary Postcondition: The follower recieves the message and can view the message along with who it's from

Alternative Sequence: 

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

10. Follow user

Precondition: The user has an account and can see other user's account

Trigger: The user click on "follow" button under a certain user's profile

Primary Sequence:

  a. The user clicks on a certain user
  b. User is prompted with a "follow" button under that user
  c. User clicks "follow" and is now following user
  d. System shows a symbol indicating that the user is following

Primary Postcondition: The user is now following another user and can see their activities

Alternative Sequence:

User is already blocked by a certain user
  a. The user clicks on a certain user
  b. User is prompted with a "blocked" sign under that user
  c. User cannot follow as that user does not permit them to follow