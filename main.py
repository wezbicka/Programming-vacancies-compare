import requests
from itertools import count


PROGRAMMING_LANGUAGES = [
    "GO",
    "JavaScript",
    "Java",
    "Python",
    "Ruby",
    "PHP",
    "C++",
    "C#",
    "C",
    "TypeScript",
]


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    elif salary_from:
        return salary_from * 1.2
    elif salary_from:
        return salary_from * 0.8


def count_average_salary(salaries):
    salaries_amount = sum(salaries)
    count = len(salaries)
    average_salary = 0
    if count:
        average_salary = int(salaries_amount / count)
    return average_salary, count


def get_response():
    url = "https://api.hh.ru/vacancies/"
    # payload = {
    #     "text": f"Программист {programing_language}",
    #     "area": "1",
    #     "period": 30
    #     }
    # response = requests.get(url, params=payload)
    # response.raise_for_status()
    # return response.json()
    general_statistic = {}
    for language in PROGRAMMING_LANGUAGES:
        salaries = []
        language_static = {}
        for number_page in count(0):
            payload = {
                "per_page": 100,
                "text": f"Программист {language}",
                "area": "1",
                "period": 30
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
        language_static['vacancy_amount'] = vacancies_amount
        language_static['vacancies_processed'] = vacancies_processed
        language_static['average_salary'] = average_salary
        general_statistic[language] = language_static
    return general_statistic


def print_salary(programing_language):
    decoded_response = get_response(programing_language)
    for vacancy in decoded_response["items"]:
        print(vacancy["salary"])


def statistic_count_vacancies(programing_languages):
    languages_statistic = {}
    for lang in programing_languages: 
        languages_statistic[lang] = {}
        pages = get_response(lang)
        salaries = []
        for page in pages:
            count = get_count_vacancies(page)
            languages_statistic[lang]["vacancies_found"] = count
            vacancies = pages[page]["items"]
            for vacancy in vacancies:
                salary = predict_salary(vacancy)
                salaries.append(salary)
        vacancies_processed, average_salary = count_average_salary(salaries)
        languages_statistic[lang]["vacancies_processed"] = vacancies_processed
        languages_statistic[lang]["average_salary"] = average_salary
    print(languages_statistic)


def main():
    
    # decoded_response = get_response("Python")
    # vacancies = decoded_response["items"]
    # for vacancy in vacancies:
    #     salary = predict_rub_salary(vacancy)
    #     print(salary)

    #statistic_count_vacancies(programing_languages)
    # get_response("Python")
    # print_salary("Python")
    # for language in programing_languages:
    #     pass
    print(get_response())


if __name__ == "__main__":
    main()
