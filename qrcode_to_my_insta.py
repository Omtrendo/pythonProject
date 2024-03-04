import pyqrcode

s = 'https://www.instagram.com/allaomtrendo/'
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)