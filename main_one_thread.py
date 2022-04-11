from thread import JaccardCalculator
from edit_distance import editDistDP
import time


def job(ngram):
    thread = JaccardCalculator("thread_1", "th1", query, lines, ngram)
    thread.run()
    maximum = max(thread.top3)
    coef[0] = maximum
    words[0] = thread.similar_words[thread.top3.index(maximum)]
    thread.top3[thread.top3.index(maximum)] = 0
    maximum = max(thread.top3)
    coef[1] = maximum
    words[1] = thread.similar_words[thread.top3.index(maximum)]
    thread.top3[thread.top3.index(maximum)] = 0
    maximum = max(thread.top3)
    coef[2] = maximum
    words[2] = thread.similar_words[thread.top3.index(maximum)]
    thread.top3[thread.top3.index(maximum)] = 0


def printOutput(ngram, words, coef, distance, spent):
    print(f'''
            {ngram}Grams !!

            Word : {words[0]} 
            with Jaccard Coefficient : --- {round(coef[0], 2)} --- has the minimum distance : {distance[0]}

            Word : {words[1]} 
            with Jaccard Coefficient : --- {round(coef[1], 2)} --- has the distance : {distance[1]}

            Word : {words[2]} 
            with Jaccard Coefficient : --- {round(coef[2], 2)} --- has the distance : {distance[2]}

            Spent time : {str(round(spent, 2))}''')
    print("-------------------------------------------------------------------------------")


def distanceCalc():
    distance[0] = editDistDP(query, words[0], len(query), len(words[0]))
    distance[1] = editDistDP(query, words[1], len(query), len(words[1]))
    distance[2] = editDistDP(query, words[2], len(query), len(words[2]))


def editDistanceAnalysis():
    minDist = 99
    similar_word = ""
    before = time.perf_counter()
    for line in lines:
        distance = editDistDP(query, line, len(query), len(line))
        if distance < minDist:
            minDist = distance
            similar_word = line
    after = time.perf_counter()
    print(f''' EditDistance !!

                Word : {similar_word} --- has the minimum distance : {minDist}
                
                Spent time : {str(round(after - before, 2))}
    ''')
    print("-------------------------------------------------------------------------------")


with open('660000_parole_italiane.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].rstrip("\n")
query = "conigl"
coef = [0, 0, 0]
words = ["", "", ""]
distance = [0, 0, 0]

# Analisi di 1Gram
before = time.perf_counter()
job(1)
after = time.perf_counter()
distanceCalc()
printOutput(1, words, coef, distance, after - before)
# Analisi di 2Gram
before = time.perf_counter()
job(2)
after = time.perf_counter()
distanceCalc()
printOutput(2, words, coef, distance, after - before)
# Analisi di 3Gram
before = time.perf_counter()
job(3)
after = time.perf_counter()
distanceCalc()
printOutput(3, words, coef, distance, after - before)
# Analisi di 4Gram
before = time.perf_counter()
job(4)
after = time.perf_counter()
distanceCalc()
printOutput(4, words, coef, distance, after - before)
# Analisi di EditDistance
editDistanceAnalysis()
