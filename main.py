"""
בס"ד
Elior Safiev 212795355
ariel david 324929124
yosef haim amedi 211376686
"""

def pentagonal_number(n: int) -> int:
    """1א: מחזיר את המספר הפנטגונלי ה-n"""
    return n * (3 * n - 1) // 2


def pentagonal_range(a: int, b: int) -> list:
    """1ב: מחזיר רשימה של מספרים פנטגונליים מטווח a עד b"""
    return [pentagonal_number(i) for i in range(a, b + 1)]


def digit_sum(n: int) -> int:
    """2: סכום ספרות"""
    return sum(int(d) for d in str(abs(n)))


def gematria_value(text: str) -> int:
    """3: גימטריה בסיסית (א=1, ב=2, ... ת=400)"""
    hebrew_letters = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
        'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
        'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40,
        'נ': 50, 'ן': 50, 'ס': 60, 'ע': 70, 'פ': 80,
        'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
        'ש': 300, 'ת': 400
    }
    return sum(hebrew_letters.get(ch, 0) for ch in text)


def is_prime(n: int) -> bool:
    """4א: בדיקה אם מספר ראשוני"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def twin_of_prime(p: int) -> int | None:
    """
    4ב: מקבל מספר ראשוני ומחזיר את התאום אם קיים.
    אם אין תאום – מחזיר None.
    """
    if not is_prime(p):
        return None
    if is_prime(p - 2):
        return p - 2
    if is_prime(p + 2):
        return p + 2
    return None


def twin_primes_up_to(n: int) -> list:
    """
    4ג: מחזיר רשימה של כל המספרים הראשוניים עד n שיש להם תאום.
    משתמש ב-twin_of_prime.
    """
    result = []
    for i in range(2, n + 1):
        if is_prime(i) and twin_of_prime(i) is not None:
            result.append(i)
    return result


def dict_3_add(d1: dict, d2: dict, d3: dict) -> dict:
    """ממזג שלושה מילונים לפי דרישת התרגיל (tuple של כל הערכים ללא כפילויות)"""
    all_keys = set(d1.keys()) | set(d2.keys()) | set(d3.keys())
    new_dict = {}
    for key in all_keys:
        values = []
        for d in (d1, d2, d3):
            if key in d and d[key] not in values:
                values.append(d[key])
        new_dict[key] = tuple(values)
    return new_dict


# ====== 6א/6ב – פונקציות מתמטיות עם קלט מהמשתמש ======
def double(x):
    return 2 * x

def square(x):
    return x ** 2

def inverse(x):
    if x == 0:
        return "undefined"
    return 1 / x

functions = [double, square, inverse]

def apply_functions(numbers, functions):
    result = {}
    for func in functions:
        result[func.__name__] = [func(n) for n in numbers]
    return result


def main():
    while True:
        print("\nבחר פעולה:")
        print("1א. מספר פנטגונלי יחיד")
        print("1ב. טווח מספרים פנטגונליים")
        print("2. סכום ספרות (digit_sum)")
        print("3. גימטריה")
        print("4א. בדיקה אם ראשוני")
        print("4ב. twin prime")
        print("4ג. מילון twin primes עד n")
        print("5. איחוד שלושה מילונים")
        print("6. פונקציות מתמטיות אונריות")
        print("7. יציאה")
        choice = input(">> ")


        if choice == "1א":
            n = int(input("enter n: "))
            print(pentagonal_number(n))

        elif choice == "1ב":
            a = int(input("enter start: "))
            b = int(input("enter end: "))
            print(pentagonal_range(a, b))

        elif choice == "2":
            n = int(input("enter number: "))
            print(digit_sum(n))

        elif choice == "3":
            text = input("enter text (עברית): ")
            print(gematria_value(text))

        elif choice == "4א":
            n = int(input("enter number: "))
            print(is_prime(n))


        elif choice == "4ב":

            n = int(input("enter number: "))

            result = twin_of_prime(n)

            if result is None:

                print("invalid input")

            else:

                print(result)



        elif choice == "4ג":

            n = int(input("enter max number: "))

            print(twin_primes_up_to(n))



        elif choice == "5":

            d1 = eval(input("הכנס מילון ראשון: "))

            d2 = eval(input("הכנס מילון שני: "))

            d3 = eval(input("הכנס מילון שלישי: "))

            print(dict_3_add(d1, d2, d3))



        elif choice == "6":

            raw = input("הכנס מספרים מופרדים ברווחים (ללא אפסים): ")

            nums = [float(x) for x in raw.split()]

            print(apply_functions(nums, functions))


        elif choice == "7":
            print("bye!")
            break

        else:
            print("invalid input")


if __name__ == "__main__":
    main()
