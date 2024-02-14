#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
import glob
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# creating dict of dict so specific date and hashtag will have a count
total = defaultdict(lambda: defaultdict(int))
for path in glob.glob('outputs/geoTwitter*.country'):
    with open(path) as f:
        tmp = json.load(f)
         # extracting date from file name : geoTwitterDD-MM-YY.zip.country
        date = os.path.basename(path)[10:18]
        
        #increasing occurences of hashtag on a day
        for hashtag in args.keys:
            if hashtag in tmp:
                total[hashtag][date]+=sum(tmp[hashtag].values())

fig, ax = plt.subplots()
for hashtag in args.keys:
    dates = sorted(total[hashtag].keys())
    vals = [total[hashtag][date] for date in dates]
    days = [datetime.strptime(date, '%y-%m-%d') for date in dates]

    ax.plot(days, vals, label = hashtag)

ax.set_xlabel('Date')
ax.set_ylabel('Number of Tweets')
ax.legend()

# save plot
tags = [hashtag[1:] for hashtag in args.keys]
plt.savefig('_'.join(tags) + '.png')

