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

CREATE TABLE authors (
	id INTEGER PRIMARY KEY,
	author_name TEXT	
)

CREATE TABLE recipe (
	id INTEGER PRIMARY KEY,
	recipe_name TEXT,
	rating INTEGER CHECK (rating >= 1 AND rating <= 5)),
	author_id INTEGER,
	submitter_id INTEGER,
	url TEXT,
	FOREIGN KEY (submitter_id) REFERENCES user(id)
	FOREIGN KEY (author_id) REFERENCES authors(id)
	
);