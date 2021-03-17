import sqlite3
import pandas
from shwapi.db import get_db

def import_mentions(df):
    db = get_db()
    df = df.groupby(['id', 'hour']).size().reset_index(name='counts')
    df.to_sql("reddit_submissions", db, if_exists='append', index=False)
