# Mail-News
It sends newses to you.

# About
If you run this program, it collects newses from news-api.
Then, send the information to you with email.

# Usage
First, what you have to do is setting data.
- /letter/template.py
    - You can set data about creating email. You can set subject of
      email, and the sentence that be inserted at the end.
      
- /mailer/metadata.py
    - You have to set data about sending email. You can see more details
    from the file.
      
- /news_api/news_api.py
    - You have to set data about collecting news. You can see how you can get
    the data about news-api from https://newsapi.org .
      
Then, if you run the main.py, you can see the email.
