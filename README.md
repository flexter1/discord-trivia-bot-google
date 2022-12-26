# discord-trivia-bot-google

This software allows you to automatically answer the questions in discord-trivia

How does it work:

1) Setting your config file:
   
discord_token - your discord token for answering and parsing messages
   
chat_id - chat id where you need to answer and parsing messages
   
author_name - TRIVIA-Author name. For example, if DogeElon#4434 will survey the trivia, you need to write "DogeElon" to config
   
last_author_message - The last message that has been sent by author. It's to avoid accidentally answering the last message

2) Write "pip install -r requirements.txt" in the cmd
3) Start the soft


Working procedure:
1) Parsing NEW messages from author every second
2) If there is a new message, software automatically searching the answer in google
3) If there is an answer, you automatically answer it to the discord. If it not - you just passing it
