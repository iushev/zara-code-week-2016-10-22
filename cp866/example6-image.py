# -*- coding: 866 -*-


def jpeg_res(filename):
    """"���� �㭪�� �⯥�⢠ १������ �� JPEG ����ࠦ����"""

    # �⢠�ﭥ �� 䠩�� � ����祭 ०��
    with open(filename, 'rb') as img_file:

        # ���稭�� �� ����ࠦ����� � �� 164-� ������
        img_file.seek(163)

        # ���⠭� �� 2 ����
        a = bytearray(img_file.read(2))

        # ������ �� ���稭��
        height = (a[0] << 8) + a[1]

        # ᫥����� 2 ���� � ��稭��
        a = bytearray(img_file.read(2))

        # ������ �� ��稭��
        width = (a[0] << 8) + a[1]

    return {
        'width': width,
        'height': height
    }


res = jpeg_res("img.jpg")
print("��������� � {width}x{height}".format(**res))

print("��������� � {width}x{height}".format(**jpeg_res("image-resolution.jpg")))
