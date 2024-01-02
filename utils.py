import nltk
from nltk.corpus import words
from nltk.corpus import wordnet

try:
    # Check if the NLTK resources are already installed
    nltk.data.find('corpora/words')
    nltk.data.find('corpora/wordnet')
except LookupError:
    # Download the NLTK resources if they are not installed
    nltk.download('words')
    nltk.download('wordnet')

# Set of English words
english_words = set(words.words())

def is_human_readable(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    # Count the number of recognized words
    recognized_words = sum(1 for word in words if word.lower() in english_words or wordnet.synsets(word, lang='eng'))
    # Check if at least 50% of the words are recognized
    return recognized_words / len(words) >= 0.5