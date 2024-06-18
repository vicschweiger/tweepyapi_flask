from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import tweepy
from tweepy import TweepyException

app = Flask(__name__)

API_KEY = 'K5kuPSlVJrVcSoE3QbvM4ZwQ2'
API_KEY_SECRET = 'W8t6RyVAROM2uW2RmED1n1btws9wWcFve4vRbqBf0w7whIt8Mb'
ACCESS_TOKEN = '138202719-B7rdr7QBphWPUIf69IzPf2Zf9SaR0vnnQLtvaQuI'
ACCESS_TOKEN_SECRET = '0kLc77XjyO390w4EMpOJSkbYhI4PaXnYffMn5DvKsaebT'

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    count = int(request.form['count'])
    try:
        tweets = api.search_tweets(q=query, count=count)
        results = [{"user": tweet.user.screen_name, "text": tweet.text} for tweet in tweets]
        return render_template('results.html', results=results, query=query)
    except tweepy.TweepyException as e:
        error_message = f"Erro ao buscar tweets: {str(e)}"
        return render_template('error.html', error_message=error_message)
    
if __name__ == "__main__":
    app.run(debug=True)
