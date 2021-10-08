import pandas as pd
import config


def get_ATM_machine():
    status, location, cash_available = open("Machine_info.txt").read().split('\n')
    return config.Classes.Machine(location, status, float(cash_available)) 

def save_ATM_Machine(mch):
    pass###

def save_acc(acc):
    columns = ["Balance", "Card PIN"]
    df =  pd.read_csv('Accounts_Data_Test.csv', dtype=str)
    vals = acc.get_vals()
    for c in range(len(columns)):
        print('a')
        df.loc[df["Account No"] == str(acc.acc_no), columns[c]] = vals[c]
    #df.to_csv('Accounts_Data_Test.csv')

def save_card(card):
    columns = ["status", "attmpts"]
    df =  pd.read_csv('Cards_Data_Test.csv', dtype=str)
    vals = card.get_vals()
    for c in range(len(columns)):
        print('a')
        df.loc[df["Card No"] == str(card.card_no), columns[c]] = vals[c]
    print(df)
    #df.to_csv('Cards_Data_Test.csv')

def check_card(accs, card_no):
    if str(card_no) in accs["Card No"].values:
        row = accs[ accs["Card No"] == str(card_no) ].values[0]
        return config.Classes.Account(row[0],row[1],row[2],row[3],int(row[4]),row[5],row[6])
    return None


def get_acc_from_card(card_no):
    dataframe = pd.read_csv("Accounts_Data.csv", dtype=str)
    return check_card(dataframe, card_no)


def get_acc(acc_no):
    dataframe = pd.read_csv("Accounts_Data.csv", dtype=str)
    row = dataframe[dataframe["Account No"] == str(acc_no)]
    if (row.size):
        row = row.values[0]
        return config.Classes.Account(row[0],row[1],row[2],row[3],int(row[4]),row[5],row[6])
    return None


def get_cards():
    cards = []
    dataframe = pd.read_csv("Cards_Data.csv", dtype=str).head(6)
    for row in dataframe.values:
        cards.append(config.Classes.Card(row[0],row[1],row[2],row[3]))
    return cards


if __name__ == "__main__":
    mch = get_ATM_machine()
