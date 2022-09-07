import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def main_page():
    return render_template('index.html')

@main_blueprint.route('/search/')
def search_page():
    search_key = request.args.get('s', '')
    logging.info('выполняю поиск')
    try:
        posts = get_posts_by_word(search_key)
    except FileNotFoundError:
        logging.error('Фаил не найде')
        return "Фаил не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template('post_list.html', key=search_key, posts=posts)