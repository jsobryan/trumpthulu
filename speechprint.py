#!/usr/bin/env python

import markovify
import re
import random
from os import system, name

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
speechtext = []

def speechsent():
    return generator.make_sentence(max_chars=(random.randint(80,140)),tries=1000)

def speech(x):
    for i in range(x):
      speechtext.append(speechsent())

def clear():
    if name == 'nt':
      system('cls')
    else:
      system('clear')
    

def speechgen():
  while True:
    newline = '\n\n'
    try:
      x = int(input("How many lines should the speech be?: "))
      for i in range(x):
        speechtext.append(speechsent())
    except:
      print('Not a valid answer.  Must be a number')
      continue
    print(f'{newline}{" ".join(speechtext)}{newline}')
    cont = input("Another one? yes/no > ")
    while cont.lower() not in ("yes","no","y","n"):
        cont = input("Please enter 'y' or 'n' ")
    if cont == "no" or cont == "n":
        break

        
        
        
        

speechgen()

  

  
f.close()



 
