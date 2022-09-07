def save_pic(picture) -> str:
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path