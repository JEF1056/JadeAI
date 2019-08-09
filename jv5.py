# Import all the dependencies
import pandas as pd
import numpy as np
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator

from sklearn.pipeline import make_pipeline

import argparse

# Log starting time
from datetime import datetime
t1 = datetime.now()

# Define something to allow simple t/f args such as "-train"
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Parser of args ;D
parser = argparse.ArgumentParser(description='Add training/loading fuctionality')
parser.add_argument("-train", type=str2bool, nargs='?', const=True, default=False,
                        help="Train (will otherwise load)")
parser.add_argument("-path", type=str, default="pipe.p",
                        help="training output path")
parser.add_argument("-input", type=str, default="inputcln.txt",
                        help="training output path")
parser.add_argument("-size", type=int, default=350,
                        help="size for the training compression")                       
args = parser.parse_args()

# Nou, matplotlib
import warnings
warnings.filterwarnings("ignore")

if args.train == True:
    # Read file
    lines = [line.rstrip('\n').replace('\\n',' ').replace('>','') for line in open(args.input)]

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

    # Depending on the size of your data, you want ARPACK 
    # to at least keep around 50% or more of your data
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
    def __init__(self, k=8, temperature = 1.2):
        self.k = k
        self.temperature = temperature
    
    def fit(self, X, y):
        self.tree_ = BallTree(X)
        self.y_ = np.array(y)
        
    def predict(self, X, random_state = None):
        distances, indeces = self.tree_.query(X, return_distance = True, k = self.k)
        result = []
        dist = []
        for distance, index in zip(distances, indeces):
            result.append(np.random.choice(index, p = softmax(distance * self.temperature)))
            dist.append(distance)
            
        return self.y_[result], dist

ns = NeighborSampler()

if args.train == True:
    ns.fit(matrix_small, subtitles.reply)
    
    # Vectorize, SVD and then chose an answer
    pipe = make_pipeline(vectorizer, svd, ns)

    #save the pipe variable for the sake of faster loading
    with open(args.path, 'wb') as pickle_file:
        pickle.dump(pipe, pickle_file, protocol=4)
else:
    with open(args.path, 'rb') as fp:
        pipe = pickle.load(fp)

#undo the vectorization from ealier
def fixpunctuation(sentence):
    sentence=sentence.replace(' !', "!")
    sentence=sentence.replace(' ?', "?")
    sentence=sentence.replace(' ,', ",")
    sentence=sentence.replace(' .', ".")
    sentence=sentence.replace(' :', ":")
    return sentence

#import some discord stuff
import os, os.path
import sys
import asyncio
import discord

asyncio.set_event_loop(asyncio.new_event_loop())
import aiohttp
client = discord.AutoShardedClient()
global headers, url

@client.event
async def on_ready():
    global headers, url
    dbltoken = "noice"
    url = "https://discordbots.org/api/bots/" + str(client.user.id) + "/stats"
    headers = {"Authorization" : dbltoken}
    print('Logged in as '+client.user.name+' (ID:'+str(client.user.id)+') | Connected to '+str(len(client.guilds))+' servers | Connected to '+ str(len(set(client.get_all_members()))) +' users')
    print('--------')
    print('You are running "nut."') #Do not change this. This will really help us support you, if you need support.
    print('--------')
    print("Discord.py verison: " + discord.__version__)
    print('--------')
    print("Ready in " + str(datetime.now() - t1))
    print('--------')
    print(str(len(client.shards))+" shard(s)")   
    await client.change_presence(activity=discord.Game(name="Someone talk to me!!!!", type=3), status=discord.Status.idle)
    
    payload = {"server_count"  : len(client.guilds)}
    async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)

@client.event         
async def on_server_join(server):
    global headers, url
    payload = {"server_count"  : len(client.guilds)}
    async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)

@client.event
async def on_server_remove(server):
    global headers, url
    payload = {"server_count"  : len(client.guilds)}
    async with aiohttp.ClientSession() as aioclient:
            await aioclient.post(url, data=payload, headers=headers)
    
@client.event        
async def on_message(message):
    if not message.author.bot:
        if message.content.startswith('JD ') or message.content.startswith('jd '):
            ModMessage = message.content[3:]
            p_resp, dist = pipe.predict([ModMessage])
            response=fixpunctuation(p_resp[0])
            print(datetime.time())
            print(str(message.author)+": " + ModMessage + "\nJade: " + response)
            print("Probability: "+str(dist).replace("array", "")[2:][:-2] + "\n")
            await message.channel.send(response)
    
client.run("Nou")