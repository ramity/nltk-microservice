from flask import Flask
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import requests
import time
import gzip

app = Flask(__name__)

@app.route("/sentiment", methods=["POST"])
def sentiment(text):

    """
    Converts incoming text into sentiment score.

    Args:
        { text }

    Returns 
        { neg, neu, pos, compound }
    """

    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)

    return scores

@app.route("/sentiment/multiline", methods=["POST"])
def sentiment(text):

    """
    Converts incoming multiline text into an array of setence sentiment scores.

    Args:
        { text }

    Returns 
        { [] { neg, neu, pos, compound } }
    """

    sia = SentimentIntensityAnalyzer()
    sentences = sent_tokenize(text)
    scores = [sia.polarity_scores(sentence) for sentence in sentences]

    return scores

@app.route("/frequency/word", methods=["POST"])
def word_frequency(text):

    """
    Converts incoming text into token counts.

    Args:
        { text }

    Returns 
        { token: count, ..., token: count }
    """

    tokens = word_tokenize(text)
    frequency = Counter(tokens)

    return frequency

@app.route("/tokenize/words", methods=["POST"])
def tokenize_words(text):

    """
    Converts incoming text into array of words.

    Args:
        { text }

    Returns 
        [ word_0, word_1, ... , word_n ]
    """

    words = word_tokenize(text)

    return words

@app.route("/tokenize/sentences", methods=["POST"])
def tokenize_sentences(text):

    """
    Converts incoming text into array of sentences.

    Args:
        { text }

    Returns 
        [ sentence_0, sentence_1, ... , sentence_n ]
    """

    sentences = sent_tokenize(text)

    return sentences

@app.route("/scrape", methods=["POST"])
def scrape(url):

    """
    Scrapes the incoming URL, gzips and saves the response.

    Args:
        { URL }

    Returns 
        { filepath }
    """

    response = requests.get(url)
    current_time = time.time()
    file_path = f"/scrapes/{current_time}-{url}-response.gz"
    compressed_response = gzip.compress(response.content)

    with open(file_path, "wb") as f:
        f.write(compressed_response)

    return file_path








if __name__ == "__main__":
    text = input("Enter the text for sentiment analysis: ")
    scores = sentiment(text)
    print(scores)
