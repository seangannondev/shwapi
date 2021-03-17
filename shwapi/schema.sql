DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS tickers;
DROP TABLE IF EXISTS aliases;
DROP TABLE IF EXISTS reddit_comments;
DROP TABLE IF EXISTS reddit_submission;


CREATE TABLE reddit_comments(
  hour INTEGER NOT NULL,
  ticker TEXT NOT  NULL,
  mentions INTEGER NOT NULL,
  PRIMARY KEY(hour, ticker)
);

CREATE TABLE reddit_submissions(
  hour INTEGER NOT NULL,
  ticker TEXT NOT  NULL,
  mentions INTEGER NOT NULL,
  PRIMARY KEY(hour, ticker)
);

CREATE TABLE tickers(
  id INTEGER PRIMARY KEY,
  ticker TEXT NOT NULL,
  stock_name TEXT
);

CREATE TABLE aliases(
  id INTEGER NOT NULL,
  alias TEXT NOT NULL
);