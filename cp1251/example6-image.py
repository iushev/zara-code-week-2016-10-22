# -*- coding: 1251 -*-


def jpeg_res(filename):
    """"���� ������� ��������� ����������� �� JPEG �����������"""

    # �������� �� ����� � ������� �����
    with open(filename, 'rb') as img_file:

        # ���������� �� ������������� � �� 164-�� �������
        img_file.seek(163)

        # ��������� �� 2 �����
        a = bytearray(img_file.read(2))

        # ����������� �� ����������
        height = (a[0] << 8) + a[1]

        # ���������� 2 ����� �� ����������
        a = bytearray(img_file.read(2))

        # ����������� �� ����������
        width = (a[0] << 8) + a[1]

    return {
        'width': width,
        'height': height
    }


res = jpeg_res("img.jpg")
print("����������� � {width}x{height}".format(**res))

print("����������� � {width}x{height}".format(**jpeg_res("image-resolution.jpg")))
