from decouple import config
import tweepy

CONSUMER_KEY = config('CONSUMER_KEY', default='')
CONSUMER_SECRET = config('CONSUMER_SECRET', default='')

class TwitterClient():
  """ Implements counting capabilities to Twitter API
  """
  
  def __init__(self):
    self.api = tweepy.API(tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET))
    
  def count(self, term):
    """
    Count how many results were found for a given term.
    
    Twitter's API has limit rates for query Tweets, those limits only allow
    us to get tweets from previous 7 days (standard)
    """
    tweets = self.api.search(term, count=500, result_type='recent')
    
    return len(tweets)