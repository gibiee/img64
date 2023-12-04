from PIL import Image
import io
import base64
import numpy as np

img = Image.open('sample.jpg').convert('RGB')
img1 = Image.open('sample.jpg').convert('RGB')
img2 = Image.open('sample.png').convert('RGB')

img == img1
img1 == Image.fromarray(np.array(img1))
img1 == img2


np.array_equal(img, img1)
np.array_equal(img, Image.fromarray(np.array(img1)))
np.array_equal(img1, img2)







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