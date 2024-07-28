import wikipedia

def scrape(name='Microsoft', sentences=2):
    return wikipedia.summary(name, sentences)