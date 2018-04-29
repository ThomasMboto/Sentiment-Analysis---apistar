from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from vaderSentiment import SentimentIntensityAnalyzer


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}

def getAll(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    return vs

def getCompound(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    rating = vs["compound"]
    return {'score': rating}

def getNegative(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    rating = vs["neg"]
    return {'score': rating}

def getPositive(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    rating = vs["pos"]
    return {'score': rating}

def getNeautral(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    rating = vs["neu"]
    return {'score': rating}

routes = [
    Route('/', 'GET', welcome),
    Route('/getAll/{text}', 'GET', getAll),
    Route('/getCompound/{text}', 'GET', getCompound),
    Route('/getNegative/{text}', 'GET', getNegative),
    Route('/getPositive/{text}', 'GET', getPositive),
    Route('/getNeautral/{text}', 'GET', getNeautral),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
