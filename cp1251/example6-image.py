# -*- coding: 1251 -*-


def jpeg_res(filename):
    """"Тази функция отпечатва резолюцията на JPEG изображение"""

    # отваряне на файла в двоичен режим
    with open(filename, 'rb') as img_file:

        # височината на изображението е на 164-та позиция
        img_file.seek(163)

        # прочитане на 2 байта
        a = bytearray(img_file.read(2))

        # изчисляване на височината
        height = (a[0] << 8) + a[1]

        # следващите 2 байта са широчината
        a = bytearray(img_file.read(2))

        # изчисляване на щирочината
        width = (a[0] << 8) + a[1]

    return {
        'width': width,
        'height': height
    }


res = jpeg_res("img.jpg")
print("Резолюцията е {width}x{height}".format(**res))

print("Резолюцията е {width}x{height}".format(**jpeg_res("image-resolution.jpg")))
