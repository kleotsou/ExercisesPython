def remove_chars(data, chars):
    new_data = data
    for ch in chars:
        new_data = new_data.replace(ch, '')
    return new_data

file1 = open("text.txt", "w")
file1.write("Fruits are the means dy which angiosperms disseminate seeds. Edible fruits, in particular, have propagated with the movements of humans and animals in a symbiotic relationship as a means for seed dispersal and nutrition; in fact, humans and many animals have become dependent on fruits as a source of food, Accordingly, fruits account for a substantial fraction of the worlds agricultural output, and some (such as the apple and the pomegranate) have acquired extensive cultural and symbolic meanings. ")                                                                                                                                                                                                                                                                                                                                                                                               
file1.close()
file1 = open("text.txt", "r")
f = file1.read()
file1.close()
x = len(f)
w = " "
words = []
for i in range(x):
    if (f[i] != " ") and (f[i] != "/n"):
        w = (w + f[i])
    else:
        words.append(w)
        w = " "
x1 = len(words)
for i in range(x1):
    n = words[i]
    a = remove_chars(n, '.,()! ')
    words[i] = a
word = []
for i in range(x1):
    z = words[i]
    k = z.lower()
    word.append(k)
word.sort(key=len)
lastword = []
for i in range(x1-1, x1-6, -1):
    m = word[i]
    z = remove_chars(m, 'aeioyu')
    z1 = len(z)
    new = " "
    for j in range(z1-1, -1, -1):
        new = new + z[j]
    lastword.append(new)
print(lastword)


