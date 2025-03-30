# AGI-ny Aunt

Aginy Aunt: A therapy website powered by ChatGPT. This is a Python web app using a Django framework with a sqlite3 database, which has been optimized for mobile.

### Video Demo: [https://www.youtube.com/watch?v=mAgBsdmz1tg](https://www.youtube.com/watch?v=mAgBsdmz1tg)

## Installation

Follow these steps to set up Aginy Aunt on your local machine:

### Prerequisites

-   Python 3.6+
-   pip package installer
-   A valid OpenAI API key

### Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/mattbailey1991/aginyaunt.git
    cd aginyaunt
    ```

2.  **Set up the environment variables:**

    -   Create a `.env` file inside the `aginyaunt/aginyaunt` directory.
    -   Add your OpenAI API key and Django SECRET_KEY to the `.env` file.

        ```
        OPENAI_API_KEY='your_openai_secret_key'
        DJANGO_SECRET_KEY='your_django_secret_key'
        ```

    **Important:** Ensure you replace `'your_openai_secret_key'` and `'your_django_secret_key'` with your actual keys.

3.  **Install the dependencies:**

    While no `package.json` was found, this is a Django project, so you'll need to install the Python dependencies.  It's highly recommended to use a virtual environment.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows

    pip install Django
    pip install openai
    pip install python-dotenv
    ```

4.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Aginy Aunt website.

## Key Features

*   **ChatGPT-Powered Therapy:** Utilizes the OpenAI API to provide therapeutic conversations.
*   **Mobile-Optimized:** Designed for a seamless experience on mobile devices.
*   **Chat History:** Stores chat history for users to review previous sessions.
*   **User Authentication:** Uses Django's built-in user authentication system.

## Project Structure

The main app for the project is located in `/aginyaunt/aginy`. The major files are:

### HTML Files

*   `layout.html`: Website layout and nav bar
*   `index.html`: Home page for the website, where a new chat can be started
*   `chat.html`: Live chat with Aginy Aunt bot
*   `history.html`: Table of all previous chat histories for user. Hovering on a row will highlight it, and clicking will resume the chat.

### Python Files

*   `chatbot.py`: Defines the `OpenAIBot` class which opens a connection to the OpenAI API using a secret key which must be saved in the .env file and a message history (either initial prompt if accessed from homepage or full history if accessed from history page). The bot is initialized with a system prompt which tells it to act like a therapist, ask lots of questions, and recommend CBT techniques. Using the chat method with a prompt will fetch a completion from the OpenAI API.
*   `models.py`: Defines `ChatHistory` model class in db.sqlite3. This has four fields: i) user - django user object of the current session; ii) datetime - date and time of chat; iii) title - first 50 characters of initial prompt; iv) message_history - text field which stores full message history as a JSON string.
*   `dbmanager.py`: `get_all_chats` pulls all ChatHistories for the logged in user from db.sqlite3. `get_chat_history` pulls a particular ChatHistory by the primary key. `save_chat` will save a new ChatHistory to the database using session data for current chat.
*   `views.py`:
    *   `chat/`: Handles the chat page with two routes: i) 'chat' will send prompt to OpenAI API, save message history to session, and then either render a new chatpage (if called from homepage) or return a JSON (if called by AJAX request on page); ii) 'view' will save historical message history to session and render the chatpage.
    *   `history/`: Runs `get_all_chats` in dbmanager.py and renders table of all chat histories.

### JavaScript Files

*   `chatpage.js`: i) parses chat history into user and bot messages, assigns the correct css class and then adds to DOM; ii) continuing a chat using 'tell me more' will submit an AJAX request to chat/; iii) while thinking, will display "Aginy Aunt: ..." to make the website appear more responsive.
*   `historypage.js`: Gets ChatHistory id when a user clicks on a line in their history table, and sends to /chat/.
