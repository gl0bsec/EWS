import feedparser as fp
source1 = ("http://www.business-standard.com/rss/companies-101.rss",str) 
source2 = ("http://www.financialexpress.com/feed/",str)
source3 = ("http://economictimes.indiatimes.com/small-biz/rssfeeds/5575607.cms",str)
sources = [source1,source2, source3]

# generates an individual RSS feed:
def genfeed(url):
    feed = fp.parse(url)
    entries = feed.entries
    summaries = [x.summary for x in entries]
    titles = [x.title for x in entries]
    return titles

# fetches a RSS feeds given a list of sources 
def fetch_feeds(sources):
    fetched = []
    for source in sources:
        fetched.append(genfeed(source[0]))   
    return fetched 

# comment out below to call functions independently 
feed_fetched = fetch_feeds(sources)
