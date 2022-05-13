#!/usr/bin/env python

import markovify
import re
import random

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

with open('poemspeech.txt','r') as f:
    content = f.read()


data = text_cleaner(content)

generator = markovify.Text(data,state_size=1)

#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

with open('poemspeech.txt','r') as f:
    content = f.read()

data = text_cleaner(content)

generator = markovify.Text(data,state_size=2)

def speechsent():
    return generator.make_sentence(max_chars=(random.randint(80,140)),tries=1000)

def speech(x):
    for i in range(x):
      print(speechsent())

speechsent(20)
  
f.close()



 
