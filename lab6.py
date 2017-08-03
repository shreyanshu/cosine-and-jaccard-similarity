import re
import math
import operator

def getwordlist(filename):
    content = ""
    # open file in read mode
    f = open(filename, "r")
    if f.mode == 'r':
        content = f.readline()
    words_list = re.findall(r'\b[a-z]{1,}\b', content.lower())
    f.close()
    return words_list


def getwordcount(words_list):
    word_count = {}
    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # f.close()
    return word_count


def getinvdocfreq(doc_freq):
    inv_doc_ferq = {}
    for key in doc_freq:
        inv_doc_ferq[key] = math.log(4/doc_ferq[key], 2)

    return inv_doc_ferq


def jaccardSimilarity(doc1, doc2):
    intersection = set(doc1).intersection(doc2)
    union = set(doc1).union(doc2)
    print("Intersection: ", intersection)
    print("Union: ", union)
    return len(intersection)/len(union)


def cosineSimilarity(doc1, doc2, freqdoc1, freqdoc2):
    numerator = 0
    maxdoc1 = freqdoc1[max(freqdoc1, key=freqdoc1.get)]
    maxdoc2 = freqdoc2[max(freqdoc2, key=freqdoc2.get)]
    # print(freqdoc2, maxdoc2, maxdoc1)
    sumWtd1 = 0
    sumWtd2 = 0
    all_words = set(completeWordList)
    for word in all_words:
        if word in freqdoc1:
            wDoc1 = inv_doc_ferq[word]*freqdoc1[word]/maxdoc1
        else:
            wDoc1 = 0
        if word in freqdoc2:
            wDoc2 = inv_doc_ferq[word]*freqdoc2[word]/maxdoc2
        else:
            wDoc2 = 0

        sumWtd1 = sumWtd1 + math.pow(wDoc1, 2)
        sumWtd2 = sumWtd2 + math.pow(wDoc2, 2)
        numerator = numerator + wDoc1*wDoc2

    denominator = math.sqrt(sumWtd1*sumWtd2)

    return numerator/denominator



word_list_d1 = getwordlist("d1.txt")
word_count_d1 = getwordcount(word_list_d1)
word_list_d2 = getwordlist("d2.txt")
word_count_d2 = getwordcount(word_list_d2)
word_list_d3 = getwordlist("d3.txt")
word_count_d3 = getwordcount(word_list_d3)
word_list_d4 = getwordlist("d4.txt")
word_count_d4 = getwordcount(word_list_d4)

# Part A
print("\nPART A: Find the Jaccard similarity of each of the above documents to all other documents. \n")
print("For Document 1 and 2:")
jaccDoc1Doc2 = jaccardSimilarity(word_list_d1, word_list_d2)
print("Hence, Jaccard similarity: ", jaccDoc1Doc2, "\n")

print("For Document 1 and 3:")
jaccDoc1Doc3 = jaccardSimilarity(word_list_d1, word_list_d3)
print("Hence, Jaccard similarity: ", jaccDoc1Doc3, "\n")

print("For Document 1 and 4:")
jaccDoc1Doc4 = jaccardSimilarity(word_list_d1, word_list_d4)
print("Hence, Jaccard similarity: ", jaccDoc1Doc4, "\n")

print("For Document 2 and 3:")
jaccDoc2Doc3 = jaccardSimilarity(word_list_d2, word_list_d3)
print("Hence, Jaccard similarity: ", jaccDoc2Doc3, "\n")

print("For Document 2 and 4:")
jaccDoc2Doc4 = jaccardSimilarity(word_list_d2, word_list_d4)
print("Hence, Jaccard similarity: ", jaccDoc2Doc4, "\n")

print("For Document 3 and 4:")
jaccDoc3Doc4 = jaccardSimilarity(word_list_d3,word_list_d4)
print("Hence, Jaccard similarity: ", jaccDoc3Doc4, "\n")


completeWordList = list(set(word_list_d1)) + list(set(word_list_d2)) + list(set(word_list_d3)) + list(set(word_list_d4))
# print(completeWordList)

# PART B
doc_ferq = getwordcount(completeWordList)
inv_doc_ferq = getinvdocfreq(doc_ferq)
print("PART B: Calculate the Cosine similarity of the above documents. ")

cosDoc1Doc2 = cosineSimilarity(word_list_d1, word_list_d2, word_count_d1, word_count_d2)
print("\nFor Document 1 and 2")
print("Cosine Similarity: ", cosDoc1Doc2)

cosDoc1Doc3 = cosineSimilarity(word_list_d1, word_list_d3, word_count_d1, word_count_d3)
print("\nFor Document 1 and 3")
print("Cosine Similarity: ", cosDoc1Doc3)

cosDoc1Doc4 = cosineSimilarity(word_list_d1, word_list_d4, word_count_d1, word_count_d4)
print("\nFor Document 1 and 4")
print("Cosine Similarity: ", cosDoc1Doc4)

cosDoc2Doc3 = cosineSimilarity(word_list_d2, word_list_d3, word_count_d2, word_count_d3)
print("\nFor Document 2 and 3")
print("Cosine Similarity: ", cosDoc2Doc3)

cosDoc2Doc4 = cosineSimilarity(word_list_d2, word_list_d4, word_count_d2, word_count_d4)
print("\nFor Document 2 and 4")
print("Cosine Similarity: ", cosDoc2Doc4)

cosDoc3Doc4 = cosineSimilarity(word_list_d3, word_list_d4, word_count_d3, word_count_d4)
print("\nFor Document 3 and 4")
print("Cosine Similarity: ", cosDoc3Doc4)











