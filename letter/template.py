class Template:
    """You can change subject of letter and end_sentence."""
    subject = "Today News"
    end_sentence = "Have a nice day!"

    @staticmethod
    def attach_end_sentence(body):
        """As the name, it attaches end-sentence."""
        arranged_body = body
        arranged_body += "\n\n\n"
        arranged_body += Template.end_sentence

        return arranged_body
