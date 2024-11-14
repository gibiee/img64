import io
import base64
import numpy as np
from PIL import Image
from typing import Union, Literal

 # image → bytes → base64
def image_to_bytes(img: Union[Image.Image, np.ndarray], format: str='PNG') -> bytes :
    if isinstance(img, np.ndarray) :
        img = Image.fromarray(img)
    
    with io.BytesIO() as buffer :
        img.save(buffer, format=format)
        img_bytes = buffer.getvalue()
    return img_bytes

def bytes_to_base64(img_bytes: bytes) -> str :
    img_b64 = base64.b64encode(img_bytes)
    img_b64_utf8 = img_b64.decode("utf-8")
    return img_b64_utf8

def image_to_base64(img: Union[Image.Image, np.ndarray], format: str='PNG') -> str :
    img_bytes = image_to_bytes(img, format)
    img_b64_utf8 = bytes_to_base64(img_bytes)
    return img_b64_utf8

# base64 → bytes → image
def base64_to_bytes(b64: str) -> bytes :
    img_bytes = base64.b64decode(b64)
    return img_bytes

def bytes_to_image(img_bytes: bytes, out_type: Literal['pil', 'numpy']='pil') -> Union[Image.Image, np.ndarray] :
    assert out_type in ['pil', 'numpy'], "Expected type 'pil' or 'numpy'"

    with io.BytesIO(img_bytes) as buffer :
        img = Image.open(buffer)
        img = np.array(img) # RGB 이미지가 PIL.PngImagePlugin.PngImageFile 객체인 현상 방지
    if out_type == 'numpy' :
        return img
    else :
        return Image.fromarray(img)
    
def base64_to_image(b64: str, out_type: Literal['pil', 'numpy']='pil') -> Union[Image.Image, np.ndarray] :
    assert out_type in ['pil', 'numpy'], "Expected type 'pil' or 'numpy'"

    img_bytes = base64_to_bytes(b64)
    if out_type == 'numpy' :
        return bytes_to_image(img_bytes, out_type='numpy')
    else :
        return bytes_to_image(img_bytes, out_type='pil')