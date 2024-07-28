import wikipedia


def scrape(name="Microsoft", sentences=2):
    return wikipedia.summary(name, sentences)


if __name__ == "__main__":
    print(scrape())
