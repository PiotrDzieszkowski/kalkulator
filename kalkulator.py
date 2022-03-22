def pobierz_liczbe():
  while True:
    try:
      liczba = float(input())
      break
    except ValueError:
      print("Podany tekst nie jest liczbą")
  return liczba

def main():
  koniec = False
  while not koniec:
    print("Podaj w oddzielnych wierszach liczbę, operację matematyczną: +,-,*,/,%, a następnie kolejną liczbę:")
    liczba1 = pobierz_liczbe()
    operacja = input()
    liczba2 = pobierz_liczbe()

    try:
      if operacja == "+":
        wynik = liczba1 + liczba2
      elif operacja == "-":
        wynik = liczba1 - liczba2
      elif operacja == "*":
        wynik = liczba1 * liczba2
      elif operacja == "/":
          wynik = liczba1 / liczba2
      elif operacja == "%":
        wynik = liczba1 % liczba2
      else:
        print("Niepoprawna operacja")
        break
      print("Twój wynik to: " + str(wynik))
    except ZeroDivisionError:
      print("Nastąpiło dzielenie przez zero")

    print("Chcesz wykonać kolejne działanie? Wpisz literę t lub n")

    kolejne = input()
    if kolejne == "n":
      koniec = True
    elif kolejne != "t":
      print("Niepoprawny wybór")
      break

if __name__ == "__main__":
  main()