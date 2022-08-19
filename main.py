import requests


def get_response(programing_language):
    url = "https://api.hh.ru/vacancies/"
    payload = {
        "text": f"Программист {programing_language}",
        "area": "1",
        "period": 30
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


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


def get_count_vacancies(programing_language):
    count = get_response(programing_language)["found"]
    return count


def statistic_count_vacancies(programing_languages):
    languages_statistic = {}
    for lang in programing_languages:
        count = get_count_vacancies(lang)
        languages_statistic[lang] = {}
        languages_statistic[lang]["vacancies_found"] = count
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


if __name__ == "__main__":
    main()
