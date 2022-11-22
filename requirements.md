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

7) Post image with message
Pre-condition: User is attempting to post a message and has an image they would like to attach to the message.
Trigger: User clicks a button that allows them to upload an image.

Primary Sequence
1. User writes a message to post.
2. User prompts system to attach an image through a button.
3. System prompts user to select an image.
4. User uploads an image.
5. System will save the image to post with the message.
6. User will post the message that now has an image attached.

Primary Postconditions
The message posted by the user will show both the text and image when posted. Other users will also be able to see the text and image together.

Alternate Sequence
The user uploads a file that is not an image
  a. The system will display an error message to the user
  b. The system prompts the user to submit a file with a valid type


9) Search for user
Pre-condition: User wants to find another user on the site.
Trigger: User clicks on a search bar that allows them to type in a prompt to find other users.

Primary Sequence
1. User clicks on the search bar.
2. User enters a name that they would like to search for.
3. System finds a name that matches what was entered.
4. System displays the page of the user that was found.

Primary Postconditions
The user is now able to view the page of the user whose name was entered into the search bar.

Alternate Sequence
The name being searched for does not exist in the database
  a. The system will display an error stating that the entered user does not exist
