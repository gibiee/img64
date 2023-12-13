from PIL import Image
import img64

img_jpg = Image.open('sample.jpg').convert('RGB')
img_png = Image.open('sample.png').convert('RGB')
img_gray = Image.open('sample_grayscale.jpg').convert('L')

img64.base64_to_image(img64.image_to_base64(img_jpg), type="pil")
img64.base64_to_image(img64.image_to_base64(img_png), type="numpy")
img64.base64_to_image(img64.image_to_base64(img_gray), type="pil")
img64.base64_to_image(img64.image_to_base64(img_gray), type="numpy")

