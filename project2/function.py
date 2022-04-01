import dbfunction as db
import vfunctions as f
import csv
from datetime import date
import pandas as pd
import lit as l
def menu():
    print(l.TEXT01)
    print(l.TEXT02)
    m = int(input(l.TEXT03))
    if m == 1 :
        # insert new enteries
        n = int(input(l.TEXT04))
        dic(n)
        db.insert_data()
    elif m== 2 :
        # show the current day reservation
        db.select_data()

    elif m == 3:
        #export data to csv
        db.export_data()
    elif m == 4:
        #show the tables in tabular form
        show_table()


def dic(n):
    for i in range(n):

        id = f.validate_id()
        nif = input(l.TEXT05)
        data = f.validate_date()
        hora = f.validate_time()
        motiu = input(l.TEXT06)
        datares = date.today()

        logs = {
            "id" : id,
            "nif": nif,
            "date": data,
            "hora": hora,
            "motiu" : motiu,
            "datares":datares
        }
        write_CSV(logs)

def read_CSV():
    with open('file/reserves.csv','r') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)


def write_CSV(std):
    chk = chk_file()
    with open('file/reserves.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id','nif', 'date', 'hora', 'motiu','datares']
        write_csv = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if chk == False :
            write_csv.writeheader()
        write_csv.writerow(std)

# function to check the file if exist or not
def chk_file():
    try:
        f = open('file/reserves.csv','r')
        return True
    except FileNotFoundError as e:
        return False
    else:
        f.close()

def show_table():
    # configuration to show all the table
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    df = pd.read_csv('file/reserves.csv', index_col='id')
    print(df)

