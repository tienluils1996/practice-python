import nltk as s
document_text = open('m.txt', 'r')
a = document_text.read()
##print(a)
def long_words(n, str):
    word_len = []
    txt = str.split()
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

b = long_words(2,a)
fdist1 = s.FreqDist(b)

print(fdist1.most_common(100))
print(type(fdist1.most_common(100)))
