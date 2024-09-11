import os
import json
import re
from collections import defaultdict
import random
#puts every message into one json
def getSuperJSON(name = "super.json"):
    path = "./package/messages/"
    #iterate over the directories if its a directory (instead of regular looping)
    subdirectories = [os.path.join(path, subdir + "/messages.json") for subdir in os.listdir(path) if os.path.isdir(os.path.join(path, subdir))]
    superJson = list()  

    for x in subdirectories:
    #with doing error handling instead of try catch; also auto closes it
        with open(x, 'r', encoding='utf-8') as infile:
            superJson.extend(json.load(infile))

    with open(name, 'w', encoding='utf-8') as output_file:
        json.dump(superJson, output_file)
#getSuperJSON()
    

#gets everything
def getContents():
    with open('./super.json', 'r') as file:
        data = json.load(file)

    content = [item['Contents']for item in data]
    return content

#gets attachments of message
def getAttachments():
    with open('./super.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    attachments = [info['Attachments']for info in data]
    return attachments

def attachmentSetup(fun = False):
    #removes all non attachments for fun

    attachments = getAttachments()
    attachmentDict = defaultdict(int)
    for x in range(len(attachments)-1):
        value = attachments[x]
        attachmentDict[value] +=1
    if fun:
        attachmentDict.pop('', None)

    return attachmentDict

def predictAttachment(attachmentDictionary):

    links = list(attachmentDictionary.keys())
    probability = list(attachmentDictionary.values())

    attachment = random.choices(links, weights=probability, k=1)
    return attachment

def saveAttachGram(attachments, file):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(attachments, file)

def loadAttachGram(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    


# saveAttachGram(attachmentSetup(True), "attachments.json")

#regexs to remove links, and split by the space and also returns with start and end of sentence
def tokenize(text):
    text = re.sub(r'https?://\S+', '', text) 
    text = re.sub(r'[^\w\s]', '', text) 
    tokens = re.findall(r'\b\w+\b', text.lower())
    return ["<s>"] + tokens + ["</s>"]

#returns the ngram model
def setup():
    content = getContents()
    #gets everything

    #splits everything into words and adds <s> </s> to end and start of sentences 
    tokenized_contents = [tokenize(content) for content in content]

    #flattens everything so it's 1 array
    tokens = [token for sublist in tokenized_contents for token in sublist]
    
    # print(tokens)

    def generate_ngrams(tokens, n):
        # ngrams = zip(*[tokens[i:] for i in range(n)])
        slices = [tokens[i:] for i in range(n)]
        #iterates through to slices the n'th index
        #e.g n = 3 array [A, B, C, D, E]
        #creates 3 slices: [A, B, C, D, E]
        # [B, C, D, E]
        # [C, D, E]


        #zip takes those slices and pairs the same index with each other  
        # so it'll pair A, B, C
        # and B, C, D
        # and C, D, E
        # which are ngrams/trigrams but in tuple form 
        ngrams = list(zip(*slices))
        # print(ngrams)

        #turns it from tuple into a single string ngram array
        return [" ".join(ngram) for ngram in ngrams]

    ngrams = generate_ngrams(tokens, 2)
    # print(ngrams)
    ngram_model = defaultdict(lambda: defaultdict(int))
    # print(ngram_model)

    #creates a nested dictionary for each word and pair
    #so it'd be like A: {B: 1}
    # B: {C: 1}
    for i in range(len(tokens) - 1):
        context = tokens[i]
        next_word = tokens[i + 1]
        ngram_model[context][next_word] += 1
    return ngram_model

#saves ngram to file
def saveNgram(nGramModel, file):
    with open(file, 'w', encoding='utf-8') as file:
        json.dump(nGramModel, file)

#loads the ngram from file
def loadNgram(file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return defaultdict(lambda: defaultdict(int), data)

#predicts the next word
def predict_next_word(ngram_model, previous_word):
    #access the dictionaries key value pair
    next_word_frequencies = ngram_model.get(previous_word, {})
    # print(next_word_frequencies)
    if not next_word_frequencies:
        return None  # No valid next word for this context


    #every possible option based on previous word 
    words = list(next_word_frequencies.keys())

    #gets the value/weighting off it all
    weights = list(next_word_frequencies.values())
    

    #makes a choice randomly
    next_word = random.choices(words, weights=weights, k=1)[0]
    return next_word

# ngram_model = setup()
# saveNgram(dict(ngram_model), "nGram.json")

#runs all the setups 
def superSetUp(gramFileName = "", attachmentFileName = "", superName = "", attachmentCoolness = False):
    if not not superName:
        #makes a json with all the messages
        getSuperJSON(superName)

    #gets content from superJSON
    if not not gramFileName:
        #sets up the nested dictionary of the ngram
        nGram = setup()
        #saves
        saveNgram(nGram, gramFileName)

    if not not attachmentFileName:
        #sets up the dictionary of the attachments // also a flag if it's cool or not (will always give an attachment and not blank)
        aGram = attachmentSetup(attachmentCoolness)
        #saves
        saveAttachGram(aGram, attachmentFileName)

# superSetUp("", "", "superTest.json")


ngram_model = loadNgram("nGram.json")
attachGram_Model = loadAttachGram('attachments.json')

# Example: predict the next word after "<s>"
nextWord = "<s>"
sentence = ""
while not nextWord == "</s>":
    sentence += " " + nextWord
    nextWord = predict_next_word(ngram_model, nextWord)
    # print(nextWord)
sentence = sentence[5:]

att = predictAttachment(attachGram_Model)
print(sentence)
print(att)
# print(next_word)
