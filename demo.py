from PIL import Image
import io
import base64
import numpy as np
import io
from typing import Union

img0 = Image.open('sample.jpg').convert('RGB')
img1 = Image.open('sample.jpg').convert('RGB')
img2 = Image.open('sample.png').convert('RGB')
img_g = Image.open('sample_grayscale.jpg')

img1 = np.array(img1)
type(img1)

img1.tobytes()[:30]
img1_bytes = img1.tobytes()
img_bytes = img1_bytes

# -------- equal test --------------------------------------------------

img == img1
img1 == Image.fromarray(np.array(img1))
img1 == img2

np.array_equal(img, img1)
np.array_equal(img, Image.fromarray(np.array(img1)))
np.array_equal(img1, img2)

# ----------------------------------------------------------

buffer = io.BytesIO()
# img.save(buffer, format='JPEG')
img.save(buffer, format="PNG")

img_bytes = buffer.getvalue()
img_b64 = base64.b64encode(img_bytes)
img_b64_utf8 = img_b64.decode("utf-8")

img_bytes[:30]
img_b64[:30]
img_b64_utf8[:30]

# ----------------------------------------------------------


img_bytes = base64.b64decode(img_b64_utf8)
buffer = io.BytesIO(img_bytes)
img = Image.open(buffer)


# numpy array의 결과는 1차원 array로 flatten 되는 문제가 있음!
# 따라서, PIL 기준의 io.BytesIO() 통한 인코딩으로 통합
img_array = np.frombuffer(img_bytes, dtype=np.uint8)
Image.fromarray(img_array).convert('RGB')


np.array_equal(img1, img_array)

# ----------------------------------------------------------

def image_to_base64(image: Union[Image.Image, np.ndarray]) :
    if type(image) == np.ndarray :
    pass

def base64_to_image() :
    pass


# ----------------------------------------------------------




def b64string_to_image(b64string) :
    b64 = base64.b64decode(b64string)
    img_bytes = io.BytesIO(b64)
    return Image.open(img_bytes)

def image_to_b64string(img) :
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    img_b64 = base64.b64encode(buffered.getvalue())
    img_b64string = img_b64.decode("utf-8")
    return img_b64string