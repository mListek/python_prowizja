import pandas as pd
import pyperclip

def filterData(border_date, month, region):
    pyperclip.waitForNewPaste()
    df = pd.read_clipboard(na_filter=False, decimal=',')

    # fiter out rows without payment
    df = df.loc[df['należn'] == 'zapłacono']
    # format data
    df['netto'] = df['netto'].str.replace(' ', '').str.replace(',', '.').astype(float)
    df['wpłynęło'] = pd.to_datetime(df['wpłynęło']).dt.date
    df['termin pr.'] = pd.to_datetime(df['termin pr.']).dt.date
    # filter out data
    df = df.loc[df['wpłynęło'] >= border_date]
    df = df.loc[df['wpłynęło'] < df['termin pr.']]
    
    # split into companies and clients
    df_companies = df.loc[df['rodzaj'] == 'Przedst']
    df_clients = df.loc[df['rodzaj'] == 'Klient']

    # calculate sum
    companies_sum = df_companies['netto'].sum()
    clients_sum = df_clients['netto'].sum()

    saveToPdf(df_companies, month, region)
    saveToPdf(df_clients, month, region)

def saveToPdf(df, month, region):
    with pd.ExcelWriter('prowizja_test.xlsx', mode='a', if_sheet_exists='new') as writer:
        df.to_excel(writer)
