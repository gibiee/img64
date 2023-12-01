from PIL import Image
import io
import base64

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