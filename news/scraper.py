import feedparser

def fetch_google_news():

    url = "https://techcrunch.com/feed/"

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:10]:

        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })

    return articles
