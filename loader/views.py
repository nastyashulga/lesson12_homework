import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_pic

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')

@loader_blueprint.route('/post, methods=["POST"]')
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return "Нет картинки или текста"
    elif picture.filename.split(".")[-1] not in ['jpeg', 'png']:
        logging.info('загружен файл а не картинка')
        return "Неверное раширение файла"
    try:
        picture_path: str = '/' + save_pic(picture)
    except FileNotFoundError:
        logging.error('Фаил не найде')
        return "Фаил не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)