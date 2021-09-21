import pandas as pd
import config


def check_card(accs, card_no):
    if str(card_no) in accs["Card No"].values:
        row = accs[ accs["Card No"] == str(card_no) ].values[0]
        return config.Classes.Account(row[0],row[1],row[2],row[3],int(row[4]),row[5],row[6])
    return None

    
def get_acc(card_no):
    dataframe = pd.read_csv("Accounts_Data.csv", dtype=str)
    return check_card(dataframe, card_no)

def get_card(card_no):                              #Not req
    cards = pd.read_csv("Cards_Data.csv", dtype=str)
    row = cards[ cards["Card No"] == str(card_no) ].values[0]
    return config.Classes.Card(row[0],row[1],row[2],row[3])

def get_cards():
    cards = []
    dataframe = pd.read_csv("Cards_Data.csv", dtype=str).head(6)
    for row in dataframe.values:
        cards.append(config.Classes.Card(row[0],row[1],row[2],row[3]))
    return cards


if __name__ == "__main__":

    acc = get_acc('784521')
    #acc.details() if acc else print("Nope")