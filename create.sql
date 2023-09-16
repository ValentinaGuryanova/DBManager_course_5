DROP TABLE IF EXISTS employers;

DROP TABLE IF EXISTS vacancies;

CREATE TABLE employers (
    company_id integer PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    company_url varchar(100),
    company_open_vacancies integer,
    vacancies_url varchar(100)
    );

CREATE TABLE vacancies (
    vacancy_id integer PRIMARY KEY,
    vacancy_name varchar(100) NOT NULL,
    company_id integer REFERENCES employers(company_id),
    city varchar(50) NOT NULL,
    salary_from integer,
    salary_to integer,
    currency varchar(10) NOT NULL,
    vacancy_url varchar(100) NOT NULL
);
