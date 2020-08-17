import bs4 as bs
import urllib.request
import re
import nltk
# Convert Paragraphs to Sentences- split the paragraph whenever a period is encountered
# Text Processing- remove all the special characters, stop words and numbers from all the sentences
# Tokenizing the Sentences
# Find Weighted Frequency of Occurrence
# Replace Words by Weighted Frequency in Original Sentences
# Sort Sentences in Descending Order of Sum

scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

# print(article_text)

# Removing Square Brackets and Extra Spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

sentence_list = nltk.sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)
# ......................
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
#
# # Input text - to summarize
# text = """ """
#
# # Tokenizing the text 
# stopWords = set(stopwords.words("english"))
# words = word_tokenize(text)
#
# # Creating a frequency table to keep the
# # score of each word
#
# freqTable = dict()
# for word in words:
#     word = word.lower()
#     if word in stopWords:
#         continue
#     if word in freqTable:
#         freqTable[word] += 1
#     else:
#         freqTable[word] = 1
#
# # Creating a dictionary to keep the score
# # of each sentence
# sentences = sent_tokenize(text)
# sentenceValue = dict()
#
# for sentence in sentences:
#     for word, freq in freqTable.items():
#         if word in sentence.lower():
#             if sentence in sentenceValue:
#                 sentenceValue[sentence] += freq
#             else:
#                 sentenceValue[sentence] = freq
#
#
#
# sumValues = 0
# for sentence in sentenceValue:
#     sumValues += sentenceValue[sentence]
#
# # Average value of a sentence from the original text
#
# average = int(sumValues / len(sentenceValue))
#
# # Storing sentences into our summary.
# summary = ''
# for sentence in sentences:
#     if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
#         summary += " " + sentence
# print(summary)
