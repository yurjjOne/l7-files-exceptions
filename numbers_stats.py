"""Л7, ДЗ 2. Числа з файлу з помилками: сума, мінімум, максимум.

Автор: Михайлюк Юрій, група МІТ-1026г
Обробляються: відсутній файл, порожні рядки, текст замість числа, кома замість крапки.
"""


def read_numbers(filename):
    """Повертає список чисел з файлу або None, якщо файлу немає."""
    numbers = []
    try:
        with open(filename, encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                text = line.strip()
                if text == "":
                    continue
                try:
                    numbers.append(float(text))
                except ValueError:
                    print(f"Рядок {line_no}: '{text}' не число — пропускаю")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено")
        return None
    return numbers


def stats(numbers):
    """(сума, мінімум, максимум); для порожнього списку — ValueError."""
    if len(numbers) == 0:
        raise ValueError("у файлі немає жодного числа")
    return sum(numbers), min(numbers), max(numbers)


if __name__ == "__main__":
    name = input("Ім'я файлу (Enter — numbers.txt): ").strip() or "numbers.txt"
    nums = read_numbers(name)
    if nums is not None:
        try:
            total, low, high = stats(nums)
            print("Чисел:", len(nums))
            print("Сума:", total)
            print("Мінімум:", low)
            print("Максимум:", high)
        except ValueError as e:
            print("Помилка:", e)
