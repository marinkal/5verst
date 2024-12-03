from datetime import datetime


def get_sorted_rows(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: datetime.strptime(row['time'], '%H:%M:%S').time())


def generate_sequence(letter):
    for i in range(10, 81, 5):
        if i < 80:
            yield f"{letter}{i}-{i+4}"


def validate_category(category: str) -> bool:
    return category in ('Ж10', 'М10') \
        or category in generate_sequence('Ж') \
        or category in generate_sequence('М')


def validate_sat(sat: str) -> bool:
    format_str = '%d.%m.%Y'
    if len(sat) != 10:
        return False
    try:
        datetime.strptime(sat, format_str)
    except ValueError:
        return False
    return True


def validate(category: str, sat: str) -> tuple[bool, list[str]]:
    errors = []
    if not validate_category(category):
        errors.append(f'Категории {category} не существует')
    if not validate_sat(sat):
        errors.append(f'Неверная дата {sat}')

    if errors:
        return False, errors

    return True, []
