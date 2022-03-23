print("Kalkulator")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
wynik = 0
działanie = input("Wybierz działanie: ")
while True:  
  n = int(input()) 
  if działanie == "1":
    wynik = a+b
  elif działanie == "2":
    wynik = a-b
  elif działanie == "3":
    wynik = a*b
  elif działanie == "4":
    wynik = a/b
  else:
    wynik = "Nie ma takiego działania"
print(wynik)