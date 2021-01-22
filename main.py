from letter.letter import Letter
from news_api.news_list import NewsList
from mailer.metadata import Metadata
from mailer.mailer import Mailer

newses = NewsList()
letter_body = newses.to_contents()

letter = Letter(letter_body)
letter.add_data(Metadata.email, Metadata.to_email)

with Mailer() as mailer:
    mailer.connection.starttls()
    mailer.wrapped_login()
    mailer.wrapped_sendmail(letter.as_string())
