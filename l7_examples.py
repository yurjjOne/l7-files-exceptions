"""Л7, ДЗ 1. Приклади з лекції: спершу прогноз (коментар «прогноз»), потім запуск.

Архіву l7_files.zip у Classroom немає, тому десять прикладів узято зі слайдів
і конспекту Л7 — по одному на кожну тему l7_01 … l7_10.
Усі файли створюються в тимчасовій папці й видаляються після запуску.
"""
import csv
import json
import os
import tempfile

tmp = tempfile.mkdtemp()
data_txt = os.path.join(tmp, "data.txt")

print("--- 01. Запис \"w\" і читання \"r\"")
with open(data_txt, "w", encoding="utf-8") as f:
    f.write("Перший рядок\n")
    f.write("Другий рядок\n")
    f.write("Третій рядок\n")
with open(data_txt, encoding="utf-8") as f:
    print(len(f.read()))
# прогноз: 39 (12 + 1 + 12 + 1 + 12 + 1)

print("--- 02. Дописування \"a\"")
with open(data_txt, "a", encoding="utf-8") as f:
    f.write("Четвертий рядок\n")
with open(data_txt, encoding="utf-8") as f:
    print(len(f.readlines()))
# прогноз: 4

print("--- 03. Курсор: другий read() порожній")
with open(data_txt, encoding="utf-8") as f:
    first = f.read()
    second = f.read()
print(len(first) > 0, repr(second))
# прогноз: True ''

print("--- 04. Кодування")
word = "Привіт"
print(len(word), len(word.encode("utf-8")))
# прогноз: 6 12

print("--- 05. try / except / else / finally")
for text in ("5", "abc", "0"):
    try:
        n = int(text)
        r = 100 / n
    except ValueError:
        print(text, "-> не ціле число")
    except ZeroDivisionError:
        print(text, "-> ділити на нуль не можна")
    else:
        print(text, "->", r)
    finally:
        pass
# прогноз: 5 -> 20.0 / abc -> не ціле число / 0 -> ділити на нуль не можна

print("--- 06. Текст помилки")
try:
    int("12x")
except ValueError as e:
    print(e)
# прогноз: invalid literal for int() with base 10: '12x'

print("--- 07. FileNotFoundError")
try:
    open(os.path.join(tmp, "no_such_file.txt"), encoding="utf-8")
except FileNotFoundError:
    print("Файл не знайдено")
# прогноз: Файл не знайдено

print("--- 08. raise")
def average(numbers):
    if len(numbers) == 0:
        raise ValueError("Список порожній")
    return sum(numbers) / len(numbers)
for d in ([4, 5, 3], []):
    try:
        print(average(d))
    except ValueError as e:
        print("Помилка:", e)
# прогноз: 4.0 / Помилка: Список порожній

print("--- 09. CSV і JSON")
students = [{"name": "Оля", "grade": 5}, {"name": "Іван", "grade": 4}]
p_csv = os.path.join(tmp, "s.csv")
with open(p_csv, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "grade"])
    for s in students:
        w.writerow([s["name"], s["grade"]])
with open(p_csv, encoding="utf-8", newline="") as f:
    print([row["grade"] for row in csv.DictReader(f)])
p_json = os.path.join(tmp, "s.json")
with open(p_json, "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False)
with open(p_json, encoding="utf-8") as f:
    print(json.load(f) == students)
# прогноз: ['5', '4'] (CSV — рядки) / True (JSON пам'ятає типи)

print("--- 10. lambda")
prices = {"apple": 30, "milk": 45, "bread": 25}
print(sorted(prices.items(), key=lambda p: p[1]))
print(max(prices.items(), key=lambda p: p[1]))
# прогноз: [('bread', 25), ('apple', 30), ('milk', 45)] / ('milk', 45)

for name in os.listdir(tmp):
    os.remove(os.path.join(tmp, name))
os.rmdir(tmp)
