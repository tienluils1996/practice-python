import nltk as s
document_text = open('music.txt', 'r')
a = document_text.read()
##print(a)
b = a.split()
fdist1 = s.FreqDist(b)

print(fdist1.most_common(100))

print(type(fdist1.most_common(100)))
