import pandas as pd
import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator

from sklearn.pipeline import make_pipeline

import argparse

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='Add training/loading fuctionality')
parser.add_argument("-train", type=str2bool, nargs='?', const=True, default=False,
                        help="Train (will otherwise load)")
parser.add_argument("-path", type=str, default="pipe.p",
                        help="training output path")
parser.add_argument("-size", type=int, default=350,
                        help="size for the training compression")                       
args = parser.parse_args()

import warnings
warnings.filterwarnings("ignore")

if args.train == True:
    print("Training!")
    # Read file
    lines = [line.rstrip('\n').replace('\\n',' ').replace('>','') for line in open('inputcln.txt')]

    subtitles = pd.DataFrame(columns=['context', 'reply'])
    subtitles['context'] = lines
    subtitles['context'] = subtitles['context'].apply(lambda x: x.lower())
    subtitles['reply'] = lines[1:] + ['...']
    subtitles['reply'] = subtitles['reply'].apply(lambda x: x.lower())

    for sign in ['!', '?', ',', '.', ':']:
        subtitles['context'] = subtitles['context'].apply(lambda x: x.replace(sign, f' {sign}'))
        subtitles['reply'] = subtitles['reply'].apply(lambda x: x.replace(sign, f' {sign}'))

    subtitles.info()

    vectorizer = TfidfVectorizer()
    vectorizer.fit(subtitles.context)

    matrix_big = vectorizer.transform(subtitles.context)

    matrix_big.shape

    svd = TruncatedSVD(n_components=args.size, algorithm='arpack')
    svd.fit(matrix_big)

    matrix_small = svd.transform(matrix_big)

    # Print new dimensionality and explained variance ratio
    print(matrix_small.shape)
    print(svd.explained_variance_ratio_.sum())

def softmax(x):
    proba = np.exp(-x)
    return proba/sum(proba)

# Choosing one of the k nearest neighbors with BallTree algorithm
class NeighborSampler(BaseEstimator):
    def __init__(self, k=5, temperature = 1.0):
        self.k = k
        self.temperature = temperature
    
    def fit(self, X, y):
        self.tree_ = BallTree(X)
        self.y_ = np.array(y)
        
    def predict(self, X, random_state = None):
        distances, indeces = self.tree_.query(X, return_distance = True, k = self.k)
        result = []
        for distance, index in zip(distances, indeces):
            result.append(np.random.choice(index, p = softmax(distance * self.temperature)))
            
        return self.y_[result]

ns = NeighborSampler()

if args.train == True:
    ns.fit(matrix_small, subtitles.reply)
    
    # Vectorize, SVD and then chose an answer
    pipe = make_pipeline(vectorizer, svd, ns)

    with open(args.path, 'wb') as pickle_file:
        pickle.dump(pipe, pickle_file, protocol=4)
    print("Truncation complete")
else:
    print("Loading!")
    with open(args.path, 'rb') as fp:
        pipe = pickle.load(fp)

def fixpunctuation(sentence):
    sentence=sentence.replace(' !', "!")
    sentence=sentence.replace(' ?', "?")
    sentence=sentence.replace(' ,', ",")
    sentence=sentence.replace(' .', ".")
    sentence=sentence.replace(' :', ":")
    return sentence

import os, os.path
import sys
import asyncio
import discord

asyncio.set_event_loop(asyncio.new_event_loop())
import aiohttp
client = discord.AutoShardedClient()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+str(client.user.id)+') | Connected to '+str(len(client.guilds))+' servers | Connected to '+ str(len(set(client.get_all_members()))) +' users')
    print('--------')
    print('You are running "nut."') #Do not change this. This will really help us support you, if you need support.
    print('--------')
    print("Discord.py verison: " + discord.__version__)
    print('--------')
    print(str(len(client.shards))+" shard(s)")   
    await client.change_presence(activity=discord.Game(name="wow pls don't just copy code, learn how to code.", type=3), status=discord.Status.do_not_disturb)
    
@client.event        
async def on_message(message):
    if not message.author.bot:
        if message.content.startswith('JD ') or message.content.startswith('jd '):
            ModMessage = message.content[3:]
            response=fixpunctuation(pipe.predict([ModMessage])[0])
            print(str(message.author)+": " + ModMessage + "\nJade: " + response + "\n")
            await message.channel.send(response)
    
client.run("hahahahahahah *evil laugh*")