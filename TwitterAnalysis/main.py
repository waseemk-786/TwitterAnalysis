from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


consumer_key = 'kjnuVeyEy4yOk4KUFoDx0Jf3J'
consumer_secret = 'g1fVqAZYBdU9EN9fazzLFrcOsmJ6P5lfOeqImWKCjYC8KAWVPE'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)


api = tweepy.API(auth)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search_tweets(q=search_tweet, tweet_mode='extended')
    # tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        t.append(tweet.full_text)


    return jsonify({"success":True,"tweets":t})
if __name__ == '__main__':
    app.run()