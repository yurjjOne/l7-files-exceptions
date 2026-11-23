"""Л7, ДЗ 3. Збереження й завантаження списку словників у JSON і CSV.

Автор: Михайлюк Юрій, група МІТ-1026г
"""
import csv
import json


def save_json(items, filename):
    """Записати список словників у JSON (українські літери — відкритим текстом)."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def load_json(filename):
    """Прочитати список з JSON. Немає файлу або файл пошкоджений — порожній список."""
    try:
        with open(filename, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено — починаємо з порожнього списку")
        return []
    except json.JSONDecodeError:
        print(f"Файл {filename} пошкоджений — починаємо з порожнього списку")
        return []


def save_csv(items, filename, fields):
    """Записати список словників у CSV з заголовком fields."""
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(items)


def load_csv(filename, int_fields=()):
    """Прочитати CSV у список словників; поля з int_fields перетворити на int."""
    try:
        with open(filename, encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено — починаємо з порожнього списку")
        return []
    for row in rows:
        for field in int_fields:
            row[field] = int(row[field])
    return rows


def average_grade(students):
    """Середня оцінка; для порожнього списку — ValueError."""
    if len(students) == 0:
        raise ValueError("список студентів порожній")
    return sum(s["grade"] for s in students) / len(students)


if __name__ == "__main__":
    students = load_json("students.json")
    if not students:
        students = [{"name": "Оля", "grade": 5}, {"name": "Іван", "grade": 4},
                    {"name": "Марко", "grade": 3}]
    save_json(students, "students.json")
    save_csv(students, "students.csv", ["name", "grade"])

    print("JSON:", load_json("students.json") == students)
    print("CSV:", load_csv("students.csv", int_fields=["grade"]) == students)
    print("Середня оцінка:", round(average_grade(students), 2))
