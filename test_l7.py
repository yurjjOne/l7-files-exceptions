"""Тести до ДЗ Л7 (запуск: python3 test_l7.py). Працюють у тимчасовій папці."""
import os
import tempfile

from numbers_stats import read_numbers, stats
from storage import save_json, load_json, save_csv, load_csv, average_grade

with tempfile.TemporaryDirectory() as tmp:
    p = os.path.join(tmp, "n.txt")
    with open(p, "w", encoding="utf-8") as f:
        f.write("10\n20.5\nabc\n\n30\n7,5\n-4\n")
    nums = read_numbers(p)
    assert nums == [10.0, 20.5, 30.0, -4.0]
    assert stats(nums) == (56.5, -4.0, 30.0)
    assert read_numbers(os.path.join(tmp, "missing.txt")) is None
    try:
        stats([])
        assert False
    except ValueError:
        pass

    data = [{"name": "Оля", "grade": 5}, {"name": "Іван", "grade": 4}]
    j = os.path.join(tmp, "s.json")
    save_json(data, j)
    assert load_json(j) == data
    assert load_json(os.path.join(tmp, "none.json")) == []
    with open(j, "w", encoding="utf-8") as f:
        f.write("{broken")
    assert load_json(j) == []

    c = os.path.join(tmp, "s.csv")
    save_csv(data, c, ["name", "grade"])
    assert load_csv(c, int_fields=["grade"]) == data
    assert load_csv(os.path.join(tmp, "none.csv")) == []
    assert average_grade(data) == 4.5

print("Усі тести пройдено")
