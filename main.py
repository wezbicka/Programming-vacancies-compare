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


def get_count_vacancies(programing_language):
    count = get_response(programing_language)["found"]
    return count


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
    languages_statistic = {}
    for lang in programing_languages:
        count = get_count_vacancies(lang)
        languages_statistic[lang] = count
    print(languages_statistic)
    print_salary("Python")


if __name__ == "__main__":
    main()
