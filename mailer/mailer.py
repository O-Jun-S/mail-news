# My own modules
from .metadata import Metadata

# Other modules
import smtplib


class Mailer:
    def __init__(self):
        pass

    def __enter__(self):
        self.connection = smtplib.SMTP(
            Metadata.smtp_server,
            Metadata.smtp_server_port
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        self.connection.close()

    def wrapped_login(self):
        email = Metadata.email
        password = Metadata.password
        self.connection.login(
            user=email,
            password=password,
        )

    def wrapped_sendmail(self, letter):
        self.connection.sendmail(
            from_addr=Metadata.email,
            to_addrs=Metadata.to_email,
            msg=letter,
        )
