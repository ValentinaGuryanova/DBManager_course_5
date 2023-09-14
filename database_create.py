import psycopg2


def create_db(params: dict, db_name: str,) -> None:
    """Создание новой базы данных"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    try:
        cur = conn.cursor()
        cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
        cur.execute(f'CREATE DATABASE {db_name}')
    finally:
        conn.close()


def execute_sql(params, db_name, create_file) -> None:
    """Создание таблицы в базе данных по коду в файле create.sql."""

    with psycopg2.connect(**params, database=db_name) as conn:
        with conn.cursor() as cur:
            with open(create_file, 'r') as file:
                sql_command = file.read()
            cur.execute(sql_command)
    conn.close()


def insert_data(params, db_name, employers, vacancies) -> None:
    """Добавление данных в таблицы 'employers' и 'vacancies'."""

    with psycopg2.connect(**params, database=db_name) as conn:
        with conn.cursor() as cur:
            for employee in employers:
                cur.execute(
                    "INSERT INTO "
                    "employers (company_id, company_name, company_url, company_open_vacancies, vacancies_url) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (employee['company_id'], employee['company_name'], employee['company_url'],
                     employee['company_open_vacancies'], employee['vacancies_url'])
                )

            for vacancy in vacancies:
                cur.execute(
                    "INSERT INTO "
                    "vacancies (vacancy_id, vacancy_name, company_id, city, salary_from, salary_to, currency, vacancy_url) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (vacancy['vacancy_id'], vacancy['vacancy_name'], vacancy['company_id'],
                     vacancy['city'], vacancy['salary_from'], vacancy['salary_to'],
                     vacancy['salary_currency'], vacancy['vacancy_url'])
                )
    conn.close()