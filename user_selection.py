from datetime import date

managers = {1: 'Mrozowski', 2: 'Dziędziurko', 3: 'Kukowka'}

def getDateFromUser():
  while True:
    try:
      year = int(input('Podaj rok: '))
      month = int(input('Podaj miesiąc: '))
      day = int(input('Podaj dzień: '))

      end_date = date(year, month, day)

      print('Czy data: ', end_date, 'jest poprawna?')
      user_confirmation = input('1 - Poprawna, 2 - Spróbuj ponownie: ')

      if user_confirmation == '1':
        return end_date
    except:
      print('Zły format daty, spróbuj jeszcze raz')

def getManagerFromUser():
  print('1. Marek Mrozowski')
  print('2. Tomasz Dziędziurko')
  print('3. Gabriel Kukowka')
  while True:
    try:
      choosen_mgr = int(input())
      if choosen_mgr > 0 and choosen_mgr < 4:
        return managers[choosen_mgr]
      else:
        raise ValueError('Zły numer')
    except:
      print('Wystąpił błąd! Wpisz 1, 2, albo 3:')