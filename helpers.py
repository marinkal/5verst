from datetime import datetime


def get_sorted_rows(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda row: datetime.strptime(row['time'], '%H:%M:%S').time())


def generate_sequence(letter):
    for i in range(10, 81, 5):
        if i < 80:
            yield f"{letter}{i}-{i+4}"


def test_get_sorted_rows():
    rows = [
        {'text': 'и тут тоже неважно', 'time': '00:29:17'},
        {'text': 'все равно что тут', 'time': '00:16:20'},
        {'text': 'и тут все равно', 'time': '01:02:07'},
    ]
    waiting_rows = [
        {'text': 'все равно что тут', 'time': '00:16:20'},
        {'text': 'и тут тоже неважно', 'time': '00:29:17'},
        {'text': 'и тут все равно', 'time': '01:02:07'}
    ]
    result = get_sorted_rows(rows)
    assert waiting_rows == result

