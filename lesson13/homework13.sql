--users table:
CREATE TABLE students(
id serial PRIMARY KEY,
name VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
age INTEGER NOT NULL,
faculty VARCHAR(13) NOT NULL,
nationality TEXT
);

--audience table:
CREATE TABLE audience(
id serial PRIMARY KEY,
classname VARCHAR(20) NOT NULL,
number_cabinet INTEGER,
user_id INTEGER,
FOREIGN KEY (user_id)
REFERENCES students (id)
ON DELETE CASCADE ON UPDATE NO ACTION
);

-- fill users table
INSERT INTO students (name, surname, age, faculty, nationality)
VALUES
  ('Alex', 'Morozov', 34, 'ATF', 'belarus'),
  ('Ann', 'Ivanova', 32, 'MTF', 'russia'),
  ('Kate', 'Borisova', 25, 'FITR', 'germany');

-- fill posts table
INSERT INTO audience (classname, number_cabinet, user_id)
VALUES
  ('mathematics', 234, 1),
  ('physics', 435, 2),
  ('english', 568, 3);