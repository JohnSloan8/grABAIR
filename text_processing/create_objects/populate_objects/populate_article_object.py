from models.articles import POSArticle, POSDefaultArticle


def populate_article_object(word):

    default_article_object = POSDefaultArticle(
        word="an",
        sg="an",
        pl="na"
    )

    if word == "an":
        article_object = POSArticle(
            word="an",
            POS="article",
            number="sg",
            default=default_article_object
        )

    elif word == "na":
        article_object = POSArticle(
            word="na",
            POS="ARTICLE",
            number="pl",
            default=default_article_object
        )

    return article_object
