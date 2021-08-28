#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import sys
import configparser
import fasteners
import traceback

from rpi_epd2in7.epd2in7 import EPD
from PIL import Image,ImageDraw,ImageFont

LOCKFILE = '/tmp/lockepaper'

# 176x264
FONT_FILE = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
TITLE_Y = 0
TITLE_SZ = 18


def disp_qrcode(png_file, title_str, clear_frame):
    lock = fasteners.InterProcessLock(LOCKFILE)
    if not lock.acquire():
        print('now using')
        return

    try:
        print('init')
        epd = EPD()
        epd.init()

        if clear_frame:
            print('clear')
            epd.Clear(0xFF)

        else:
            print('display')
            image = Image.new('1', (epd.width, epd.height), 255)
            image = _disp_image(epd, image, png_file)
            image = _disp_title(epd, image, title_str)
            epd.display(epd.getbuffer(image))

        epd.sleep()
    except:
        print('exception')
        print('traceback.format_exc():\n%s' % traceback.format_exc())

    lock.release()


def _disp_image(epd, image, png_file):
    if os.path.isfile(png_file):
        print('PNG file' + png_file)
        img = Image.open(png_file);
        px = int((epd.width - img.size[0]) / 2)
        py = int((epd.height - img.size[1]) / 2)
        image.paste(img, (px, py))
    return image


def _disp_title(epd, image, title_str):
    if len(title_str) > 0:
        print('title')
        print(title_str)
        draw = ImageDraw.Draw(image)
        imgfont = ImageFont.truetype(FONT_FILE, TITLE_SZ)
        height = TITLE_Y
        for title in title_str:
            if title.isdecimal():
                title = '{:,}'.format(int(title))
            draw_sz = draw.textsize(title, font = imgfont)
            draw_pos = ((epd.width - draw_sz[0]) / 2, height)
            draw.text(draw_pos, title, font = imgfont, fill = 0)
            height += TITLE_SZ
    return image


# arg none: clear
# arg[1]: PNG filename
# arg[2]: title
def main():
    print('start')
    clear_frame = False
    png_file = ''
    title_str = ''
    if len(sys.argv) < 3:
        clear_frame = True
    else:
        png_file = sys.argv[1]
        title_str = sys.argv[2:]

    disp_qrcode(png_file, title_str, clear_frame)


if __name__ == '__main__':
    main()
