from newspaper import Article
import requests

def get_article_content(url):

    # Follow redirect to get real article URL
    response = requests.get(url, allow_redirects=True)
    real_url = response.url

    article = Article(real_url)

    article.download()
    article.parse()

    return {
        "title": article.title,
        "text": article.text,
        "image": article.top_image,
        "publish_date": article.publish_date,
        "url": real_url
    }