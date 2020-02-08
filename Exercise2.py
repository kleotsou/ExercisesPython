def remove_chars(data, chars):
    new_data = data
    for ch in chars:
        new_data = new_data.replace(ch, '')
    return new_data
def BadOrGood(x):
  j = "fckrFCKR"
  good = 0
  bad = 0
  h = list(x)
  y = len(h)
  for i in range(y):
    if (h[i] not in j):
      good+=1
    else:
      bad+=1
  if (good < bad):
    print("The word",x,"is BAD!!!")
  else:
    print("The word",x,"is GOOD!!!")
f = open("file.txt", "w")
f.write("Fake news is written and published usually with the intent to mislead in order to damage an agency, entity, or person, and or gain financially or politically, voften using sensationalist, dishonest, or outright fabricated headlines to increase readership. Similarly, clickbait stories and headlines earn advertising revenue from this activity. Some keywords are fake junk news, pseudonews. ")
f.close()
f = open("file.txt", "r") 
text = f.read()
print(text)
f.close()
print(text)
word = " "
List = []
j = len(text)
print(j)
for i in range(j):
  if text[i] != " " and text[i] != "/n":
    word = (word + text[i])
  else:
    List.append(word)
    word = " "
j2 = len(List)
print(j2)
print(List)
new = []
for i in range(j2):
  s = List[i]
  a = remove_chars(s, 'aieuyoAIEUYO., ')
  new.append(a)
print(new)
for i in range(j2):
  w = new[i]
  BadOrGood(w)

