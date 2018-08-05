#!/usr/bin/env python3

from PIL import Image
im = Image.open('timg-1.jpg')
w, h = im.size
print('Original image size: %sx%s' % (w,h))

im.thumbnail((w//4, h//4))
print('Resize image to: %sx%s' % (w//4, h//4))
im.save('tumbnail.jpg', 'jpeg')
