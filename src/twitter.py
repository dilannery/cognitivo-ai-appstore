from decouple import config
import tweepy

CONSUMER_KEY = config('CONSUMER_KEY', default='')
CONSUMER_SECRET = config('CONSUMER_SECRET', default='')

class TwitterClient():
  
  
  def __init__(self):
    self.api = tweepy.API(tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET))
    
  def count(self, term):
    """
    Count how many results were found for a given term
    """
    tweets = self.api.search(term, count=500, result_type='recent')
    
    return len(tweets)