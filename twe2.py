#QUE 1-
print("An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread.")
import tweepy
access_token=1002830618831478785-KGYSD9LlrkiL4qSJbIortGaPM2JfYa
print (access_token)


#Que 2
import socket
addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')
addr3 = socket.gethostbyname('facebook.com')
print(addr1, addr2, addr3)




#QUE 3-
from twe1 import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api = tweepy.API(oauth)
print (api.search("#technical"))

api=tweepy.API(oauth)
user=api.search('#tech')


# QUE4-
print("Application Program Interfaces, or APIs, are commonly used to retrieve data from remote websites. Sites like Reddit, Twitter, and Facebook all offer certain data through their APIs. To use an API, you make a request to a remote web server, and retrieve the data you need ,A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily. For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself. Typically a library will only offer one area of functionality (processing images or operating on zip files)")
print("Python library is a collection of functions and methods that allows you to perform lots of actions without writing your own code.")


#QUE5-
from twe1 import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth = tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api= tweepy.API(oauth)
print(api.search("#sanju"))
user=api.get_user('@TarunKu44483398')
print(user.screen_name)
print(user.followers_count)
