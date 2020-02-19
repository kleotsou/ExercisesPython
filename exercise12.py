import datetime
today1 = datetime.date.today()
print("Η σημερινή ημερομηνία είναι:", today1)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%M:%S")
print("Η τρέχουσα ώρα είναι =", current_time)

year = int(input("Δώσε τον χρόνο που θες:")
while (year == " ") or (year < 0):
  year = int(input("Δώσε τον χρόνο που θες:"))
month = int(input("Δώσε τον μήνα που θες:")
while (month < 1) or (month > 12) or (month == " "):
  month = int(input("Δώσε τον μήνα που θες:")
day = int(input("Δώσε την ημέρα που θες:")
if (month == 2):
  if (year%4 == 0) or (year%100 == 0) or (year%400 == 0):
    while (day < 1) or (day > 29) or (day == " "):
      day = int(input("Δώσε την ημέρα που θες:"))
  else:
    while (day < 1) or (day > 28) or (day == " "):
      day = int(input("Δώσε την ημέρα που θες:"))
    
