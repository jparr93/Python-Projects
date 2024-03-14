import feedparser

NewsFeed = feedparser.parse("https://azurecomcdn.azureedge.net/en-gb/updates/feed/")

entry = NewsFeed.entries[1]

print (entry.published)
print ("******")
print (entry.summary)
print ("------News Link--------")
print (entry.link)