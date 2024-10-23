import re

class EnglishTextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.word_freq = {}

    def tokenize(self):
        clean_text = str(re.sub(r'[^\w\s\n]', '', self.text))
        self.tokens = (clean_text.lower()).split()
        
    def analyze_word_freq(self):
        if not self.tokens:
            self.tokenize()
        for token in self.tokens:
            self.word_freq[token] = self.word_freq.get(token, 0) + 1

    def get_top_word(self):
        if not self.word_freq:
            self.analyze_word_freq()
        biggest = ("", 0)

        for key, value in self.word_freq.items():
            if value > biggest[1]:
                biggest = (key, value)
        return biggest