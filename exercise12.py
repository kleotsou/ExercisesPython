import datetime
today1 = datetime.date.today()
print("Η σημερινή ημερομηνία είναι:", today1)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Η τρέχουσα ώρα είναι =", current_time)

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
    
