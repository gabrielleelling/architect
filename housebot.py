import tweepy
import linecache
import random
import os
import sys


consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def check(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

prefix = "pics/building"
suffix = ".jpg"

myList = list(range(1, 30))

# iterate base from 1 to (some number?) and make it into string using str()
base = myList[random.randint(0, 29)]

result = prefix + str(base) + suffix

if check('used.txt', prefix + str(base) + suffix):
    #rerun
	print("reloading") #this will loop forever if it reaches the end of its corpus
	os.execl(sys.executable, sys.executable, *sys.argv)
else:
	file = open("caption.txt")
	caption = linecache.getline("caption.txt", base)
	file.close()
	api.update_with_media(result, caption)
	f = open("used.txt", "a")
	f.write(result + '\n')
	f.close()
	print("Success!")