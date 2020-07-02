from constants import *
import wikipedia
import nltk

LANG = "simple"

# Rating between 0 and 1
# Higher rating: more difficult/more letters on top and bottom row
def rateString(word):
    count = 0
    for char in list(word):
        if(char not in HOMEROW):
            count += 1
    return count / len(word)

# Returns a sorted list of tuples (sentence, rating)
def rateText(text):
    sentences = nltk.sent_tokenize(text)
    ratedSentences = []
    for s in sentences:
        r = rateString(s)
        ratedSentences.append((s, r))
    return sorted(ratedSentences, key=lambda sentence: sentence[1])

# Rate a wikipedia article
def rateArticle(article):
    wikipedia.set_lang(LANG)
    content = wikipedia.page(article).content
    return rateText(content)
