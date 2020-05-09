# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:58:56 2020

@author: Lokesh Kumar
""" 
import qrcode
qr=qrcode.QRCode(
    version=1,box_size=25,border=5)
data="hi!"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="green",back_color="blue")
img.save("sample1.png")