#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True,nargs='+')
parser.add_argument('--key',required=True,nargs='+')
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
for in_file in args.input_path:
    with open(in_file) as f:
        counts = json.load(f)

    for in_key in args.key:
# normalize the counts by the total values
        if args.percent:
            for k in counts[in_key]:
                counts[in_key][k] /= counts['_all'][k]

# print the count values
        items = sorted(counts[in_key].items(), key=lambda item: (item[1],item[0]), reverse=True)
        for k, v in items[:10]:
            print(k,':',v)

        # extracting the top 10 keys and values from items and then sorting from low to high
        # this works because items is already sorted from high to low

        keys = [item[0] for item in items[:10]][::-1]
        vals = [item[1] for item in items[:10]][::-1]

        plt.bar(range(len(vals)), vals)
        plt.xticks(range(len(keys)), keys)
        plt.ylabel('Number of Tweets')

        if (in_file == 'reduced.lang'):
            plt.xlabel('Language Code')
            plt.savefig(in_key[1:] + '_lang.png')
        else:
            plt.xlabel('Country Code')
            plt.savefig(in_key[1:] + '_country.png')
       
        plt.clf()
        
