from itertools import count
import os
from dotenv import load_dotenv

import requests
from terminaltables import AsciiTable


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    if salary_from:
        return salary_from * 1.2
    if salary_from:
        return salary_from * 0.8


def count_average_salary(salaries):
    salaries_amount = sum(salaries)
    count = len(salaries)
    average_salary = int(salaries_amount / count) if count else 0
    return average_salary, count


def predict_rub_salary_hh(language):
    url = "https://api.hh.ru/vacancies/"
    salaries = []
    language_statistic = {}
    for number_page in count(0):
        payload = {
            "per_page": 100,
            "text": f"Программист {language}",
            "area": "1",
            "period": 30,
        }
        response = requests.get(url, params=payload)
        response.raise_for_status()
        page = response.json()
        if number_page >= page["pages"]:
            break
        for vacancy in page["items"]:
            salary_range = vacancy['salary']
            if not salary_range:
                continue
            if salary_range['currency'] != 'RUR':
                continue
            vacancy_salary = predict_salary(
                salary_range['from'],
                salary_range['to']
            )
            if vacancy_salary:
                salaries.append(vacancy_salary)
    average_salary, vacancies_processed = count_average_salary(salaries)
    vacancies_amount = page['found']
    language_statistic['vacancies_found'] = vacancies_amount
    language_statistic['vacancies_processed'] = vacancies_processed
    language_statistic['average_salary'] = average_salary
    return language_statistic





def create_table(title, statistic):
    table_header = [
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата',
    ]
    table_data = [
        table_header,
    ]
    for lang, params in statistic.items():
        table_raw = [
            lang,
            params['vacancies_found'],
            params['vacancies_processed'],
            params['average_salary'],
        ]
        table_data.append(table_raw)
    table = AsciiTable(table_data, title)
    return table.table


def main():
    load_dotenv()
    superjob_token = os.environ['SUPERJOB_SECRET_KEY']
    programming_languages = [
        "GO",
        "JavaScript",
        "Java",
        "Python",
        "Ruby",
        "PHP",
        "C++",
        "C#",
        "C",
        "TypeScript"
    ]
    # salary_statistic = {}
    # for language in programming_languages:
    #     salary_statistic[language] = predict_rub_salary_hh(language)
    # title = "HeadHunter Moscow"
    # print(create_table(title, salary_statistic))

    url = "https://api.superjob.ru/2.0/vacancies/"
    header = {
        "X-Api-App-Id": superjob_token,
    }
    response = requests.get(url, headers=header)
    response.raise_for_status()
    print(response.json()['objects'])


if __name__ == "__main__":
    main()
