from db_manager import DBManager
from database_create import create_db, execute_sql, insert_data
from function import get_data_employers, get_vacancies
from config import config


def main():
    url = 'https://api.hh.ru/employers'
    db_name = 'database_hh'
    create_file = 'create.sql'
    params = config()

    employers = get_data_employers(url)  # получаем список компаний
    vacancies = get_vacancies(employers)  # получаем список вакансий

    create_db(params, db_name)  # создание базы данных
    execute_sql(params, db_name, create_file)  # создание таблиц в базе данных
    insert_data(params, db_name, employers, vacancies)  # добавление данных в таблицы

    db = DBManager(params, db_name)


    print("Привет! Программа умеет выполнять следующие функции:")
    print("1 - Вывести список всех компании и количество вакансий у каждой")
    print("2 - Вывести список всех вакансий с указанием вакансии, компании, зарплаты и ссылки на вакансию")
    print("3 - Вывести среднюю зарплату по вакансиям")
    print("4 - Вывести список всех вакансий, у которых зарплата выше среднего")
    print("5 - Вывести список список всех вакансий по заданному слову")
    number = input('Введите номер функции, которая должна быть выполнена: ')
    if number == "1":
        db.get_companies_and_vacancies_count()
    elif number == "2":
        db.get_all_vacancies()
    elif number == "3":
        db.get_avg_salary()
    elif number == "4":
        db.get_vacancies_with_higher_salary()
    elif number == "5":
        keyword = input('Введите слово: ')
        db.get_vacancies_with_keyword(keyword.lower())
    else:
        print("Неверная команда!")


if __name__ == '__main__':
    main()