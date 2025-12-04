
# Lily-Bot

**Lily-Bot** is an n-gram language model based on my own Discord messages.  
It is built to use as few pre-made libraries as possible. This README also guides you through setting up your own n-gram model using your preferred Discord package.

---

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
````

Run the Flask app:

```bash
flask run
```

Or run with Gunicorn (for production):

```bash
gunicorn -w 4 app:app
```

---

## Overview

This repository contains an n-gram language model trained on my own Discord messages.

### What is an n-gram?

N-gram models predict the next word based on the previous "n" words:

* **Unigram**: 1 word at a time
* **Bigram**: 2 words at a time
* **Trigram**: 3 words at a time

The model looks at the previous word(s) and predicts the next word based on probabilities derived from the training data.

---

### References

My understanding of n-gram models is largely derived from:

**Daniel Jurafsky and James H. Martin (2024).**
*Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models, 3rd edition.*
Online manuscript released August 20, 2024.
[https://web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3)

---

### Demo

The model and original messages have been removed for privacy.
You can try an implementation here:
[Google Cloud Demo](https://lily-bot-352988256386.us-central1.run.app/)

