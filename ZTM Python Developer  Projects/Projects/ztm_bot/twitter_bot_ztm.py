import tweepy
import time
import pdb

auth = tweepy.OAuthHandler('A3lrgGPzzWE9KYrlGk9Xh2SmI', 'r0wnbWVu9r6JouesoItxtG1JZvCXfjAKk5GpxIEIkgeQWp654i')
auth.set_access_token('2193699638-Poyc99qg29HgTpyETodYVz04c5WCodOuBGNKzBb', 'PFGqloYDWqNEqGU1uDhn4UkZgTNzEebySESDyMIShYMxp')

api = tweepy.API(auth)
user = api.me()

print(user.name)
print(user.screen_name)
print(user.followers_count)

public_tweets = api.home_timeline() 

for tweet in public_tweets:
  print(tweet.text)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(300)
    
        
# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Marcelo':
  # or if follower.followers_count() > 100:
    follower.follow()
    break
    
search_string = "Python"
numberOfTweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
    try:
        tweet.favorite() #or .retweet()
        print("That is quite interesting!")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    
