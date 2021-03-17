import pandas
import sqlite3
from shwapi.db import get_db


def refresh_stocks():
    import_tickers_from_csv()
    import_aliases_from_csv()

def import_tickers_from_csv():
    db = get_db()
    db.execute("DROP TABLE IF EXISTS tickers;")
    db.execute("CREATE TABLE tickers(id INTEGER PRIMARY KEY, ticker TEXT NOT NULL, stock_name TEXT);")
    df = pandas.read_csv("shwapi/tickers_and_names.csv")
    df.to_sql("tickers", db, if_exists='append', index=False)


def import_aliases_from_csv():
    db = get_db()
    db.execute("DROP TABLE IF EXISTS aliases;")
    db.execute("CREATE TABLE aliases(id INTEGER NOT NULL,alias TEXT NOT NULL);")
    df = pandas.read_csv("shwapi/aliases.csv")
    df.to_sql("aliases", db, if_exists='append', index=False)

def get_stock_dict():
    db = get_db()
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute("select * from aliases")
    x = c.fetchone()
    mydict = {}
    
    while x != None:
        name = x[1].split()
        if len(name) > 1:
            m = name[1:]
            m.append(x[0])
            mydict[name[0]] = m
        else: 
            mydict[x[1]] = x[0]
        
        x = c.fetchone()
    
    return mydict



    



    

