#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 02:01:18 2017

@author: JUN
"""

from PIL import Image

# 画像合成
# -------------------------------------------------------------
def layover():
    
    img = Image.open('temp/share0.png')
    
    #オリジナル画像の幅と高さを取得
    width, height = img.size

    img.close
    
    #取得したサイズと同じ空のイメージを新規に作成
    img2 = Image.new('RGB', (width, height))

    for num in range(3):
        img = Image.open('temp/share' + str(num) + '.png')
        for y in range(height):
            for x in range(width):
                r,g,b,c = img.getpixel((x,y))
                #取得したピクセルの透過情報が0ならputする
                if c == 0:
                    img2.putpixel((x, y), (r, g, b, c))
        img.close

    img2.save('temp/shared.png')
    
# main
# -------------------------------------------------------------
layover()