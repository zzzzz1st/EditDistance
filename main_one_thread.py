from thread import JaccardCalculator
from edit_distance import editDistDP
import time

start_time = time.time()
query = "conigl"
coef = [0, 0, 0]
words = ["", "", ""]
distance = [0, 0, 0]
thread = JaccardCalculator("thread_1", "th1", query, "660000_parole_italiane.txt")
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
distance[0] = editDistDP(query, words[0], len(query), len(words[0]))
distance[1] = editDistDP(query, words[1], len(query), len(words[1]))
distance[2] = editDistDP(query, words[2], len(query), len(words[2]))
spent_time = time.time() - start_time
print(f'''

        Calculations Done !!


        Word : {words[0]} 
        with Jaccard Coefficient : --- {coef[0]} --- has the minimum distance : {distance[0]}

        Word : {words[1]} 
        with Jaccard Coefficient : --- {coef[1]} --- has the distance : {distance[1]}

        Word : {words[2]} 
        with Jaccard Coefficient : --- {coef[2]} --- has the distance : {distance[2]}

        Spent time : {spent_time} seconds ! main 222222 ''')
