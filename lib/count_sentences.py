import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):  # renamed from is_period to is_sentence
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0
        
        text = self.value.replace("...", ".")
        sentences = re.split(r'[.?!]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)
