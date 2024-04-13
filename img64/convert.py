import io
import base64
import numpy as np
from PIL import Image
from typing import Union, Literal

def image_to_bytes(img: Union[Image.Image, np.ndarray]) -> bytes :
    if isinstance(img, np.ndarray) :
        img = Image.fromarray(img)
    
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    return img_bytes

def image_to_base64(img: Union[Image.Image, np.ndarray]) -> str :
    img_bytes = image_to_bytes(img)
    img_b64 = base64.b64encode(img_bytes)
    img_b64_utf8 = img_b64.decode("utf-8")
    return img_b64_utf8

def base64_to_bytes(b64: str) -> bytes :
    img_bytes = base64.b64decode(b64)
    return img_bytes
    
def base64_to_image(b64: str, type: Literal['pil', 'numpy']='pil') -> Union[Image.Image, np.ndarray] :
    assert type in ['pil', 'numpy'], "Expected type 'pil' or 'numpy'"
    
    img_bytes = base64_to_bytes(b64)
    buffer = io.BytesIO(img_bytes)
    img = Image.open(buffer)
    img = np.array(img) # RGB 이미지가 PIL.PngImagePlugin.PngImageFile 객체인 현상 방지

    if type == 'numpy' : return img
    else : return Image.fromarray(img)