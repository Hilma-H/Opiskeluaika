CREATE TABLE IF NOT EXISTS "accountStudent" (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE courses (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE hours (
	id INTEGER NOT NULL, 
	timehours INTEGER NOT NULL, 
	courses_id INTEGER, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(courses_id) REFERENCES courses (id), 
	FOREIGN KEY(account_id) REFERENCES "accountStudent" (id)
);

Huom. Hours taulun courses_id voi olla null, koska näin sain kurssin poiston toimimaan. En halunnut, että yksittäidet kirjaukset poistuisivat kurssin mukana.