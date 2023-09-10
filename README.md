# Aginy Aunt
#### Video Demo: https://www.youtube.com/watch?v=mAgBsdmz1tg

Aginy Aunt: a therapy website powered by ChatGPT. This is a python web app using a Django framework with a sqlite3 database, which has been optimised for mobile.

#### Setup: Download the repo and save a .env file inside the main project folder (aginyaunt/aginyaunt) with OpenAI API secret key. This must be called OPENAI_API_KEY='secretkey'. You also need to include a Djago SECRET_KEY='key' inside the same file.

#### Description:

/aginyaunt/aginy is the main app for the project. The major files are

layout.html: Website layout and nav bar
index.html: Home page for the website, where a new chat can be started
chat.html: Live chat with Aginy Aunt bot
history.html: Table of all previous chat histories for user. Clicking on a row will resume the chat.

models.py: Define ChatHistory model class in db.sqlite3.

dbmanager.py: get_all_chats pulls all ChatHistories for the logged in user from db.sqlite3. get_chat_history pulls a particular ChatHistory by the primary key. save_chat will save a new ChatHistory to the database using session data for current chat.

views.py: 
    chat/: Handles the chat page with two routes: i) 'chat' will send prompt to OpenAI API, save message history to session, and then either render a new chatpage (if called from homepage) or return a JSON (if called by AJAX request on page); ii) 'view' will save historical message history to session and render the chatpage.

    history/: Runs get_all_chats and renders table of all chat histories.   

chatpage.js: i) parses chat history into user and bot messages, assigns the correct css class and then adds to DOM; ii) continuing a chat using 'tell me more' will submit an AJAX request to chat/; iii) while thinking, will display "Aginy Aunt: ..." to make the website appear more responsive.

historypage.js: Gets ChatHistory id when a user clicks on a line in their history table, and sends to /chat. 