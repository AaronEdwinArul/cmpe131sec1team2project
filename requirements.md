## Aaron Arul 014807611
## Brandon Yu 014810185
## Michael Xiao 014115361
## Vincent Cruz 012541139

## Functional Requirements

1. Login (Michael Xiao)
2. Logout (Aaron Arul)
3. Create new account (Brandon Yu)
4. delete account (Vincent Cruz)
5. User home page (user can see messages of users they follow) (Aaron Arul)
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

5. User home page (user can see messages of users they follow)
- **Pre-condition:** The user is logged in successfully. 
- **Trigger:** The user clicks the 'Home Page' button.
- **Primary Sequence:**
  1. System directs user to the home page.
  2. User is shown other options on home page
  3. User can click home page button on sidebar again to redirect to page that they are on (refreshing page)
  4. User can see 'Make a Post', 'View Followers' and 'Feed' buttons
  5. User can see the posts of accounts that they follow
- **Primary Postconditions:** The user is on the starting page of the application directed to them after logging in
- **Alternate Sequence:** 
  1. After logging in for the first time, the new user is presented the home page with "Make a Post!", "View Followers", and "Feed" buttons.
  2. The new user scrolls down and sees no posts in the "See what your firends are up to" area of the home page
  
  
  
6. Post message to followers
- **Pre-condition:** The user is signed in
- **Trigger:** The user clicks "Make a Post!" button
- **Primary Sequence:** 
  1. The user is redirected to the "Make a Post!" page
  2. The user enters text into the message box
  3. The user may insert a link for an image (.png file) if they want to for the message
  4. The user clicks the "Post" button
  5. The user is directed to the Feed page
- **Primary Postconditions:** The post is viewable on feed and home page of user, and to other accounts in the feed
- **Alternate Sequence:** 
  1. User enters in a message over 500 characters
  2. System displays error message that message for post is too long
  


7. Post image with message
- **Pre-condition:** User is on the "Make a Post!" page.
- **Trigger:** User clicks post button on the "Make a Post!" page after inserting a link for the image they would like to add to the post they are creating.
- **Primary Sequence**
    1. User is redirected to the feed page
    2. User can view their new post at the bottom of the feed page which has the post with the image
- **Primary Postconditions:**
The post created by the user will show both the text and/or image when posted. Other users will also be able to see the text and image together.
- **Alternate Sequence:**
    1. The user uploads a file that is not an image
    2. The system will upload a blank non-readable png


8. Like messages
- **Pre-condition:** The user is logged in, on the home or feed page, and has not liked the message that they want to like
- **Trigger:** The user clicks on the like button for the post they are viewing
- **Primary Sequence:**
    1. User is on the home or feed page of the application
    2. User selects the like button for the post they are viewing on the current page
    3. System increments like count for the post and displays updated like count to user
    4. System displays a symbol next to post indicating user liked that specific post
- **Primary Postconditions:** The user is on the home or feed page of the application
- **Alternate Sequence:** 
    1. User clicks on like button for a post that they have already liked (to unlike)
    2. System decrements like count for the post and displays updated like count to user

9. Search for user 
- **Pre-condition:** User wants to find another user on the site.
- **Trigger:** User clicks on a search button on the sidebar
- **Primary Sequence:**
    1. User is redirected to the search page
    2. User enters a name that they would like to search for in the search bar.
    3. System finds a name that matches what was entered.
    4. System displays the link of the user profile that was found.
- **Primary Postconditions:** The user is now able to view the link of the user profile whose name was entered into the search bar.
- **Alternate Sequence:**
    -The name being searched for does not exist in the database
    1. The system will display an error stating that the entered user does not exist


10. Follow user 
- **Pre-condition:** The user has an account and can see other user's account
- **Trigger:** The user clicks on "follow" button under searched user's profile
- **Primary Sequence:**
    1. The user clicks on "Follow" button
    2. The user is redirected to the user profile page of the user that they just followed.
    3. The button on the bottom of this page is displaying "Unfollow"
    4. There is message displaying that current user is following searched user
- **Primary Postconditions:** The user is now following another user
- **Alternate Sequence:**
    1. User is already following the searched user



11. User Profiles 
- **Pre-condition:** The user is logged in and is currently on the home page tab
- **Trigger:** User clicks on the profile button 
- **Primary Sequence:**
    1. User clicks profile button
    2. User is sent to profile page
    3. Profile tab contains miscellaneous information such as DOB, Location, Bio, etc.
    4. User clicks on "Edit Profile" button
    5. User is able to edit information of this miscellaneuos information and save it using "Save" button
    6. User is redirected to their profile page
- **Primary Postconditions:** The user is on the profile page
- **Alternative Sequence:**
    1. User clicks profile button
    2. User is sent to profile page
    3. Profile tab contains miscellaneous information such as DOB, Location, Bio, etc.
    4. User clicks on "Edit Profile" button
    5. User is able to edit information of this miscellaneuos information
    6. User enters a bio more than 200 characters
    7. User is displayed an error message when trying to click "Save"
   


12. Visualize connections of all users
- **Pre-condition:** The user is logged in already, and is on the profile page of another user
- **Trigger:**  The user clicks another user's profile link
- **Primary Sequence:** 
    1. User is on the profile page of another user
    2. User clicks "Follows" button
    3. User is sent to the profile of the user that they just followed
- **Primary Postconditions:** The user is on the profile page of another user
- **Alternative Sequence:**
    1. User A clicks User B's profile
    2. User A is already following User B, can only unfollow

