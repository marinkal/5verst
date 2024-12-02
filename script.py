import re
import requests
import time

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from helpers import get_sorted_rows

saturday = '16.09.2023'
cat = 'Ж30-34'
url = f'https://5verst.ru/results/all/'


def process_page_rows(page_rows: list) -> list[dict]:
    pattern_time = r'\d{2}:\d{2}:\d{2}'
    pattern_cat = r'[МЖ]\d{2}(-\d{2})?'
    page_runners = []
    for p_row in page_rows:
        is_write, time_p = True, None  # у незарегистрированных пользователей в протоколе не всегда фиксируется время
        for child in p_row:
            if re.match(pattern_time, child.get_text()):
                time_p = child.get_text()
            if m := re.match(pattern_cat, child.get_text()):
                if m[0] != cat:
                    is_write = False
                    break
        if is_write and time_p:
            new_row = {'row': p_row, 'time': time_p}
            page_runners.append(new_row)
    
    return page_runners


def process_page(row):
    href = row.attrs['href'].replace('all', f'{saturday}/')
    response = requests.get(href)
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    page_rows = soup.select('tbody tr')
    if not page_rows:
        return []

    return process_page_rows(page_rows)


def get_all_runners():
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.select('tbody tr>td div a')

    with ThreadPoolExecutor(max_workers=8) as executor:
        runners_exec = [
            executor.submit(process_page, row)
            for row in rows
        ]

    all_runners = []
    for part in runners_exec:
        all_runners.extend(part.result())

    return all_runners

   
start = time.time()
all_runners = get_all_runners()
sorted_runners = get_sorted_rows(all_runners)
print(sorted_runners)
end = time.time()
print(end-start)

