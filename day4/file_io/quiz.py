import re
import collections

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))

f = open('files/relative_data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

f = open('newfile.txt', 'a')
f.write("Hello\nWorld\n")
f.close()

f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines)
f.write(text)
f.close()