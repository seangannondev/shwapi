from datetime import datetime, time
from psaw import PushshiftAPI
import pandas
from shwapi.timemethods import get_current_time, get_midnight, get_top_of_hour, get_year_start
from shwapi.stocks import get_stock_dict
from shwapi.common import import_mentions

def t():
    
    column_names = ["id", "hour"]
    df = pandas.DataFrame(columns = column_names)
    print(df)
    after = get_year_start()
    before = get_top_of_hour()
    posts_list = get_submissions(after, before)

    tickerDict = get_stock_dict()

    for thing in posts_list:    
        thingtime = thing.d_['created_utc'] 
        hourdt = datetime.utcfromtimestamp(thingtime)
        hour = int(thingtime) - (hourdt.minute * 60 + hourdt.second)
        seenset = set()
        if 'selftext' not in thing.d_:
            titleAndText = thing.d_['title']
        else:
            titleAndText = thing.d_['selftext'] + thing.d_['title']
        words = titleAndText.split()
        i = 0
        while i < len(words):
            curr = words[i]
            if words[i] in tickerDict:
                if isinstance(tickerDict[words[i]], list):
                    mark,z = i, 0
                    remwords = tickerDict[words[i]]
                    ismatch = True
                    while not isinstance(remwords[z], int) and ismatch is True:
                        if remwords[z] == words[i]:
                            z += 1
                            i += 1
                        else:
                            i = mark + 1
                            ismatch = False
                    
                    if remwords[z] not in seenset and ismatch is True:
                        df = df.append({'id': remwords[z], 'hour': hour}, ignore_index = True)
                        i += 1
                        seenset.add(remwords[z])

                else:
                    if tickerDict[words[i]] not in seenset:
                        df = df.append({'id': tickerDict[words[i]], 'hour': hour}, ignore_index = True)
                        seenset.add(tickerDict[words[i]])
                    i += 1
            else:
                i += 1
    
    import_mentions(df)
    

def get_submissions(afterdate, beforedate):
    api = PushshiftAPI()
    gen = api.search_submissions(after = afterdate, before = beforedate,
    subreddit='wallstreetbets', filter=['title','selftext'], limit = 200 )
    mylist = list(gen)
    return mylist   

    