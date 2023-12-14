articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
     articles = []
     if letter_case:
         for article in articles_dict:
             for keys, value in article.items():
                 if key in str(value):
                         articles.append(article)
     else:
         for article in articles_dict:
             for keys, value in article.items():
                 if key.lower() in str(value).lower():
                         articles.append(article)
     return articles   