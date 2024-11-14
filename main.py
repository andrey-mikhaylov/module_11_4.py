from PIL import Image, ImageDraw


class Pic:
    def __init__(self, path):
        self.img = Image.open(path)

    def print_info(self):
        print(self.img.format, self.img.mode, self.img.size)

    def crop(self, left, upper, wdt, hgt):
        self.img = self.img.crop((left, upper, left+wdt, upper+hgt))

    def resize(self, new_w, new_h):
        self.img = self.img.resize((int(new_w), int(new_h)))

    def width(self):
        return self.img.width

    def height(self):
        return self.img.height

    def show(self, title=''):
        self.img.show(title)

    def save(self, path):
        self.img.save(path)

    def paste(self, other, x, y):
        self.img.paste(other.img, (x, y))

    def print(self, text, x, y):
        draw = ImageDraw.Draw(self.img)
        draw.text((x, y), text, font_size=50)


def test1():
    #img = Image.new('RGB', (200, 200), (255, 255, 0))
    #img = Image.open("images.jpg")
    img = Image.open("high.webp")
    img.show()
    print(img.format, img.mode, img.size)
    img2 = img.crop((13, 418, 652+13, 493+418))
    img2.show()
    img2.save("out.jpg")


def test2():
    img = Pic("high.webp")
    img.print_info()
    img.crop(16, 420, 650, 490)
    img.print_info()
    #img.show()
    #img.save("out.jpg")

    img2 = Pic("images.jpg")
    img2.print_info()
    img2.resize(img2.width()/2, img2.height()/2)
    img2.print_info()
    img.paste(img2, 530, 5)
#    img.show()
#    img.save("out.jpg")

    img.print('bober', 10, 10)
    img.show()
    img.save("out.jpg")


if __name__ == '__main__':
    #test1()
    test2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
Д2023/12/27 00:00|Лекция. Практика. 1.1
Практика. Часть 1
Сторонние библиотеки
Для выполнения задачи нужно:

1) Создать изображение, на котором будет сгенерирована надпись с помощью Python.

2) Найти подходящие методы обработки изображений на Python, изучить библиотеки, такие как PIL или OpenCV.

3) Найти учебные материалы (туториалы) по обработке изображений в Python.

4) Изучить документацию по библиотекам для обработки изображений, чтобы лучше понять их возможности.

5) Разработать код с использованием интроспекции, позволяющий исследовать атрибуты объектов и их методы.

6) Инкапсулировать все в один класс и протестировать запуск кода.


2023/12/28 00:00|Лекция. Практика. 1.2
Практика. Часть 2
Продолжаем работу с библиотекой Pillow и создаём открытку, на которую поместим изображение и текст.

1) Сначала необходимо сохранить длину и ширину изображения в переменные. Это можно сделать следующим образом: 'width, height = im.size'.

2) Затем можно изучить атрибуты объекта Image. Для этого, нажав Ctrl и перейдя к методу size, можно увидеть, что он возвращает кортеж (tuple), который состоит из двух значений типа int. Это именно ширина и высота изображения.

3) Используя эти значения, можно затем построить открытку, добавив изображение и текст. Это поможет узнать характеристики изображения и подготовить его для дальнейшей обработки.


2023/12/29 00:00|Лекция. Практика. 1.3
Практика. Часть 3


"""