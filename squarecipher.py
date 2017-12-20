#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 05:29:27 2017

@author: JUN
"""

from PIL import Image
from pyzbar.pyzbar import decode


# ビット化
# -------------------------------------------------------------
def toBit():
    f = open('temp/square.txt',"r")
    b = open('temp/squarebit.txt',"w")

    for line in f:
        for char in line:
            if char.islower() and char.isalpha():
                b.write('1')
            elif char.isupper() and char.isalpha():
                b.write('0')
            else:
                b.write("\n")

    f.close
    b.close


# 画像化
# -------------------------------------------------------------
def toQR():
    
    # 画像サイズ定義
    width, height = 31, 31
 
    #取得したサイズと同じ空のイメージを新規に作成
    img2 = Image.new('RGB', (width, height))
    
    b = open('temp/squarebit.txt',"r")
    numY = 0
    for line in b:
        numX = 0
        for char in line:
            if char == '1':
                img2.putpixel((numX, numY), (255, 255, 255))
            elif char == '0':
                img2.putpixel((numX, numY), (0, 0, 0))     
            numX = numX + 1
        numY = numY + 1
        
    b.close
    
    img2.save('temp/qr.png')

# 画像拡大
# -------------------------------------------------------------
def expand():
    
    #拡大率
    mag = 10; 

    img = Image.open('temp/qr.png')
    
    #オリジナル画像の幅と高さを取得
    width, height = img.size
    
    #取得したサイズと同じ空のイメージを新規に作成
    img2 = Image.new('RGB', (width * mag, height * mag))

    for y in range(height):
        for x in range(width):
            r,g,b = img.getpixel((x,y))
            for exy in range(y * mag, y * mag + mag):
                for exx in range(x * mag, x * mag + mag):
                    img2.putpixel((exx, exy), (r, g, b))

    img.close

    img2.save('temp/expanded_qr.png')


# QRコード読み込み
# -------------------------------------------------------------
def readQR():
    # 画像ファイルの指定
    img = Image.open('temp/expanded_qr.png')
    
    # QRコードの読取り
    data = decode(img)
    
    # コード内容を出力
    print(data[0][0].decode('utf-8', 'ignore'))
    
# main
# ------------------------------------------------------------- 
if __name__ == '__main__':
    readQR()
    