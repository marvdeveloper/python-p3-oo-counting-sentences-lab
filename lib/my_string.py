import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0

        # Replace ellipses with a unique token so they don't split incorrectly
        text = self.value.replace('...', '<ELLIPSIS>')

        # Split on sentence-ending punctuation sequences (one or more of ! or ? or .)
        # but treat the ellipsis token as a sentence end too
        parts = re.split(r'[!?\.]+', text)

        # Filter out empty strings and count
        count = sum(1 for part in parts if part.strip())

        return count
