import requests
from itertools import count
from pprint import pprint


def get_response(programing_language):
    url = "https://api.hh.ru/vacancies/"
    # payload = {
    #     "text": f"Программист {programing_language}",
    #     "area": "1",
    #     "period": 30
    #     }
    # response = requests.get(url, params=payload)
    # response.raise_for_status()
    # return response.json()
    spisok = []
    pages_number = 2
    for page in count():
        payload = {
            'page': page,
            "per_page": 100,
            "text": f"Программист {programing_language}",
            "area": "1",
            "period": 30
        }
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        page_data = page_response.json()
        spisok.append(page_data)
        if page >= page_data["pages"]:
            break
    return spisok


def print_salary(programing_language):
    decoded_response = get_response(programing_language)
    for vacancy in decoded_response["items"]:
        print(vacancy["salary"])


def predict_rub_salary(vacancy):
    salary = vacancy["salary"]
    if salary:
        if salary["currency"] == "RUR":
            if salary['from'] and salary['to']:
                predict_salary = int((salary['from'] + salary['to']) / 2)
                return predict_salary
            elif salary['from']:
                predict_salary = int(salary['from'] * 1.2)
                return predict_salary
            elif salary['to']:
                predict_salary = int(salary['to'] * 0.8)
                return predict_salary


def get_average_salary(salaries):
    total = 0
    count_vacancies = 0
    for salary in salaries:
        if salary:
            count_vacancies += 1
            total += salary
    average_salary = int(total / count_vacancies)
    return count_vacancies, average_salary


def get_count_vacancies(programing_language):
    count = get_response(programing_language)["found"]
    return count


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
                salary = predict_rub_salary(vacancy)
                salaries.append(salary)
        vacancies_processed, average_salary = get_average_salary(salaries)
        languages_statistic[lang]["vacancies_processed"] = vacancies_processed
        languages_statistic[lang]["average_salary"] = average_salary
    print(languages_statistic)


def main():
    programing_languages = [
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
    # decoded_response = get_response("Python")
    # vacancies = decoded_response["items"]
    # for vacancy in vacancies:
    #     salary = predict_rub_salary(vacancy)
    #     print(salary)

    statistic_count_vacancies(programing_languages)
    # get_response("Python")
    # print_salary("Python")
    for language in programing_languages:
        pass

if __name__ == "__main__":
    main()
