import base64

# Открываем изображение в бинарном режиме
with open("photos/photo_10@14-09-2024_16-46-08.jpg", "rb") as image_file:
    # Кодируем изображение в base64
    base64_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(base64_string)
