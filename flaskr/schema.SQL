DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    submitted_by INTEGER NOT NULL,
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
    url TEXT NOT NULL,
    FOREIGN KEY (submitted_by) REFERENCES user (id)
);