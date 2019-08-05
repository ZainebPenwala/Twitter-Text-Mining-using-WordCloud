from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import json
import requests
import re
from requests_oauthlib import OAuth1
from IPython.display import Image as im


api_key = '' # enter api key
api_secret_key = '' # enter api secret key
auth = OAuth1(api_key, api_secret_key)


url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=thevirdas&count=20"
ans=requests.get(url,auth=auth)
j_ans=json.loads(ans.text)
j_ans

#for text in j_ans:
 #   print(text["text"])
  #  print("\n")

raw_tweets = []
for tweets in j_ans:
    raw_tweets.append(tweets['text'])
raw_tweets

raw_string=''.join(raw_tweets)
no_links = re.sub(r'http\S+', '', raw_string)
no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)

words = no_special_characters.split(" ")
words = [w for w in words if len(w) > 2]  # ignore a, an, be, ...
words = [w.lower() for w in words]
words = [w for w in words if w not in STOPWORDS]
words

wc = WordCloud(background_color="white", max_words=2000)
clean_string = ','.join(words)
wc.generate(clean_string)

f = plt.figure(figsize=(15,15))
f.add_subplot(1,2, 2)
plt.imshow(wc, interpolation='bilinear')
plt.title('Twitter Generated Cloud', size=10)
plt.axis("off")
plt.show()

