import datetime
today1 = datetime.date.today()
print("Η σημερινή ημερομηνία είναι:", today1)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Η τρέχουσα ώρα είναι =", current_time)

da = str(today1)
ds = da.split('-')
formatted = ds[0] + ds[1] + ds[2]

y = int(formatted[0] + formatted[1] + formatted[2] + formatted[3])
m = int(formatted[4] + formatted[5])
d = int(formatted[6] + formatted[7])

m1 = str(current_time)
m2 = m1.split(':')
time = m2[0] + m2[1] + m2[2]

h = int(time[0] + time[1])
mi = int(time[2] + time[3])*60
s = int(time[4] + time[5])+mi 

year = int(input("Δώσε τον χρόνο που θες:"))
while (year == " ") or (year < 0):
  year = int(input("Δώσε τον χρόνο που θες:"))
month = int(input("Δώσε τον μήνα που θες:"))
while (month < 1) or (month > 12) or (month == " "):
  month = int(input("Δώσε τον μήνα που θες:"))
day = int(input("Δώσε την ημέρα που θες:"))
if (month == 2):
  if (year%4 == 0) or (year%100 == 0) or (year%400 == 0):
    while (day < 1) or (day > 29) or (day == " "):
      day = int(input("Δώσε την ημέρα που θες:"))
    print("Ο μήνας έχει 29 μέρες.")
  else:
    while (day < 1) or (day > 28) or (day == " "):
      day = int(input("Δώσε την ημέρα που θες:"))
    print("Ο μήνας έχει 28 μέρες")
else:
  for i in range(1, 9 , 2):
    if (month == i):
        while (day < 1) or (day > 31) or (day == " "):
          day = int( input("Δώσε την ημέρα που θες:"))
        print("Ο μήνας που δώθηκε έχει 31 μερες.")
  for i in range(8, 14, 2):
    if (month == i):
      while (day < 1) or (day > 31) or (day == " "):
        day = int( input("Δώσε την ημέρα που θες:"))
      print("Ο μήνας που δώθηκε έχει 31 μερες.")
  for i in range(4, 8, 2):
    if (month == i):
      while (day < 1) or (day > 30) or (day == " "):
        day = int( input("Δώσε την ημέρα που θες:"))
      print("Ο μήνας που δώθηκε έχει 30 μερες.")
  for i in range(9, 13, 2):
     if (month == i):
      while (day < 1) or (day > 30) or (day == " "):
        day = int( input("Δώσε την ημέρα που θες:"))
      print("Ο μήνας που δώθηκε έχει 30 μερες.")
      
print("Η ημερομηνία που δώθηκε είναι:", year, "-", month, "-", day)
  if (year >= y) and (month >= m) and (day > d):
    day = day - 1                      

from datetime import date
x1 = date(y, m, d)
x2 = date(year, month, day)
x3 = (x2 - x1)

if (year == y) and (month == m) and (day == d):
  print("Ίδια ημερομηνία με την τρέχουσα")
elif (year >= y) and (month >= m) and (day >= d):
  print("Απέχει", abs(x3), 24-h, "ώρες", 3600-s, "δευτερόλεπτα")
else:
  print("Απέχει", abs(x3), 24-h, "ώρες", 3600-s, "δευτερόλεπτα")
