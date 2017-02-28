"Πρόβλημα με το encoding όταν τρέχει απευθείας. Όλα καλά όταν τρέχει μέσα απο το IDLE"
import tweepy
from tweepy import OAuthHandler

consumer_key = "pNKYrZwP9bSgrqgxmvAXhW7Pi"
consumer_secret = "MwyIIUGg2b0gbFXMhJidu4lpFRntYFqR1bxuIqidax2CKKP39h"
access_token = "828382368499118080-xCfhjOFrtTCz9iwc7TBu5K6PX8QiRJw"
access_secret = "IGbjqNm32JM46XQz8yfhpcqZ1wjEpD97Z7ESGIOPsPnQn"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

def get_tweets_count(twitter_name):
    tweets1 = api.user_timeline(screen_name = twitter_name, count = 10)
    tweets = [tweet.text for tweet in tweets1]
    words = 0
    for tweet in tweets:
        words = words + len(tweet.split())
    return words

user1 = raw_input("Type the username of the first person >> ")
user1_c = get_tweets_count(user1)
user2 = raw_input("Type the username of the first person >> ")
user2_c = get_tweets_count(user2)

if (user1_c > user2_c):
    print "Ο χρήστης {} έχει μεγαλύτερο αριθμό λέξεων στα tweets του!".format(user1)
elif (user1_c < user2_c):
    print "Ο χρήστης {} έχει μεγαλύτερο αριθμό λέξεων στα tweets του!".format(user2)
else:
    print "Ίδιος αριθμός λέξεων στα tweets των δύο χρηστών!"

a = input()
