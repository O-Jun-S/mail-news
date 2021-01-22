# My own package
from .template import Template
from letter.keys import Keys

# Other modules.
from email.mime.text import MIMEText
from email.utils import formatdate


class Letter(MIMEText):
    def __init__(self, body):
        arranged_body = Template.attach_end_sentence(body)
        super().__init__(arranged_body)

    def add_data(self, from_address, to_address):
        self.set_metadata(from_address, to_address)
        self.set_subject()

    def set_metadata(self, from_address, to_address):
        self[Keys.from_key] = from_address
        self[Keys.to_key] = to_address
        self[Keys.date_key] = formatdate()

    def set_subject(self):
        subject = Template.subject
        self[Keys.subject_key] = subject
