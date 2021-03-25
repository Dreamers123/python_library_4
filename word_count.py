from collections import Counter

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]


word_counts = Counter(words)
top_three = word_counts.most_common(3)
morewords = ['why','are','you','not','looking','in','my','eyes','eyes','eyes','eyes','eyes','eyes','eyes']
for word in morewords:
    word_counts[word] += 1
#print(word_counts['eyes'])
a=Counter(words)
b=Counter(morewords)
c=a+b
print(c.most_common(1))