from user_selection import getDateFromUser, getManagerFromUser
from comission import filterData
from datetime import date
from dateutil.relativedelta import relativedelta

regions = {'Mrozowski':('Wielkopolska', 'Pomorze'),
           'Dziędziurko': ('Małopolska', 'Mazowsze Wschód'),
           'Kukowka': ('Śląsk', 'Mazowsze Zachód')}

# get data from user
end_date = getDateFromUser()
choosen_mgr = getManagerFromUser()

# calculate the date after which the payments will be counted
border_date = date(end_date.year, end_date.month, 1)

# get the last three months before the border date
months = [(border_date - relativedelta(months=3)).month,
          (border_date - relativedelta(months=2)).month,
          (border_date - relativedelta(months=1)).month]

for month in months:
  for region in regions[choosen_mgr]:
    print('Miesiąc:', month, 'Region:', region)
    filterData(border_date, month, region)
