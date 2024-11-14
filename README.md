![PyPI - Version](https://img.shields.io/pypi/v/img64)
![PyPI - Downloads](https://img.shields.io/pypi/dm/img64?color=red)
![PyPI - License](https://img.shields.io/pypi/l/img64)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/img64)

<p align="center">
  <img src="https://github.com/gibiee/img64/assets/37574274/1e4ba6f4-776d-4e84-b589-09f75d64d175" width="50%" height="50%" />
</p>

This library converts images to base64 encoding and vice versa.


# Installation
```sh
pip install img64
```


# Quick start

## Convert Image to Base64
```py
from PIL import Image
import cv2
import img64

# PIL image to Base64
image = Image.open('sample.png')
base64 = img64.image_to_base64(image)
base64[:30] # 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'

# Numpy(OpenCV) image to Base64
image = cv2.imread('sample.png')
image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
base64 = img64.image_to_base64(image)
base64[:30] # 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
```

## Convert Base64 to Image
```py
import img64

# Base64 to PIL image
base64 = 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
image = img64.base64_to_image(base64, type='pil')
type(image) # PIL.Image.Image

# Base64 to Numpy(OpenCV) image
base64 = 'iVBORw0KGgoAAAANSUhEUgAABAAAAA...'
image = img64.base64_to_image(base64, type='numpy')
type(image) # numpy.ndarray
```

# Information
- It was implemented by referencing [ternaus/base64ToImageConverters](https://github.com/ternaus/base64ToImageConverters).
  - The referenced library doesn't ensure data consistency, but this library addresses that issue.
  - This library enhances user convenience in handling both RGB and grayscale images.
