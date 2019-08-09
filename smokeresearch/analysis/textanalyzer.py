# Internal imports
import re
import os
from collections import Counter

# External imports
from nltk.corpus import stopwords

# CONSTANTS
ENGLISH = ('english', 'en')
SPANISH = ('spanish', 'es')


class TextAnalyzer():
    """Analyze the text from a research publication."""

    def __init__(self):
        pass

    def count_words(self, text: str) -> int:
        """Count number of words in the text."""
        return len(re.findall(r'\w+', text))

    def keywords(self, text: str, n: int = 6) -> list:
        """Extract the most frequent words (keywords) from the text.

        Returns:
            The n most frequent words in the text.
        """
        words = text.lower().split()
        words = self.remove_stop_words(words)
        words = filter(self.valid_keyword, words)
        c = Counter(words)
        return c.most_common(n)

    def frequency(self, text: str, keyword: str) -> int:
        """Count the frequency of a given keyword."""
        return text.lower().count(keyword.lower())

    def find_sentences(self, text: str, keyword: str) -> list:
        """Extract the sentences of the text containing a given keyword."""
        text = text.replace(os.linesep, ' ')
        # pattern = r'([^.]*?' + keyword + r'[^.]*\.) '
        # prog = re.compile(pattern, re.IGNORECASE)
        # result = prog.findall(text)
        result = [sentence + '.' for sentence in text.split('. ') if keyword.lower() in sentence.lower()]
        return result

    # def find_paragraphs(self, text: str, keyword: str) -> list:
    #     """Extract the paragraph of the text containing a given keyword."""
    #     sentences = self.find_sentences(text, keyword)
    #     result = []
    #     for s in sentences:
    #         pattern = r'([^.]*?' + s.replace('(', '\(').replace(')', '\)') + r'[^.]*\.)'
    #         print(pattern)
    #         prog = re.compile(pattern, re.IGNORECASE)
    #         result.append(prog.findall(text))
    #     return result

    def clean_sentence(self, s: str) -> str:
        s = s.replace(os.linesep, ' ')
        s = s.replace('\n', '')
        s = s.replace('- ', '-')
        s = s.lstrip()
        return s

    def valid_sentence(self, s: str) -> bool:
        return s != '' and s[0].isalpha() and s[0].isupper()

    def valid_keyword(self, keyword: str) -> bool:
        return keyword != '' and keyword[0].isalpha()

    def remove_stop_words(self, words: list) -> list:
        words = filter(lambda w: w not in stopwords.words(ENGLISH[0]), words)
        words = filter(lambda w: w not in stopwords.words(SPANISH[0]), words)
        return words
