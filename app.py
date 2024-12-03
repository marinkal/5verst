from flask import Flask, render_template
from bs4 import BeautifulSoup as BS
from helpers import generate_sequence, get_sorted_rows, validate
from script import get_all_runners
app = Flask(__name__)


@app.route('/')
def index():
    women = 'Ж10, ' + ', '.join(generate_sequence('Ж'))
    men = women.replace('Ж', 'М')

    return render_template('main.html', href='http://127.0.0.1:5000/16.09.2023/Ж30-34',
                           women=women, men=men)


@app.route('/<string:_date>/<string:category>')
def route_main(_date, category):
    category = category.upper()
    success, errors = validate(category, _date)
    if not success:
        return render_template('error.html', errors=errors)

    all_runners = get_all_runners(_date, category)
    raiting = get_sorted_rows(all_runners)
    index = 1
    result = '<Table border=1>'
    for person in raiting:
        placeTag = BS(f'<div>{index}</div>', features='html.parser')
        person['row'].select_one('div').replaceWith(placeTag)
        row = str(person['row'])
        index += 1
        result += row

    return result+'</Table>'
