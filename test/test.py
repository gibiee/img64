from PIL import Image
import img64

img = Image.open('sample.jpg')
chars = 30

img_b64 = img64.image_to_base64(img)
print(img_b64[:chars])
img_bytes = img64.image_to_bytes(img)
print(img_bytes[:chars])
img_bytes = img64.image_to_bytes(img, format='JPEG')
print(img_bytes[:chars])

t = img64.bytes_to_base64(img_bytes)
print(t[:chars])
t = img64.bytes_to_image(img_bytes)
print(t)

t = img64.base64_to_bytes(img_b64)
print(t[:chars])
t = img64.base64_to_image(img_b64)
print(t)