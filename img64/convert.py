import io
import base64 as _base64
import numpy as np
from PIL import Image
from typing import Union, Literal

def image_to_base64(image: Union[Image.Image, np.ndarray]) -> str :
    if isinstance(image, np.ndarray) :
        image = Image.fromarray(image)

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")

    image_bytes = buffer.getvalue()
    image_b64 = _base64.b64encode(image_bytes)
    image_b64_utf8 = image_b64.decode("utf-8")

    return image_b64_utf8

def base64_to_image(base64: str, type: Literal["pil", "numpy"]='pil') -> Union[Image.Image, np.ndarray] :
    assert type in ["pil", "numpy"], "Expected type 'pil' or 'numpy'"
    img_bytes = _base64.b64decode(base64)
    buffer = io.BytesIO(img_bytes)
    img = Image.open(buffer)
    img = np.array(img)

    if type == 'pil' :
        img = Image.fromarray(img)
    
    return img
