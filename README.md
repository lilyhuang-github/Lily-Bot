# Lily-Bot

### This is a ngram language model based on myself that utilises as few pre-made libraries as possible. This README can also guide you through setting up your own ngram model using your own discord package.

## Quick Start
pip install -r requirements.txt

flask run

gunicorn -w 4 app:app

## Overview

### This repository contains an n-gram language model that I trained using my own discord messages. N-gram models work by predicting the next word based on an "n" number of words. 

A unigram: 1 word at a time
A bigram: 2 words at a time
A trigram: 3 words at a time
Etc, etc.

So it looks back at the previous word, and then predicts based on probability of the model what the next word would be.

I've derived a lot of my understanding off of the 3rd chapter of Speech and Language Processing by Daniel Jurafsky and James H. Martin

_Daniel Jurafsky and James H. Martin. 2024. Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models, 3rd edition. Online manuscript released August 20, 2024. https://web.stanford.edu/~jurafsky/slp3._


The model and messages have been removed but there is an implementation below:
https://lily-bot-implementation.onrender.com/
