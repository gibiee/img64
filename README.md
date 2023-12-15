![PyPI - Version](https://img.shields.io/pypi/v/img64)
![PyPI - Downloads](https://img.shields.io/pypi/dm/img64?color=red)
![PyPI - License](https://img.shields.io/pypi/l/img64)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/img64)

<p align="center">
  <img src="https://github.com/gibiee/img64/assets/37574274/1e4ba6f4-776d-4e84-b589-09f75d64d175" width="50%" height="50%" />
</p>

This library is a tool for converting images to base64 encoding and vice versa.

- It was implemented by referencing [ternaus/base64ToImageConverters](https://github.com/ternaus/base64ToImageConverters).
  - The referenced code didn't ensure data consistency, so this code improves that issue.
  - This code enhances user convenience in handling both RGB and grayscale images.


# Installation
```sh
pip install img64
```


# Quick start

## Convert pil image to base64
```py
from PIL import Image
import img64

image = Image.open('sample.png')
base64 = img64.image_to_base64(image)
base64[:30] # 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
```

## Convert numpy(opencv) image to base64
```py
import cv2
import img64

image = cv2.imread('sample.png')
image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
base64 = img64.image_to_base64(image)
base64[:30] # 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
```

## Convert base64 to pil image
```py
import img64

base64 = 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
image = img64.base64_to_image(base64, type='pil')
type(image) # PIL.Image.Image
```

## Convert base64 to numpy image
```py
import img64

base64 = 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
image = img64.base64_to_image(base64, type='numpy')
type(image) # numpy.ndarray
```