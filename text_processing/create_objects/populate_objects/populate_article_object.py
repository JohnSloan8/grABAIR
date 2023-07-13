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
            default=default_article_object,
            number="sg"
        )

    elif word == "na":
        article_object = POSArticle(
            word="na",
            default=default_article_object,
            number="pl"
        )

    return article_object
