import string
import re

def count_words(text):
    if not text:
        return 0
    else:
        text = re.sub(r"[^\wäöüÄÖÜßА-Яа-я'\s]", "", text)
        words = text.split()
        return len(words)
