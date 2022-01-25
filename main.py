from math import perm
import requests
import json
import json
import datetime

def get_pushshift_data(ticker, after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?q=' + str(ticker) + '&after' + str(after) + '&before' + str(before) + '&subreddit=' + str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text, strict=False)
    return data['data']

def collect_subData(subm):
    subData = list()
    title = subm['title']
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"
    try:
        body = subm['selftext']
    except KeyError:
        body = ''
    author = subm['author']
    subId = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc'])
    numComms = subm['num_comments']
    permalink = subm['permalink']

    subData.append((subId, title, body, url, author, score, created, numComms, permalink, flair))



subStats = {}
subCount = 0
sub = 'wallstreetbets'
after = '1641960870'
before = datetime.time

data = get_pushshift_data(after, before, sub)

while len(data) > 0:
    for submission in data:
        collect_subData(submission)
        subCount += 1
    
    print(len(data))
    print(str(datetime.datetime.fromtimestamp((data[-1]['created_utc']))))
    after = data[-1]['created_utc']
    data = get_pushshift_data(after, before, sub)

print(len(data))
print(data)

