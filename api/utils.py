from math import log
import re


# использую Regex для рзаделения на пред и слова в них
def get_sentences(text):
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)


def get_words(sentence):
    return re.findall(r'\b\w+\b', sentence.lower())


def calculate_tf(words):
    tf = {}
    for word in words:
        tf[word] = tf.get(word, 0) + 1
    return tf


# В общем подразумевается ведь в задании один документ а в контексте
# одного документ не совсем понятно что такое idf,
# но я предложу такую реализацию где каждое предложение это документ
def calculate_idf(sentences):
    idf = {}
    total_documents = len(sentences)
    for sentence in sentences:
        seen_words = set()
        for word in get_words(sentence):
            if word not in seen_words:
                idf[word] = idf.get(word, 0) + 1
                seen_words.add(word)
    for word, count in idf.items():
        idf[word] = log(total_documents / float(count))
    return idf


def parse_string(string):
    sentences = get_sentences(string)
    words_in_sentences = [get_words(sentence) for sentence in sentences]

    all_words = [word for sentence in words_in_sentences for word in sentence]
    tf = calculate_tf(all_words)
    idf = calculate_idf(sentences)

    data = []
    for word in set(all_words):
        data.append({"word": word, "tf": tf[word], "idf": idf[word]})
    data = sorted(data, key=lambda x: x["idf"], reverse=True)
    return data
