#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# ImageResizer v. 1.0.3

# http://pillow.readthedocs.org/en/latest/index.html
# перед использованием библиотеки ставим ее
# pip install Pillow

from __future__ import print_function
from colorama import init, Fore
import os
import sys
import datetime
import time
import fnmatch
import re
import PIL
from PIL import Image
from PIL import ImageFilter
from PIL.ExifTags import TAGS
import argparse

#############################################################
# Параметры
#############################################################

# значения по умолчанию
inDir = '.' # папка где ищем изображения
outDir = 'resize' # выходная папка
# поддерживаемые форматы
myTypeFiles = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.tif', '*.tiff', )
newWidth = 750 # ширина по умолчанию
qua = 70 # качество по умолчанию

#############################################################
# определяем функции
#############################################################

# расчитываем размеры картинок
def resize_img (size, _width) :
    if size[0] > _width :
        h = int(size[1]/(size[0]/_width))
        if h < 1 :
            newSize = (_width, 1)
        else : 
            newSize = (_width, h)
    else :
        newSize = size
    return newSize

# Функция выдачи сообщения
def report (message, error = False) :
    if error :
        init()
        print (Fore.RED + 'ERROR: ' + message + Fore.RESET)
        input('Нажмите [Enter] для выхода')
        sys.exit()
    else :
        init()
        print (Fore.YELLOW + message)
        input('Нажмите [Enter] для выхода')

# прогресс бар
def progressbar(it, prefix = "", size = 60):
    count = len(it)
    def _show(_i):
        x = int(size*_i/count)
        print("%s[%s%s] %i/%i\r" % (prefix, "\u25A0"*x, "."*(size-x), _i, count), end='')
        sys.stdout.flush()
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    print()

# получаем ориентацию снимка
def get_orientation(pict):
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in pict._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    return exif['Orientation']

# выводим кортеж из имени файла и его расшерения
def imagename(il) :
    regexp = r'(.+)\.([A-Za-z0-9]+$)'
    rrr = []
    for k in range (len(il)):
        e = [re.sub(regexp, r'\1', il[k]), re.sub(regexp, r'\2', il[k])]
        rrr.append(e)
    return rrr

# сопоставляем типы вывода и  расшения файлов
def conf(imgtype, pil = False) :
    if pil :
        if imgtype == 'jpg' or imgtype == 'jpeg' or imgtype == 'tif' or imgtype == 'tiff' or imgtype == 'JPG' or imgtype == 'JPEG' or imgtype == 'TIF' or imgtype == 'TIFF':
            return 'jpeg'
        elif imgtype == 'png' or imgtype == 'PNG':
            return imgtype
        elif imgtype == 'gif' or imgtype == 'GIF':
            return imgtype
    else :
        if imgtype == 'jpg' or imgtype == 'jpeg' or imgtype == 'tif' or imgtype == 'tiff' or imgtype == 'JPG' or imgtype == 'JPEG' or imgtype == 'TIF' or imgtype == 'TIFF':
            return 'jpg'
        elif imgtype == 'png' or imgtype == 'PNG':
            return imgtype
        elif imgtype == 'gif' or imgtype == 'GIF':
            return imgtype     
        

def createParser ():
    parser = argparse.ArgumentParser(
        prog = 'resize',
        description = 'RESIZE 1.0.3 \nСкрипт для массвого ресайза и конвертирования изображений в текущей папке в формат jpg для web. Поддерживаемые форматы: jpg, png, gif, tif.',
        epilog = '(c) vetl1489, 2015.',
        # add_help = False,
        )
    parser.add_argument ('-w', '--width', nargs='?', default=newWidth, type=int, help='Ширина изображения, по-умолчанию 750px', metavar='ШИРИНА' )
    parser.add_argument ('-d', '--dir', nargs='?', default=outDir, help='Папка с результирующими изображениями', metavar='ПАПКА')
    parser.add_argument ('-q', '--quality', nargs='?', type=int, default=qua, help='Качество выходного файла jpg, по-умолчанию 70', metavar='КАЧЕСТВО')
    return parser


#############################################################
# Программа
#############################################################

# засекаем таймер
start = time.time()


parser = createParser()
args = parser.parse_args(sys.argv[1:])

newWidth = args.width
outDir = args.dir
if args.quality <= 96 and args.quality >= 1 :
    qua = args.quality
else: 
    report ('Неверно указано качество изображения (1 <= quality <= 96)', error=True)

# находим все картинки в папке
ImageList = []
for i in range (len(myTypeFiles)) :
    ImageList.extend ( imagename(fnmatch.filter(os.listdir(inDir), myTypeFiles[i])) )
if len(ImageList) < 1 :
    report ('Отсутствуют изображения для обработки', error=True)

# делаем папочку для сохранения изображений
if len(ImageList) > 0 :
    if not os.path.exists(outDir) :
        os.mkdir(outDir)

init(autoreset=False)
print (Fore.CYAN + '', end = '')


# ресайзим
for j in progressbar(range(len(ImageList)), "Ресайзим: ", 30):
    im = Image.open(ImageList[j][0] + '.' + ImageList[j][1])
    try:
        orient = get_orientation(im)
        if orient == 6:
            outImg = im.transpose(Image.ROTATE_270)
        elif orient == 8:
            outImg = im.transpose(Image.ROTATE_90)
        elif orient == 3:
            outImg = im.transpose(Image.ROTATE_180)
        else:
            outImg = im
    except: 
        outImg = im
    
    outImg = outImg.resize( resize_img(outImg.size, newWidth), Image.LANCZOS )
    outImg = outImg.filter(ImageFilter.SHARPEN)
    out = os.path.join( outDir, ImageList[j][0] + '.' + conf(ImageList[j][1]) )
    outImg.save (out, conf(ImageList[j][1], pil=True), quality = qua)

if outDir == '.' :
    print (Fore.RESET + 'Готово! Изображения сохранены в ' + Fore.YELLOW + 'текущей папке' + Fore.RESET)
else :
    print (Fore.RESET + 'Готово! Изображения сохранены в папке ' + Fore.YELLOW + outDir + Fore.RESET)

print ("Время выполнения: {:.3f} сек.".format(time.time() - start))
input('Нажмите [Enter] для выхода')


 
